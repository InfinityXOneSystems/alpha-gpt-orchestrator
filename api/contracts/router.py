from fastapi import APIRouter
from blockchain.contracts.generator import generate_contract
from blockchain.compiler.compiler import compile_contract

router = APIRouter()

@router.post('/author')
def author(prompt:dict):
    intent = prompt.get('intent','')
    template = generate_contract(intent)
    compiled = compile_contract(template)
    return {
        'intent': intent,
        'template': template,
        'compiled': compiled
    }
