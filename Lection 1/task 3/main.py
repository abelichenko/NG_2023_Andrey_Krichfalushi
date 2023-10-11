selectedNum = int(input("Choose what you need:\n"
          "1) Convert from Celsius to Fahrenheit"
          "\n2) Convert from Fahrenheit to Celsius\n"))

value = int(input("Enter the number of degrees: "))
    
match selectedNum:
    case 1:
        print(value, "°C =", value * 9 / 5 + 32, "°F")
    case 2:
        print(value, "°F =", (value - 32) * 5/9, "°C")
    case _:    
        print("Wrong choice of action. Can be 1 or 2.")
