from fastapi import Request, HTTPException
from datetime import datetime
from services.guardian.validators.calendar import calendar_check
from services.guardian.validators.tasks import task_check
from services.guardian.validators.manifest import manifest_check
from services.guardian.audit.logger import log_decision

class GuardianAgent:
    NAME = "Guardian"
    ROLE = "Governance & Validation Authority"

    def validate(self, request: Request):
        decision_log = {
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path,
            "method": request.method
        }

        try:
            manifest_check()
            calendar_check(request)
            task_check(request)

            decision_log["result"] = "APPROVED"
            log_decision(decision_log)
            return True

        except Exception as e:
            decision_log["result"] = "DENIED"
            decision_log["reason"] = str(e)
            log_decision(decision_log)
            raise HTTPException(status_code=403, detail=f"Guardian Denial: {e}")
