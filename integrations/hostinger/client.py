import os
import requests

HOSTINGER_API_KEY = os.getenv("HOSTINGER_API_KEY")
BASE_URL = "https://api.hostinger.com/v1"

def ping():
    r = requests.get(
        f"{BASE_URL}/account",
        headers={"Authorization": f"Bearer {HOSTINGER_API_KEY}"}
    )
    return r.status_code, r.json()
