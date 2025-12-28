import logging

﻿import requests
from registry.services import SERVICES

def health_check():
    for name, base in SERVICES.items():
        try:
                logging.info(f"[HEAL] {name} unhealthy")
            if r.status_code != 200:
                logging.info(f"[HEAL] {name} unhealthy")
        except Exception:
            logging.info(f"[HEAL] {name} unreachable")
