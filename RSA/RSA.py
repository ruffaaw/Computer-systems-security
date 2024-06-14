from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, inverse

def generate_large_prime(bits):
    return getPrime(bits)

def generate_rsa_keys(bits):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    et = (p - 1) * (q - 1)
    e = 65537  
    d = inverse(e, et)
    return {'public': (n, e), 'private': (n, d)}

def block_to_number(block):
    return bytes_to_long(block)

def number_to_block(number, block_size):
    block = bytearray()
    while number > 0:
        block.append(number & 0xFF)
        number >>= 8
    block.reverse()
    return bytes(block).rjust(block_size, b'\x00')

def encrypt_with_blocks(message, n, e, block_size):
    padded_message = message.ljust((len(message) + block_size - 1) // block_size * block_size, b'\x00')
    encrypted_blocks = []
    for i in range(0, len(padded_message), block_size):
        block = padded_message[i:i + block_size]
        block_num = block_to_number(block)
        encrypted_num = pow(block_num, e, n)
        encrypted_blocks.append(format(encrypted_num, 'x'))
    return ' '.join(encrypted_blocks)

def decrypt_with_blocks(encrypted_message, n, d, block_size):
    decrypted_blocks = []
    for block in encrypted_message.split(' '):
        encrypted_num = int(block, 16)
        decrypted_num = pow(encrypted_num, d, n)
        decrypted_blocks.append(number_to_block(decrypted_num, block_size).rstrip(b'\x00').decode('utf-8'))
    return ''.join(decrypted_blocks)

def read_message_from_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

key_size = 768
keys = generate_rsa_keys(key_size)
message = read_message_from_file('file.txt')
block_size = 10
encrypted_message = encrypt_with_blocks(message, keys['public'][0], keys['public'][1], block_size)
decrypted_message = decrypt_with_blocks(encrypted_message, keys['private'][0], keys['private'][1], block_size)

print("Original message:", message.decode('utf-8'))
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

if message.decode('utf-8') == decrypted_message:
    print("matches")
else:
    print("does not match")
