#Luhn Algorithm
#How credit cards use checksum?


print('Unesite 11 cifara/broj kartice: ')
numbers = [int(x) for x in input().split()]
print(numbers)


s = int(0)
for i in range (11):
    if i%2==1:    
        numbers[i] = numbers[i]*2
        if numbers[i] >= 10:
            numbers[i] = numbers[i]-9
    s += numbers[i]

print(numbers)
print(s)
if s%10==0:
    print("Kartica je validna")
else:
    print("Kartica nije validna")
