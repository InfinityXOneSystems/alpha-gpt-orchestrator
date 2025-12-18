from fastapi import APIRouter
import json

router = APIRouter()

@router.get('/ledger')
def ledger():
    with open('ledger/chain_ledger.jsonl','r') as f:
        return [json.loads(l) for l in f.readlines()[-200:]]
