from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_DES(data, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data, DES.block_size)
    return cipher.encrypt(padded_data)

def decrypt_DES(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, DES.block_size)

def main():
    # Key must be 8 bytes long
    key = get_random_bytes(8)

    # Input data to be encrypted
    data = b"Hello, DES encryption!"

    # Encrypt data
    ciphertext = encrypt_DES(data, key)
    print("Cipher Text:", ciphertext.hex())

    # Decrypt data
    decrypted_data = decrypt_DES(ciphertext, key)
    print("Decrypted Text:", decrypted_data.decode("utf-8"))

if __name__ == "__main__":
    main()
