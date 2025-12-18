from fastapi import APIRouter
from finance_agents.market_predictor import predict_market
from blockchain.wallets.replicator import replicate_wallets

router = APIRouter()

@router.post('/predict')
def api_predict(payload:dict):
    return predict_market(payload)

@router.post('/wallets/replicate')
def api_wallets(count:int=1):
    return replicate_wallets(count)
