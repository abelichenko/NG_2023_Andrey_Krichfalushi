vowels = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y",]
string = input("Go print! ")
for letter in string:
    if(letter in vowels):
        print(letter)
