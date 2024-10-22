import hashlib

def sha256_hash(message):
    message_bytes = message.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message_bytes)
    return sha256_hash.hexdigest()

if __name__ == '__main__':
    message = "Hello, World!"
    hash_value = sha256_hash(message)
    print(f"Message: {message}")
    print(f"SHA-256 Hash: {hash_value}")
