import base64
from rich import print
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Переменная должна быть постоянной, чтобы один и тот же пароль давал один и тот же ключ
SALT = b'diary_salt_123'


def get_key_from_password(password: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


# Шифрование
def encrypt_name(name: str, password: str) -> str:
    f = Fernet(get_key_from_password(password))
    return f.encrypt(name.encode()).decode()


# Дешифрование
def decrypt_name(encrypted_name: str, password: str) -> str:
    try:
        f = Fernet(get_key_from_password(password))
        return f.decrypt(encrypted_name.encode()).decode()
    except Exception:
        return None
