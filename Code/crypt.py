import hashlib, secrets,string
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    """This class is implemented for the encryption and decryption of the messages and the password of the user. |br|
    The member functions are: |br|
    1. Constructor |br|
    2. msg_decrypt |br|
    3. msg_encrypt |br|
    4. __pad |br|
    5. __unpad

    :param object: It is the Cipher object.
    :type object: Object with certain attributes
    """
    def __init__(self, key):
        """A constructor which recieves a key of any length and generates a 256 bit hash from that key.

        :param key: Key which is to be hashed
        :type key: string
        """
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def msg_decrypt(self, text):
        """Function to decrypt the encrypted message. It backtracks all the processes in the encrypt function and proceeds to decrypt it.

        :param text: The encrypted text that needs to be decrypted
        :type text: string
        :return: the decrypted text
        :rtype: string
        """
        text = b64decode(text)
        iv = text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)
    
    def msg_encrypt(self, text):
        """Function to encrypt the plain text. It first pad the plain text and then proceeds to encrypt it.

        :param text: Plain text that has to be encrypted
        :type text: string
        :return: the encrypted text
        :rtype: string
        """
        text = self.__pad(text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def __pad(self, text):
        """ It receives the plain text to be encrypted and adds a number bytes for the text to be a multiple of 128 bits.

        :param text: Text which is to be padded
        :type text: string
        :return: padded text
        :rtype: string
        """
        number_of_bytes_to_pad = self.block_size - len(text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = text + padding_str
        return padded_plain_text
    
    @staticmethod
    def __unpad(text):
        """It will receive the decrypted text, also known as plain text and will remove all the extra added characters in the __pad method

        :param text: Text that has to be unpadded
        :type text: string
        :return: unpadded text
        :rtype: string
        """
        lastchar = text[len(text) - 1:]
        return text[:-ord(lastchar)]
    
#References: https://medium.com/quick-code/aes-implementation-in-python-a82f582f51c2
