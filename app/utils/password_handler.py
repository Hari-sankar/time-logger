import bcrypt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    
    # Generate salt and hash password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    # Convert hashed password to string before returning
    return hashed_password.decode("utf-8")
