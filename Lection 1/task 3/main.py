selectedNum = input("Choose what you need:\n"
          "1) Convert from Celsius to Fahrenheit"
          "\n2) Convert from Fahrenheit to Celsius\n")

changeAction = int(selectedNum)
value = input("Enter the number of degrees: ")

if(changeAction == 1):
    print(value + "°C =", int(value) * 9 / 5 + 32, "°F")
if(changeAction == 2):
    print(value + "°F =", (int(value) - 32) * 5/9, "°C")
