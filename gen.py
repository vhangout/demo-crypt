import math
import secrets
from pathlib import Path

from algorithms import algorithms

if __name__ == '__main__':
    lines = Path('text.txt').read_text(encoding='utf-8').split('\n')
    teacher = []
    student = []
    for idx, message in enumerate(lines):
        algo = algorithms[math.trunc(secrets.SystemRandom().random() * len(algorithms))]()
        algo.generate(message)

        print(f'-= {idx + 1} =-')
        print(algo.teacher)
        print(algo.student)

        teacher += [f'-= {idx + 1} =-', algo.teacher]
        student += [f'-= {idx + 1} =-', algo.student]

    Path('teacher.txt').write_text('\n'.join(teacher), encoding='utf-8')
    Path('student.txt').write_text('\n'.join(student), encoding='utf-8')
