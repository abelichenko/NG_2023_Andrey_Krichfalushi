import math

a = input("Choose: \n1) + \n2) - \n3) * \n4) / \n5) √ \n6) ^\n")

if (int(a) < 1 or int(a) > 6):
    print("You can not do it this way!!!")
    exit()

b = input("enter the first number\n")
c = input("enter second number\n")

if(int(a) == 1):
    print(int(b) + int(c))
if(int(a) == 2):
    print(int(b) - int(c))
if(int(a) == 3):
    print(int(b) * int(c))
if(int(a) == 4):
    print(int(b) / int(c))
if (int(a) == 5):
    print(b + "= ", math.sqrt(int(b)), "\n" + c + "= ", math.sqrt(int(c)))
if (int(a) == 6):
    print(math.pow(int(b), int(c)))