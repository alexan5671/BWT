string = input("Inserisci una stringa: ")
string += "$"
print(string)

stringInvert = []
for i in range(len(string)):
    stringInvert.append(string[i:] + string[:i])
    
