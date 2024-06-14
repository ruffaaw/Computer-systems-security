def decrypt(cryptogram, key):
    message = []
    for i, j in zip(cryptogram, key):
        message.append((i - j) % 2)
    return message