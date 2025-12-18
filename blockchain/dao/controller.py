from ledger.chain_ledger import append

def request_approval(action:str, proposer:str):
    append({
        'type':'DAO_REQUEST',
        'action': action,
        'proposer': proposer
    })
    return {'status':'pending'}
