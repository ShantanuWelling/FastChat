from Crypto.Cipher import AES
import hashlib

class AESCipher:
    def __init__(self,key):
        self.key = key

    def msg_encrypt(self, msg):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(bytes(msg, 'utf-8'))
        nonce = cipher.nonce
        return (ciphertext,tag,nonce)

    def msg_decrypt(self, msg):
        cipher = AES.new(self.key, AES.MODE_EAX, msg[2])
        return cipher.decrypt_and_verify(msg[0], msg[1]).decode()