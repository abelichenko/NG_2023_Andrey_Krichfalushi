def actionSelection(): #Please enter the user's number for him to select an action
    selectedNum = int(input("Choose what you need:\n"
              "1) Convert from Celsius to Fahrenheit"
              "\n2) Convert from Fahrenheit to Celsius\n"))
    if(selectedNum == 1 or selectedNum == 2): 
        return selectedNum
    else:
        print("invalid value")
        main()

def main():
    selectedNum = actionSelection()
    
    value = int(input("Enter the number of degrees: "))
    
    if(selectedNum == 1):
        print(value, "°C =", value * 9 / 5 + 32, "°F")
    if(selectedNum == 2):
        print(value, "°F =", (value - 32) * 5/9, "°C")
        
main()
