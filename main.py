# ============================================================
# INFINITY XOS — ALPHA GPT ORCHESTRATOR (FINAL BOOTSTRAP)
# Authoritative • Proof-first • Autonomous • FAANG-grade
# ============================================================

import os, sys, time, base64, threading, json
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

import httpx
import jwt
from fastapi import FastAPI, HTTPException

# ============================================================
# FASTAPI APP (SINGLE SOURCE OF TRUTH)
# ============================================================

app = FastAPI(title="Infinity XOS — Alpha GPT Orchestrator")

# ============================================================
# GLOBAL STATE (NO SILENT LIES)
# ============================================================

STATE = {
    "identity": "InfinityXOS",
    "mode": "AUTONOMOUS",
    "leader": True,
    "boot_time": None,
    "runtime": os.getenv("K_SERVICE", "LOCAL"),
    "policy": {"no_deletion": True}
}

LEDGER: List[Dict[str, Any]] = []
RUNS: Dict[str, Dict[str, Any]] = {}
SERVICE_REGISTRY: List[Dict[str, Any]] = []

# ============================================================
# UTILITIES
# ============================================================

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

def log(event: str, meta: Optional[Dict[str, Any]] = None):
    entry = {"ts": now(), "event": event, "meta": meta or {}}
    LEDGER.append(entry)
    print(entry, flush=True)

def new_run(kind: str) -> str:
    rid = f"{kind}-{int(time.time())}"
    RUNS[rid] = {
        "run_id": rid,
        "kind": kind,
        "start": now(),
        "end": None,
        "status": "STARTED",
        "results": None,
        "errors": None
    }
    log("run_started", {"run_id": rid, "kind": kind})
    return rid

def end_run(rid: str, status: str, results=None, errors=None):
    r = RUNS.get(rid)
    if not r:
        return
    r["end"] = now()
    r["status"] = status
    r["results"] = results
    r["errors"] = errors
    log("run_completed", {"run_id": rid, "status": status})

# ============================================================
# ROUTE ENFORCEMENT (NO MORE 404 BULLSHIT)
# ============================================================

REQUIRED_ROUTES = [
    "/health",
    "/state",
    "/bootstrap",
    "/inventory",
    "/rehydrate",
    "/sync/all",
    "/run/all",
    "/emit/ledger",
    "/emit/runs",
    "/intent"
]

@app.on_event("startup")
def enforce_routes():
    existing = {r.path for r in app.routes}
    missing = [r for r in REQUIRED_ROUTES if r not in existing]
    log("route_enforcement", {
        "existing": sorted(existing),
        "missing": missing
    })
    if missing:
        raise RuntimeError(f"CRITICAL ROUTES MISSING: {missing}")

# ============================================================
# CREDENTIAL & CAPABILITY INVENTORY
# ============================================================

def inventory() -> Dict[str, Any]:
    inv = {
        "github": {
            "GITHUB_APP_ID": bool(os.getenv("GITHUB_APP_ID")),
            "GITHUB_APP_PRIVATE_KEY_B64": bool(os.getenv("GITHUB_APP_PRIVATE_KEY_B64")),
        },
        "google_cloud": {
            "GOOGLE_APPLICATION_CREDENTIALS": bool(os.getenv("GOOGLE_APPLICATION_CREDENTIALS")),
        },
        "openai": {
            "OPENAI_API_KEY": bool(os.getenv("OPENAI_API_KEY")),
        },
        "workspace_assumed_via_gcp_sa": bool(os.getenv("GOOGLE_APPLICATION_CREDENTIALS")),
    }
    missing = []
    for group in inv.values():
        if isinstance(group, dict):
            missing += [k for k, v in group.items() if not v]
    inv["missing"] = sorted(set(missing))
    return inv

# ============================================================
# GITHUB APP — FULL CONTROL PLANE
# ============================================================

GITHUB_API = "https://api.github.com"

def gh_private_key():
    return base64.b64decode(os.getenv("GITHUB_APP_PRIVATE_KEY_B64")).decode()

def gh_jwt():
    payload = {
        "iat": int(time.time()) - 30,
        "exp": int(time.time()) + 600,
        "iss": os.getenv("GITHUB_APP_ID"),
    }
    return jwt.encode(payload, gh_private_key(), algorithm="RS256")

async def gh_request(method, path, token, body=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.request(method, f"{GITHUB_API}{path}", headers=headers, json=body)
        if r.status_code >= 400:
            raise HTTPException(status_code=r.status_code, detail=r.text)
        return r.json() if r.text else {}

async def gh_installations():
    return await gh_request("GET", "/app/installations", gh_jwt())

async def gh_install_token(iid):
    return (await gh_request("POST", f"/app/installations/{iid}/access_tokens", gh_jwt()))["token"]

async def gh_repos(iid):
    t = await gh_install_token(iid)
    return (await gh_request("GET", "/installation/repositories?per_page=100", t))["repositories"]

async def gh_dispatch(owner, repo, iid):
    t = await gh_install_token(iid)
    await gh_request(
        "POST",
        f"/repos/{owner}/{repo}/actions/workflows/infinity-run.yml/dispatches",
        t,
        {"ref": "main", "inputs": {"mode": "run_all", "ts": now()}}
    )

# ============================================================
# CORE ENDPOINTS (MOBILE VERIFIABLE)
# ============================================================

@app.get("/health")
def health():
    return {"status": "ok", "role": "LEADER", "runtime": STATE["runtime"]}

@app.get("/state")
def state():
    return {
        "identity": STATE["identity"],
        "mode": STATE["mode"],
        "leader": STATE["leader"],
        "boot_time": STATE["boot_time"],
        "ledger_events": len(LEDGER),
        "runs": len(RUNS),
        "services": len(SERVICE_REGISTRY),
    }

@app.post("/bootstrap")
def bootstrap():
    if STATE["boot_time"] is None:
        STATE["boot_time"] = now()
        log("bootstrap_complete", STATE)
    return {"status": "ACTIVE", **STATE}

@app.post("/rehydrate")
def rehydrate():
    inv = inventory()
    log("rehydrate", inv)
    return {"status": "REHYDRATED", "missing": inv["missing"]}

@app.get("/inventory")
def inventory_endpoint():
    inv = inventory()
    log("inventory_emitted", inv)
    return inv

@app.get("/emit/ledger")
def emit_ledger(limit: int = 200):
    return LEDGER[-limit:]

@app.get("/emit/runs")
def emit_runs(limit: int = 50):
    return list(RUNS.values())[-limit:]

# ============================================================
# GLOBAL EXECUTION — RUN EVERYTHING
# ============================================================

@app.post("/sync/all")
async def sync_all():
    rid = new_run("sync_all")
    try:
        result = {
            "inventory": inventory(),
            "installations": [],
            "repos": []
        }
        for inst in await gh_installations():
            iid = inst["id"]
            result["installations"].append(inst["account"]["login"])
            for r in await gh_repos(iid):
                result["repos"].append(r["full_name"])
        end_run(rid, "COMPLETED", result)
        return {"run_id": rid, "result": result}
    except Exception as e:
        end_run(rid, "FAILED", errors=str(e))
        raise

@app.post("/run/all")
async def run_all():
    rid = new_run("run_all")
    dispatched = []
    try:
        for inst in await gh_installations():
            iid = inst["id"]
            for r in await gh_repos(iid):
                owner, repo = r["full_name"].split("/")
                await gh_dispatch(owner, repo, iid)
                dispatched.append(r["full_name"])
        end_run(rid, "COMPLETED", {"repos_dispatched": dispatched})
        return {"run_id": rid, "repos": len(dispatched)}
    except Exception as e:
        end_run(rid, "FAILED", errors=str(e))
        raise

@app.post("/intent")
def intent(payload: Dict[str, Any]):
    log("intent_received", payload)
    return {"status": "INTENT_ACCEPTED"}

# ============================================================
# END
# ============================================================
