"""
    python sample.py | python recomm.py
"""

import random

def main():
    for _ in range(10):
        pref = [
            random.random(),
            random.random(),
            random.random(),
        ]

        print(', '.join(str(p) for p in pref))


if __name__ == '__main__':
    main()


