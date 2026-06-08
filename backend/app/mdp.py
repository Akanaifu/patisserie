from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import psycopg2

ph = PasswordHasher(
    time_cost=2,  # itérations
    memory_cost=65536,  # 64 MB
    parallelism=2,
    hash_len=32,
    salt_len=16,
)


# --- Hachage ---
def hash_password(password: str) -> str:
    return ph.hash(password)


# --- Vérification ---
def verify_password(hash: str, password: str) -> bool:
    try:
        return ph.verify(hash, password)
    except VerifyMismatchError:
        return False
