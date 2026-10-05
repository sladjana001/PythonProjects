#user inputs integer n, program outputs n digits of PI

import math
import sys

n = int(input("Unesite nenegativan cijeli broj: "))

if n<0:
    print("Molimo Vas da unesete nenegativan cijeli broj.")
    sys.exit(-1)

#x = math.pi
print("Ispis PI sa",n,"decimala",f"{math.pi:.{n}f}")

num, dec = str(math.pi).split('.')
print("Ispis samo decimala (bez zaokruzivanja)",dec[0:n])