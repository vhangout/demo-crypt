import base64
import string

from Crypto.Cipher import AES

from algorithms import CryptBase


class GenAES(CryptBase):
    def __init__(self):
        super().__init__()
        self.alphabet = string.ascii_letters + string.digits

    def generate(self, message):
        message = message.ljust(len(message) + 16 - len(message) % 16, '.') #align message length
        super().generate(message)
        self.key = self._gen_pass(16, self.alphabet)
        cipher = AES.new(self._bytes(self.key), AES.MODE_ECB) # Electronic Codebook mode
        self.crypt_message = base64.b64encode(cipher.encrypt(self._bytes(self.message))).decode("utf-8")

    @property
    def _name(self):
        return 'Шифр AES (ECB - Electronic Codebook) частично утеряный ключ'

    @property
    def _teacher(self):
        return [self._name,
                f'Сообщение: {self.message}',
                f'CRC32: {self.crc32}',
                f'Алфавит: {self.alphabet}',
                f'Ключ: {self.key}',
                f'Шифрованое сообщение (base64): {self.crypt_message}']

    @property
    def _student(self):
        return ['Было перехвачено сообщение, его контрольная сумма и половина ключа AES (ECB - Electronic Codebook).',
                'Восстановите исходное сообщение.',
                f'CRC32 оригинального сообщения: {self.crc32}',
                f'Алфавит ключа: {self.alphabet}',
                f'Первая половина ключа (длина 16): {self.key[:13]}',
                f'Шифрованое сообщение (base64): {self.crypt_message}']