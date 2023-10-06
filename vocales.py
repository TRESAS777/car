palabra = str(input("Ingrese la palabra"))
vocales = 0

for i in palabra:
    if i == "a" or i == "A":
        vocales=vocales+1 
    if i == "e" or i == "E":
        vocales=vocales+1 
    if i == "i" or i == "I":
        vocales=vocales+1 
    if i == "o" or i == "O":
        vocales=vocales+1 
    if i == "u" or i == "U":
        vocales=vocales+1 
print(vocales)