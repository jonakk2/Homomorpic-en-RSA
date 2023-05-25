import random
import math

# Funkce pro generování náhodných prvočísel
def generate_prime():
    while True:
        num = random.randint(2**15, 2**16)  # Vygenerujeme náhodné číslo mezi 2^15 a 2^16
        if is_prime(num):
            return num

# Funkce pro ověření, zda je číslo prvočíslo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Funkce pro výpočet největšího společného dělitele (NSD) pomocí Euklidova algoritmu
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Funkce pro výpočet inverzního prvku pomocí rozšířeného Euklidova algoritmu
def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None  # Inverzní prvek neexistuje
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        quotient = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - quotient * v1), (u2 - quotient * v2), (u3 - quotient * v3), v1, v2, v3
    return u1 % m

# Funkce pro šifrování zprávy
def encrypt(message, public_key):
    n, e = public_key
    ciphertext = pow(message, e, n)
    return ciphertext

# Funkce pro dešifrování zprávy
def decrypt(ciphertext, private_key):
    n, d = private_key
    message = pow(ciphertext, d, n)
    return message

# Generování RSA klíčů
def generate_keypair():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
    d = mod_inverse(e, phi)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

# Funkce pro homomorfní násobení šifrových textů
def homomorphic_multiply(ciphertext_a, ciphertext_b, public_key):
    n, e = public_key
    result = (ciphertext_a * ciphertext_b) % n
    return result

# Volání funkcí
public_key, private_key = generate_keypair()

openTextA = 42
openTextB = 31
# Šifrování původního otevřeného textu
ciphertext_a = encrypt(openTextA, public_key)
ciphertext_b = encrypt(openTextB, public_key)

# Násobení šifrových textů
ciphertext_result = homomorphic_multiply(ciphertext_a, ciphertext_b, public_key)

# Dešifrování výsledku
result_message = decrypt(ciphertext_result, private_key)

# Výpis výsledků
print("Zašifrovaná zpráva A:", ciphertext_a)
print("Zašifrovaná zpráva B:", ciphertext_b)
print("Původní zpráva A:", decrypt(ciphertext_a,private_key))
print("Původní zpráva B:", decrypt(ciphertext_b, private_key))
print("výsledek homomorfního šifrování:", ciphertext_result)
print("Výsledek po dešifrování:", result_message)
print("Vynásobení A*B:", openTextA*openTextB)