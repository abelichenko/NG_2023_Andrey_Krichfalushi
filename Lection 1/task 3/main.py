selectedNum = input("Choose what you need:\n"
          "1) Convert from Celsius to Fahrenheit"
          "\n2) Convert from Fahrenheit to Celsius\n")

value = input("Enter the number of degrees: ")

if(int(selectedNum) == 1):
    print(b + "°C =", int(value) * 9 / 5 + 32, "°F")
if(int(selectedNum) == 2):
    print(b + "°F =", (int(value) - 32) * 5/9, "°C")
