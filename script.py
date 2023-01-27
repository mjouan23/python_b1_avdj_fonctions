# Exo 1
def helloWorld():
    return "Bonjour tout le monde"

print(helloWorld())

# Exo 2
def helloYou(firstname):
    print(f"Bonjour {firstname}")
helloYou("Steve")

# Exo 3
def average(number1, number2):
    return (number1 + number2)/2

print(average(15, 18))

# Exo 4
def my_split(strsplit, charsplit=" "):
    list_split = []; word = ""
    for letter in strsplit:
        if letter == charsplit:
            list_split.append(word)
            word = ""
        else:
            word = word + letter
    list_split.append(word)
        
    return list_split

print(my_split("Bonjour tout le monde"))

# Exo 5
def my_calcul(operation, *args):
    if operation == "addition":
        result = 0
        for number in args:
            result += number
        
        return result
    elif operation == "soustraction":
        result = args[0]
        for number in args[1:]:
            result -= number
    
        return result

print(my_calcul("addition", 5, 6, 7, 4, 10))
print(my_calcul("soustraction", 40, 6, 7, 4, 10))

# Exo 6
def person(**kwargs):
    result = ""
    for i, j in kwargs.items():
        result += i + " : "+ j +" | "
    print(result[:-2])

person(nom="Amadou", prenom="Camara", enseignant="REACT")
