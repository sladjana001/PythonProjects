#User inputs number (positive integer), program outputs first prime number that comes after the input that is prime number
import math

def prime(n: int) -> int:
    if n <= 1: #excluding 1 and all non-positive numbers
        return -1
    if n==2: #2 is the only prime number that is even
        return 1 
    if n%2==0: #excluding all even numbers
        return -1
    for i in range (3,int(math.isqrt(n))+1,2):
        if n % i == 0:                    
            return -1
    
    return 1        #it is a prime number

x = input("Input positive integer: ") #provjera funkcije
x = int(x)
prost = prime(x)
if prost == 1:
    print("Unijeli ste prost broj")
else:
    print("Uneseni broj nije prost")

x=x+1
while prime(x) == -1:
    if(prime(x)==1):
        break
    x+=1

print("Sledeci prost broj je " , x)
