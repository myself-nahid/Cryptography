import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, z):
    for d in range(1, z):
        if (e * d) % z == 1:
            return d
    return None

def generate_keys(p, q):
    n = p * q
    z = (p-1) * (q-1)
    
    e = 2
    while gcd(e, z) != 1:
        e += 1

    d = mod_inverse(e, z)
    
    return (e, d, n)

def encrypt(plain_text, public_key, n):
    encrypted_text = []
    for char in plain_text:
        m = ord(char) 
        cipher = pow(m, public_key, n) 
        encrypted_text.append(cipher)
    return encrypted_text

def decrypt(encrypted_text, secret_key, n):
    decrypted_text = ""
    for cipher in encrypted_text:
        m = pow(cipher, secret_key, n)
        decrypted_text += chr(m)
    return decrypted_text

def main():
    run = True
    while run:
        p, q = map(int, input("Enter two prime numbers separated by space:\n#> ").split())
        
        public_key, secret_key, n = generate_keys(p, q)
        
        print(f"\nPublic key (e, n): ({public_key}, {n})")
        print(f"Secret key (d, n): ({secret_key}, {n})")
        
        while True:
            print("\nCOMMANDS")
            print("-en encrypt plain text")
            print("-de decrypt encrypted text")
            print("-exit exit the program\n")
            command = input("#>")
            
            if "-exit" in command:
                run = False
                break
            
            if "-en" in command:
                plain_text = input("Enter plain text: ")
                encrypted_text = encrypt(plain_text, public_key, n)
                print("Encrypted text:", encrypted_text)
                
            if "-de" in command:
                encrypted_text = list(map(int, input("Enter encrypted text (space-separated numbers): ").split()))
                decrypted_text = decrypt(encrypted_text, secret_key, n)
                print("Decrypted text:", decrypted_text)

main()
