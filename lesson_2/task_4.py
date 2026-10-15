# 4. Rzut kostką — rzuć dwiema kostkami ( random.randint ), wypisz oba wyniki i sumę.

import random

cube_1 = random.randint(1,6)
cube_2 = random.randint(1,6)

print(f"Kostka 1: {cube_1}")
print(f"Kostka 2: {cube_2}")
print(f"Suma: {cube_1 + cube_2}")