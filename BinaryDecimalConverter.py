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

else:
    bin = input("Unesite binarni broj: ")
    i = int(0)
    dec = int(0)
    while int(bin) > 0:
        dec += (int(bin)%10)*pow(2,i)
        i+=1
        bin = int(bin)//10
    print("Decimalni oblik broja je: ",dec)
