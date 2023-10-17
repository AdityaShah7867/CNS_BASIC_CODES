from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a random 256-bit key
key = get_random_bytes(32)

# Initialize the AES cipher in ECB mode (not recommended for security reasons)
cipher = AES.new(key, AES.MODE_ECB)

# Data to be encrypted
data = b'This is a secret message. '

# Pad the data to be a multiple of block size
padded_data = pad(data, AES.block_size)

# Encrypt the padded data
encrypted_data = cipher.encrypt(padded_data)

print("Encrypted data:", encrypted_data)

# Decrypt the encrypted data
decrypted_data = cipher.decrypt(encrypted_data)

# Unpad the decrypted data
unpadded_data = unpad(decrypted_data, AES.block_size)

print("Decrypted data:", unpadded_data.decode('utf-8'))
