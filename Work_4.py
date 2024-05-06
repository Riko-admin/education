inputText = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
with open("./zapret.txt", "r", ) as myFile:
    words = myFile.read().split(" ")
for word in words:
    inputText = inputText.lower().replace(word, "*" * len(word))
inputText = list(inputText)
inputText = str.join('', inputText)
print(inputText)
