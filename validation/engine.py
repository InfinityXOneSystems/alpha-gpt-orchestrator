class ValidationEngine:
    def validate(self, data) -> bool:
        return data is not None

    def heal(self, error: Exception):
        print(f'[AUTO-HEAL] {error}')
