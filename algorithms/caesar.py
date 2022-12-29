import random
import string

from algorithms.base import CryptBase


class Caesar(CryptBase):
    def __init__(self, message):
        super().__init__(self._remove_punctuation(message.upper()))
        self.shift_range = (-20, 20)
        self.key = random.randint(*self.shift_range)
        self.alphabet = string.ascii_uppercase[-self.key:] + string.ascii_uppercase[:-self.key]

    def crypt(self) -> str:
        self.crypt_message = ''.join(
            self.alphabet[ord(letter) - ord('A')] if letter != ' ' else ' ' for letter in self.message)

    @property
    def _name(self):
        return 'Caesar'

    @property
    def _parameters(self):
        return f'Shift range: {self.shift_range}'
