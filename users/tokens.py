import datetime
import random
from datetime import *
import jose
import string

secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1488)).lower()


def create_access_token(username: str) -> str:
    payload = {
        'iat': datetime.now(),  # Issued at time
        'exp': datetime.now(timezone.utc) + timedelta(days=30),  # expires after 30 days
        'sub': username  # Subject of the token (e.g., user ID)
    }
    encode_jwt = jose.encode(payload, algorithm="HS256")
    return encode_jwt


def decode(token: str) -> dict:
    return jose.decodeJwt(token)
