import math

selectAction = input("Choose: \n1) + \n2) - \n3) * \n4) / \n5) √ \n6) ^\n")

firstValue = input("enter the first number\n")
secondValue = input("enter second number\n")

match selectAction:
    case "1":
        print(int(firstValue) + int(secondValue))
    case "2":
        print(int(firstValue) - int(secondValue))
    case "3":
        print(int(firstValue) * int(secondValue))
    case "4":
        print(int(firstValue) / int(secondValue))
    case "5":
        print(firstValue + "= ", math.sqrt(int(firstValue)), "\n" + secondValue + "= ", math.sqrt(int(secondValue)))
    case "6":
        print(math.pow(int(firstValue), int(secondValue)))
    case _:
        print("Error!")
