import pkgutil

from .base import CryptBase
from .caesar import Caesar
from .vigenere import Viginere
from .aes import GenAES


def all_subclasses(cls):
    return list(set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)]))

algorithms = all_subclasses(CryptBase)

__all__ = [algorithms]

