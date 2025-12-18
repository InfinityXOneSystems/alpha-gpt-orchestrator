from fastapi import APIRouter
from crypto.ethereum_wallet import create_eth_wallet
from crypto.bitcoin_wallet import create_btc_wallet
from predictor.market import predict

router = APIRouter()

@router.post('/wallet/ethereum')
def eth_wallet(label: str):
    return create_eth_wallet(label)

@router.post('/wallet/bitcoin')
def btc_wallet(label: str):
    return create_btc_wallet(label)

@router.post('/predict/market')
def market_predict(context: dict):
    return predict(context)
