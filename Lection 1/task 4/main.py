import math

selectAction = input("Choose: \n1) + \n2) - \n3) * \n4) / \n5) √ \n6) ^\n")

firstValue = float(input("enter the first number\n"))
secondValue = float(input("enter second number\n"))

match selectAction:
    case "1":
        print(firstValue + secondValue)
    case "2":
        print(firstValue - secondValue)
    case "3":
        print(firstValue * secondValue)
    case "4":
        print(firstValue / secondValue)
    case "5":
        print(firstValue, "= ", math.sqrt(firstValue), "\n" , secondValue, "= ", math.sqrt(secondValue))
    case "6":
        print(math.pow(firstValue, secondValue))
    case _:
        print("Error!")
