import hashlib

def generate_key(*args) -> str:
    combined = "|".join(str(arg) for arg in args if arg is not None)
    return hashlib.sha256(combined.encode()).hexdigest()[:16]