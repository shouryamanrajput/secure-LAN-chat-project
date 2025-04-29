def encrypt(message, key):
    encrypted = ''.join(chr(ord(c) ^ key) for c in message)
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ''.join(chr(ord(c) ^ key) for c in ciphertext)
    return decrypted