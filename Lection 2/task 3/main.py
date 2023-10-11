num = int(input("You num: "))
i = 1
numsList = []
simpleNums = []

while num >= i:
    localStr = str(i) + " | "
    denominator = 1
    numberOfDenominator = 0
    while denominator <= i:
        string = str(i / denominator) + " "
        if ".0 " in string:
            localStr = localStr + " " + str(denominator)
            numberOfDenominator = numberOfDenominator + 1
        denominator = denominator + 1
    if numberOfDenominator <= 2:
        simpleNums.append(i)
    numsList.append(localStr)
    i = i + 1

for element in numsList:
    print(element)
print(simpleNums)    