
sentence = "Python is fun and Python is easy to learn!"
vowels = "aeiou"
uppercasever = ""

for char in sentence:
    if char in vowels:
        uppercasever += char.upper()
    else:
        uppercasever += char

for letter in uppercasever:
    print(letter, end=" ")