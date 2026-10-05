#user inputs whole positive number n, and program outputs all numbers that n can be divided with
import sys

n = int(input("Unesite pozitivan cijeli broj: "))

if type(n)!=int or n<1:
    sys.exit(-1)

print("Faktori broja",n,"su: ")

for i in range(1,n+1):
    if n%i==0:
        print(i)
    i+=1
