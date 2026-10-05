#first 10 nubmers in Fibonacci sequence

#fibonacci = list(range(10))

n = int(input("Unesite prirodan broj: "))

fibonacci = [0]*n
i = int(0)
for i  in range(n):
    if i==0:
        fibonacci[i]=0
    if i ==1:
        fibonacci[i]=1
    if i!=1 and i!=0: 
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

print(fibonacci)