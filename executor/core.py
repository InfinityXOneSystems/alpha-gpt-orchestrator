class ExecutorCore:
    def execute(self, plan: list):
        for step in plan:
            print(f'[EXECUTE] {step}')
