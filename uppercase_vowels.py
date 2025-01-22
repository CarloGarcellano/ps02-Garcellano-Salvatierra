sentence = "Python is fun and Python is easy to learn!"


sentence = sentence.replace("a", "A")
sentence = sentence.replace("e", "E")
sentence = sentence.replace("i", "I")
sentence = sentence.replace("o", "O")
sentence = sentence.replace("u", "U")


for letter in sentence:
    print(letter, end=" ")          