import math

def encrypt(message, public_key):
    ciphertext = pow(message, public_key[0], public_key[1])
    return ciphertext

def decrypt(ciphertext, private_key):
    plaintext = pow(ciphertext, private_key[0], private_key[1])
    return plaintext

def generate_keys():
    p = 7
    q = 17
    n = p * q
    m = (p - 1) * (q - 1)

    for i in range(2, m):
        if math.gcd(i, m) == 1:
            e = i
            break

    for i in range(m):
        if (e * i) % m == 1:
            d = i
            break

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

message = int(input("Enter the message to be encrypted: "))
public_key, private_key = generate_keys()

print("Original Message is: ", message)
CT = encrypt(message, public_key)
print("Encrypted Message is: ", CT)
PT = decrypt(CT, private_key)
print("Decrypted Message is: ", PT)