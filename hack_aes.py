'''
Было перехвачено сообщение, его контрольная сумма и половина ключа AES (ECB - Electronic Codebook).
Восстановите исходное сообщение.
CRC32 оригинального сообщения: 0x6f839f70
Алфавит ключа: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
Первая половина ключа (длина 16): BaZiFMmt
Шифрованое сообщение (base64): 3IPdVNbxzEe0RJpPFHsr8EvIUoUB69IoAquGVnxclIs=
'''

import base64
import itertools
import string
import zlib
import time

from Crypto.Cipher import AES

message = base64.b64decode('sf3PzkIQovvm2xO12gUlDzQkYyfNPo4ted0v6N9tq/g=')
crc32 = 0x3ef72340
alphabet = string.ascii_letters + string.digits
base_key = b'kMMLJGDRnJ8MT'


def part_generator():
    for guess in itertools.product(alphabet, repeat=16 - len(base_key)):
        yield bytearray(''.join(guess), encoding='utf-8')


counter = 0
start_time = time.time()
for part in part_generator():
    key = base_key + part
    decipher = AES.new(key, AES.MODE_ECB)
    msg = decipher.decrypt(message)
    if zlib.crc32(msg) == crc32:
        print(key)
        print(msg)
        print('finished at {:4.3f}', time.time() - start_time)
        break

    if counter % 1e6 == 0:
        print(counter)
    counter += 1
print('Ended')
