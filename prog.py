# Recuperation d'un nombre positif impair
def getNumber(message : str) -> int :
    
    try:
        number = int(input(message))
        if number < 3:
            return getNumber("\nLe nombre doit être supérieur ou égal à 3, veuillez entrer une valeur correcte : ")
        if number % 2 == 0:
            return getNumber("\nLe nombre doit être impair, veuillez entrer une valeur correcte : ")
        return number
    
    except:
        return getNumber("\nError : Veuillez entrer un entier : ")

#Creation d'une matrice de taille n*n
def startMatrice(number : int):
    square = []
    for i in range(number):
        line = [0] * number
        square.append(line)

    return square


# Programme principal
print("\n|--- Veuiller entrer un nombre positif impair qui representera la taille d'une n d'une matrice et nous vous retournerons le carré magique correspondant ---|\n")

number = getNumber("\tNombre : ")

square = startMatrice(number)

print(square)