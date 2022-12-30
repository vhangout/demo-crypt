import secrets
import string
import zlib
from abc import ABC, abstractmethod


class CryptBase(ABC):
    def __init__(self):
        self.message = ''
        self.crc32 = ''
        self.crypt_message = ''

    @property
    def _teacher(self):
        pass

    @property
    def _student(self):
        pass

    @property
    def teacher(self):
        return f"{'-' * 32}\n{chr(10).join(self._teacher)}\n{'-' * 32}"

    @property
    def student(self):
        return f"{'-' * 32}\n{chr(10).join(self._student)}\n{'-' * 32}"

    @staticmethod
    def _remove_punctuation(s: str) -> str:
        return s.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def _gen_pass(pass_len=5, alphabet=string.ascii_letters + string.digits):  # default password gen
        return ''.join(secrets.choice(alphabet) for x in range(pass_len))

    @staticmethod
    def _ord(letter) -> int:
        return ord(letter) - ord('A')

    @staticmethod
    def _bytes(s: str) -> int:
        return bytearray(s, encoding='utf-8')

    @property
    def _name(self):
        pass

    @property
    def _parameters(self):
        pass

    def generate(self, message):
        self.message = message
        self.crc32 = hex(zlib.crc32(self.message.encode('utf-8')))
        self.crypt_message = ''



"""
    f'Message: {self.message}', f'CRC32: {self.crc}',
    f'Algorithm: {self._name}',
    f'Parameters -> {self._parameters}',
    f'KEY: {self.key}',
    f'Crypted message: {self.crypt_message}',
"""