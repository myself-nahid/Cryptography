import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_prime(start, end):
    while True:
        num = random.randint(start, end)
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            return num

def generate_keys():
    p = generate_prime(100, 300)
    q = generate_prime(100, 300)
    
    n = p * q
    
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def blind_message(public_key, message):
    e, n = public_key
    r1 = random.randint(2, n - 1)
    while gcd(r1, n) != 1:
        r1 = random.randint(2, n - 1)
    
    m_blinded = (message * pow(r1, e, n)) % n
    r2 = random.randint(1, n - 1)
    return m_blinded, r1, r2

def sign_message(private_key, blinded_message):
    d, n = private_key
    signature_blinded = pow(blinded_message, d, n)
    return signature_blinded

def unblind_signature(public_key, signature_blinded, r1):
    e, n = public_key
    r1_inv = mod_inverse(r1, n)
    signature = (signature_blinded * r1_inv) % n
    return signature

def verify_signature(public_key, message, signature):
    e, n = public_key
    return pow(signature, e, n) == message

if __name__ == '__main__':
    public_key, private_key = generate_keys()
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    message = 12345  
    print(f"Original Message: {message}")
    
    blinded_message, r1, r2 = blind_message(public_key, message)
    print(f"Blinded Message: {blinded_message}")
    print(f"Random Factor r1: {r1}, r2: {r2}")
    
    signature_blinded = sign_message(private_key, blinded_message)
    print(f"Blinded Signature: {signature_blinded}")
    
    signature = unblind_signature(public_key, signature_blinded, r1)
    print(f"Unblinded Signature: {signature}")
    
    is_valid = verify_signature(public_key, message, signature)
    print(f"Signature Valid: {is_valid}")
