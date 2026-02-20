

def mult(a,b):
    return a*b

def div(a,b):
    return a/b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def pow(a,b):
    return a**b

print("bienvenue dans la calulatrice ")

while True :

    print ('_________________________________________________________________')
    print("1 : effectuer une operation ")
    print("2 : quitter laplication ")
    choix= int(input("les choix son selectionner avec des numero veuiller rentre votre choix : "))
    print ('_________________________________________________________________')


    if choix == 1 :
        opp1 = int(input("veuiller rentre le premier opperant : "))
        signe = input("veuiller rentre le signe de lopperation : ")
        opp2 = int(input("veuiller rentre le deuxiemme opperant : "))

        if signe == "+":
            print(opp1, " + ", opp2, " = ",add(opp1,opp2))

        if signe == "-":
            print(sub(opp1,opp2))

        if signe == "x" or signe == "X" or signe == "*":
            print(mult(opp1,opp2))

        if signe == "/":
            print(div(opp1, opp2))

        if signe == "**":
            print(pow(opp1,opp2))

    if choix == 2 :
        break
