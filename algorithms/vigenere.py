import random
import string

from algorithms.base import CryptBase


class Viginere(CryptBase):
    def __init__(self, message):
        super().__init__(self._remove_punctuation(message.upper()).replace(' ', ''))
        self.key_range = (5, 10)
        self.key = self._gen_pass(random.randint(*self.key_range), string.ascii_uppercase).upper()
        self.tabula_recta = [string.ascii_uppercase[i:] + string.ascii_uppercase[:i] for i in
                             range(len(string.ascii_uppercase))]
        a = 1

    def crypt(self) -> str:
        self.crypt_message = ''.join(
            self.tabula_recta[ord(letter) - ord('A')][ord(self.key[idx % len(self.key)]) - ord('A')] for idx, letter in
            enumerate(self.message))

    @property
    def _name(self):
        return 'Viginere'

    @property
    def _parameters(self):
        return f'Key Length: {self.key_range}'
