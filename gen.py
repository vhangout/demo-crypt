import math
import secrets
from pathlib import Path

from algorithms import algorithms

if __name__ == '__main__':
    lines = Path('text.txt').read_text(encoding='utf-8').split('\n')
    for message in lines:
        algo = algorithms[math.trunc(secrets.SystemRandom().random() * len(algorithms))](message)
        algo.crypt()
        print(algo)
