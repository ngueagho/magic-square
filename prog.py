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

#Génération des nombres à utiliser
def listOfNumber(number : int) -> list : 

    myList = []
    for i in range(number*number):
        myList.append((i+1))

    return myList

#Creation d'une matrice de taille n*n
def startMatrice(number : int) -> list : 

    square = []
    for i in range(number):
        line = [0] * number
        square.append(line)

    return square

#Affichage de la matrice
def printMatrice(matrice : list) -> None :

    print("\nCarré magique : \n")
    for elt in matrice:
        print("\t",elt)

#Deplacement vers la diagonale
def moveToDiag(matrice : list, pos : int, dataSet : list) -> list :

    try:

        if len(dataSet) > 0:
            # Cas de base
            if matrice[pos[0]][pos[1]] == 0:
                matrice[pos[0]][pos[1]] = dataSet[0]
                dataSet.remove(dataSet[0])

                return [matrice, pos]

            else:
                pos[0] -= 1
                pos[1] += 1
                
                if pos[0] >= 0 and pos[1] <= len(matrice[0]): 
                    if matrice[pos[0]][pos[1]] != 0:
                        pos[0] += 1
                        pos[1] -= 1
                        return [matrice, pos]

                    matrice[pos[0]][pos[1]] = dataSet[0]
                    dataSet.remove(dataSet[0])
                    return moveToDiag(matrice, pos, dataSet)
                
                pos[0] += 1
                pos[1] -= 1
                
                return [matrice, pos]

        return [matrice, pos]
    
    except:
        pos[0] += 1
        pos[1] -= 1
        return [matrice, pos]

#Deplacement en L
def moveToL(matrice : list, pos : int, dataSet : list) -> list :

    if pos[0] != 0: #Rassurons nous premièrement que nous somme sur la première ligne
        return [matrice, pos] #si non, on essaie une autre methode
    
    else:
        if matrice[len(matrice)-1][pos[1]+1] != 0 : #Testons la fin du L
            return [matrice, pos] #Si c'est déjà occupé, on sort
        else:
            matrice[len(matrice)-1][pos[1]+1] = dataSet[0]
            dataSet.remove(dataSet[0])
            pos[0] = len(matrice)-1
            pos[1] = pos[1]+1
            return [matrice, pos]    
    
#Deplacement en L couchée
def moveToLCouchee(matrice : list, pos : int, dataSet : list) -> list :

    if matrice[pos[0] - 1][0] != 0 :
        return [matrice, pos]
    
    else:
        matrice[pos[0]-1][0] = dataSet[0]
        dataSet.remove(dataSet[0])
        pos[0] = pos[0] - 1
        pos[1] = 0
        return [matrice, pos]





# Programme principal
print("\n|--- Veuiller entrer un nombre positif impair qui representera la taille d'une n d'une matrice et nous vous retournerons le carré magique correspondant ---|\n")

number = getNumber("\tNombre : ") # Recuperation de la taille de la matrice

dataSet = listOfNumber(number) # Construction des nombres qui seront dans mon carré magique

square = startMatrice(number) # Fabrication du carré de base

pos = [0] # Position de depart (juste la ligne)

pos.append(round((len(square[0]) // 2))) # Position de depart (ajout de la colonne)

square, pos = moveToDiag(square, pos, dataSet)

square, pos = moveToDiag(square, pos, dataSet)

square, pos = moveToL(square, pos, dataSet)

square, pos = moveToDiag(square, pos, dataSet)

square, pos = moveToLCouchee(square, pos, dataSet)

square, pos = moveToDiag(square, pos, dataSet)

printMatrice(square)

print("Pos : ",pos)
print("DataSet restant : ", dataSet)
