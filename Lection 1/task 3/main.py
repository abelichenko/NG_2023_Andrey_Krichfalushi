selectedNum = int(input("Choose what you need:\n"
          "1) Convert from Celsius to Fahrenheit"
          "\n2) Convert from Fahrenheit to Celsius\n"))
if(selectedNum != 1 and selectedNum != 2): 
    print("invalid value")
    exit()

value = int(input("Enter the number of degrees: "))

if(selectedNum == 1):
    print(value, "°C =", value * 9 / 5 + 32, "°F")
if(selectedNum == 2):
    print(value, "°F =", (value - 32) * 5/9, "°C")
    
