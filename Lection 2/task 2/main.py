lst = input("Write whatever you want: ")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
tempNum = ""
accepted = []

for element in lst:
    if element in numbers:
        tempNum = tempNum + element
    else:
        if (len(tempNum) >= 2):
            accepted.append(tempNum)
        tempNum = ""

if (len(tempNum) >= 2):
    accepted.append(tempNum)

for num in accepted:
    print(num)
