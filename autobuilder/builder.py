def build_system(spec:dict):
    return {
        'system_name': spec.get('name','generated-system'),
        'agents': spec.get('agents', []),
        'storage': spec.get('storage', []),
        'status': 'built'
    }
