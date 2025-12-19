import time

from control.manifest_loader import Manifest
from crawler.universal.crawler import UniversalCrawler
from vision_cortex.controller import VisionCortexController
from predictor.market import MarketPredictor
from planner.core import PlannerCore
from executor.core import ExecutorCore
from governance.engine import GovernanceEngine
from validation.engine import ValidationEngine

class AutoLoop:
    def __init__(self, interval=60):
        self.manifest = Manifest()

        if not self.manifest.enabled('autonomy.enabled'):
            raise RuntimeError('Autonomy disabled by manifest')

        self.interval = self.manifest.get('crawler.interval_seconds', interval)

        self.crawler = UniversalCrawler()
        self.vision = VisionCortexController()
        self.predictor = MarketPredictor()
        self.planner = PlannerCore()
        self.executor = ExecutorCore()
        self.governance = GovernanceEngine()
        self.validator = ValidationEngine()

    def run_cycle(self):
        if not self.governance.authorize('auto_cycle', {}):
            return

        data = self.crawler.crawl()
        insights = self.vision.process(data)
        forecast = self.predictor.predict(insights)
        plan = self.planner.plan(forecast)
        self.executor.execute(plan)

    def start(self):
        while True:
            try:
                self.run_cycle()
            except Exception as e:
                print(f'[AUTOLOOP ERROR] {e}')
            time.sleep(self.interval)
