import subprocess
import uuid
from ledger.chain_ledger import append

MAX_INSTANCES = 5

def replicate(image='alpha-gpt-orchestrator', purpose='test'):
    instance_id = str(uuid.uuid4())[:8]

    subprocess.run([
        'docker', 'run', '-d',
        '--name', f'ai_clone_{instance_id}',
        image
    ])

    append({
        'type': 'LOCAL_AI_REPLICATED',
        'instance': instance_id,
        'purpose': purpose
    })

    return instance_id
