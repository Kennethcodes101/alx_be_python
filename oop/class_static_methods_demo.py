class Calculator:

    claculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.claculation_type}")
        return a * b