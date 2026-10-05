#convert to binary from decimal, and vice versa

import sys


print("BD-Binary to Decimal, DB-Decimal to Binary. Unesite BD ili DB: ")
s=input("BD ili DB?")

if s!='DB' and s!='BD':
    sys.exit(-1)


if s == 'DB': 
    n = int(input("Unesite cijeli broj: "))
    if n==0:
        print(0)
    bin=""
    while n > 0:
        bin += str(n%2)
        n//=2  

bin=str(bin)
print("Binarni ekvivalent je: ",bin[::-1])