# MY FIRST PYTHON PROJECT
    # This is simple calculator
        # User inputs two numbers and operator
        # Program outputs result

print("Enter two numbers: ")
x=float(input("Unesite prvi broj: "))
y=float(input("Unesite drugi broj: "))
print("Enter an operation +,-,*,/: ")
o=input()
match o:
    case '+': print("Result: ",x+y)
    case '-': print("Result: ",x-y)
    case '*': print("Result: ",x*y)
    case '/':
        if y==0:
            print('Error! Dividing by 0 is undefined!')
        else:
            print("Result: ",x/y)
    case _:print("Please enter one of the suggested operations.")    

