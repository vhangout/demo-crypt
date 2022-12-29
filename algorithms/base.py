import secrets
import string
import zlib
from abc import ABC, abstractmethod


class CryptBase(ABC):
    def __init__(self, message):
        self.message = message
        self.crc = hex(zlib.crc32(self.message.encode('utf-8')))
        self.crypt_message = ''

    def __str__(self):
        return '\n'.join(
            ['-' * 32, f'Message: {self.message}', f'CRC32: {self.crc}',
             f'Algorithm: {self._name}',
             f'Parameters -> {self._parameters}',
             f'KEY: {self.key}',
             f'Crypted message: {self.crypt_message}', '-' * 32])

    @staticmethod
    def _remove_punctuation(s: str) -> str:
        return s.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def _gen_pass(pass_len=5, alphabet=string.ascii_letters + string.digits):  # default password gen
        return ''.join(secrets.choice(alphabet) for x in range(pass_len))

    @property
    def _name(self):
        pass

    @property
    def _parameters(self):
        pass

    @abstractmethod
    def crypt(self):
        pass
