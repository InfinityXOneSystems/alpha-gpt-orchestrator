def generate_contract(intent:str):
    if 'real estate' in intent.lower():
        return 'escrow.sol'
    return 'generic.sol'
