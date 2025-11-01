# labpy03
from random import random

n = int(input("Masukkan nilai N: "))
count = 0
i = 1

while count < n:
    a = random()
    if a < 0.5:
        print(f"data ke: {i} => {a}")
        count += 1
        i += 1

print("Selesai")
