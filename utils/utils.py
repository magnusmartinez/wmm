import random
import string

def generate_random_code() -> str:
    """Generar un código aleatorio de 3 letras mayúsculas y 3 dígitos"""
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{letters}-{digits}"

grade_choices = [
    ('N/A', 'No agignado'),
    ('S1A', 'Primero A'),
    ('S1B', 'Primero B'),
    ('S1C', 'Primero C'),
    ('S2A', 'Segundo A'),
    ('S2B', 'Segundo B'),
    ('S2C', 'Segundo C'),
    ('S3A', 'Tercero A'),
    ('S3B', 'Tercero B'),
    ('S3C', 'Tercero C'),
    ('S4A', 'Cuarto A'),
    ('S4B', 'Cuarto B'),
    ('S4C', 'Cuarto C'),
    ('S5A', 'Quinto A'),
    ('S5B', 'Quinto B'),
    ('S5C', 'Quinto C'),
    ('S6A', 'Sexto A'),
    ('S6B', 'Sexto B'),
    ('S6C', 'Sexto C'),
]