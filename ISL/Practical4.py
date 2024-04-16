from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_AES(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    return ct_bytes, iv

def decrypt_AES(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt

def main():
    # Key must be either 16, 24, or 32 bytes long (AES-128, AES-192, AES-256)
    key = get_random_bytes(16)

    # Input data to be encrypted
    data = b"Hello, AES encryption!"

    # Encrypt data
    ciphertext, iv = encrypt_AES(data, key)
    print("Cipher Text:", ciphertext.hex())

    # Decrypt data
    decrypted_data = decrypt_AES(ciphertext, key, iv)
    print("Decrypted Text:", decrypted_data.decode("utf-8"))

if __name__ == "__main__":
    main()