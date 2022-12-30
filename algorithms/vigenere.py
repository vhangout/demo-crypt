import random
import string

from algorithms.base import CryptBase


class Viginere(CryptBase):
    def __init__(self):
        super().__init__()
        self.key_len = (5, 10)
        self.tabula_recta = [string.ascii_uppercase[i:] + string.ascii_uppercase[:i] for i in
                             range(len(string.ascii_uppercase))]
        a = 1

    def generate(self, message):
        super().generate(self._remove_punctuation(message.upper()).replace(' ', ''))
        self.key = self._gen_pass(random.randint(*self.key_len), string.ascii_uppercase)
        self.crypt_message = ''.join(
            self.tabula_recta[self._ord(letter)][self._ord(self.key[idx % len(self.key)])] for idx, letter in
            enumerate(self.message))

    @property
    def _name(self):
        return 'Шифр Виженера'

    @property
    def _teacher(self):
        return [self._name,
                f'Сообщение: {self.message}',
                f'CRC32: {self.crc32}',
                f'Алфавит: {string.ascii_uppercase}',
                f'Длина ключа: {self.key_len}',
                f'Ключ: {self.key}',
                f'Шифрованое сообщение (без пробелов): {self.crypt_message}']

    @property
    def _student(self):
        return ['Восстановите исходное сообщение зашифрованое шифом Виженера',
                f'CRC32 оригинального сообщения: {self.crc32}',
                f'Алфавит: {string.ascii_uppercase}',
                f'Длина ключа: {self.key_len}',
                f'Шифрованое сообщение (без пробелов): {self.crypt_message}']
