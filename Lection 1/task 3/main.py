a = input("Choose what you need:\n"
          "1) Convert from Celsius to Fahrenheit"
          "\n2) Convert from Fahrenheit to Celsius\n")

b = input("Enter the number of degrees: ")

if(int(a) == 1):
    print(b + "°C =", int(b) * 9 / 5 + 32, "°F")
if(int(a) == 2):
    print(b + "°F =", (int(b) - 32) * 5/9, "°C")