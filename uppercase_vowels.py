
sentence = "Python is fun and Python is easy to learn!"
vowels = "aeiou"
uppercase_ver = ""

for char in sentence:
    if char in vowels:
        uppercase_ver += char.upper()
    else:
        uppercase_ver += char

for letter in uppercase_ver:
    print(letter, end=" ")