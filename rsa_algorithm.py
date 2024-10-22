import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

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

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    public_key, private_key = generate_keys()
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    message = "Hello RSA!"
    
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")