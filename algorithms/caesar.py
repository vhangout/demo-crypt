import random
import string

from algorithms.base import CryptBase


class Caesar(CryptBase):
    def __init__(self):
        super().__init__()
        self.shift_range = (-20, 20)

    def generate(self, message):
        super().generate(self._remove_punctuation(message.upper()))
        self.key = random.randint(*self.shift_range)
        alphabet = string.ascii_uppercase[-self.key:] + string.ascii_uppercase[:-self.key]
        self.crypt_message = ''.join(
            alphabet[self._ord(letter)] if letter != ' ' else ' ' for letter in self.message)

    @property
    def _name(self):
        return 'Шифр Цезаря'

    @property
    def _teacher(self):
        return [self._name,
                f'Сообщение: {self.message}',
                f'CRC32: {self.crc32}',
                f'Алфавит: {string.ascii_uppercase}',
                f'Диапазон сдвига: {self.shift_range}',
                f'Ключ: {self.key}',
                f'Шифрованое сообщение: {self.crypt_message}']

    @property
    def _student(self):
        return ['Восстановите исходное сообщение зашифрованое шифом Цезаря',
                f'CRC32 оригинального сообщения: {self.crc32}',
                f'Алфавит: {string.ascii_uppercase}',
                f'Диапазон сдвига: {self.shift_range}',
                f'Шифрованое сообщение: {self.crypt_message}']
