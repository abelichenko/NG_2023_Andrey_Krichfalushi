lst = input("Write whatever you want: ")
archive = []
blackList = []

for element in lst:
    if element not in archive:
        archive.append(element)
    elif element not in blackList:
        blackList.append(element)

for element in blackList:
    if element in archive:
        archive.remove(element)

for element in archive:
    print(element)