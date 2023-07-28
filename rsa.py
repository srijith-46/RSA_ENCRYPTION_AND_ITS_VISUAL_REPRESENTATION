import random
import math
import hashlib

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(public_key, message):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    md5_checksum = hashlib.md5(message.encode('utf-8')).hexdigest()
    # convert to string
    encrypted = f"{encrypted}"
    return (encrypted, md5_checksum)


def decrypt(private_key, encrypted, md5_checksum):
    d, n = private_key

    decrypted = [pow(char, d, n) for char in encrypted]
    message = ''.join([chr(char) for char in decrypted])
    # message = message + "corrupt"
    md5_checksum_calculated = hashlib.md5(message.encode('utf-8')).hexdigest()
    # return message
    if md5_checksum == md5_checksum_calculated:
        return message
    else:
        return "Message was corrupted" 
