vowels = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y", " ", "-", ".", ",", "`", ":", "(", ")", ";", "[",
          "]", "{", "}"]
string = input("Go print! ")
output = ""

for letter in string:
    if letter in vowels:
        output = output + letter

print(output)   