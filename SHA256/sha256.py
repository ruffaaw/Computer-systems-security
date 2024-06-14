import hashlib
import time

def sha256(message):
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19
    
    bits = ''.join(format(ord(char), '08b') for char in message)
    bits += '1'
    
    while len(bits) % 512 != 448:
        bits += '0'
    
    bits += format(len(message) * 8, '064b')
    
    def right_rotate(x, n):
        return (x >> n) | (x << (32 - n)) & 0xFFFFFFFF
    
    def ch(x, y, z):
        return (x & y) ^ (~x & z)
    
    def maj(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)
    
    def sigma0(x):
        return right_rotate(x, 2) ^ right_rotate(x, 13) ^ right_rotate(x, 22)
    
    def sigma1(x):
        return right_rotate(x, 6) ^ right_rotate(x, 11) ^ right_rotate(x, 25)
    
    def delta0(x):
        return right_rotate(x, 7) ^ right_rotate(x, 18) ^ (x >> 3)
    
    def delta1(x):
        return right_rotate(x, 17) ^ right_rotate(x, 19) ^ (x >> 10)
    
    chunks = [bits[i:i+512] for i in range(0, len(bits), 512)]
    
    for chunk in chunks:
        words = [int(chunk[i:i+32], 2) for i in range(0, len(chunk), 32)]
        
        for i in range(16, 64):
            s0 = delta0(words[i-15])
            s1 = delta1(words[i-2])
            words.append((words[i-16] + s0 + words[i-7] + s1) & 0xFFFFFFFF)
        
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7
        
        for i in range(64):
            S1 = sigma1(e)
            ch_res = ch(e, f, g)
            temp1 = (h + S1 + ch_res + k[i] + words[i])
            S0 = sigma0(a)
            maj_res = maj(a, b, c)
            temp2 = (S0 + maj_res) 
            
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF
        
        # Aktualizacja wartości początkowych
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF
    
    digest = (h0 << 224) | (h1 << 192) | (h2 << 160) | (h3 << 128) | (h4 << 96) | (h5 << 64) | (h6 << 32) | h7
    
    return format(digest, '064x')

k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Length of both strings must be equal")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

message1 = "Hello world!"
message2 = "Hello world?"
time_start_my_sha256 = time.time()
time.sleep(1)
hash1 = sha256(message1)
time_end_my_sha256 = time.time()
my_duration = time_end_my_sha256-time_start_my_sha256
hash2 = sha256(message2)

print("Message 1:", message1)
print("SHA-256 Hash 1:", hash1)
print("Message 2:", message2)
print("SHA-256 Hash 2:", hash2)

print("Hamming distance between hash1 and hash2: ", hamming_distance(hash1, hash2))

time_start_library_sha256 = time.time()
time.sleep(1)
hashlib_hash1 = hashlib.sha256(message1.encode()).hexdigest()
time_end_library_sha256 = time.time()
hashlib_duration = time_end_library_sha256-time_start_library_sha256
print("\nHashlib SHA-256 Hash 1:", hashlib_hash1)

print("\nAre the hashes equal to their hashlib counterparts?")
print("Hash 1:", hash1 == hashlib_hash1)
print("Generation time by my program: ", my_duration)
print("Generation time by library functions: ", hashlib_duration)

if my_duration < hashlib_duration:
    print("My implementation is ", hashlib_duration-my_duration, "s faster.")
elif my_duration > hashlib_duration:
    print("Hashlib implementation is ", my_duration - hashlib_duration, "s faster.")
else:
    print("Both implementations took equal time.")