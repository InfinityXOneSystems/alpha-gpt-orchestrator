def call(model, prompt):
    return {
        'model': model,
        'response': f'Response from {model}',
        'confidence': 0.8
    }
