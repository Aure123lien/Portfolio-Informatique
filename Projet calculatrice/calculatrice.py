#Les fonctions mathématiques

def addition(a, b):
    #Retourne la somme des deux nombres
    return a + b

def soustraction(a, b):
    #Retourne la différence des deux nombres
    return a - b

def multiplication(a, b):
    #Retourne le produit des deux nombres
    return a * b

def division(a, b):
    #Vérifie si la personne essaie de diviser par zéro
    if b == 0:
        return "Erreur : division par zéro"
    #Retourne le résultat de la division
    return a / b

# Le programme

# La fonction main() contient toute la logique du programme
def main():

    # Le message qui est affiché au lancement du programme
    print("Calculatrice Python")
    print("Opérations disponibles : +  -  *  /")

    # Boucle infinie pour permettre à la personne d’enchaîner plusieurs calculs sans relancer le programme
    while True:

        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le second nombre : "))
        except ValueError:
            print("Veuillez entrer uniquement des nombres valides.")
            continue

        # On demande à la personne de choisir une opération qu'il souhaite effectuer
        op = input("Entrez l'opération (+, -, *, /) : ")

        if op == "+":
            result = addition(a, b)
        elif op == "-":
            result = soustraction(a, b)
        elif op == "*":
            result = multiplication(a, b)
        elif op == "/":
            result = division(a, b)
        else:
            print("Opération invalide.")
            continue  # On recommence la boucle.

        print(f"Résultat : {result}")

        choix = input("Voulez-vous faire un autre calcul ? (oui/non) : ").lower()

        if choix != "oui":
            print("Merci d'avoir utilisé la calculatrice !")
            break  # Sortie de boucle donc la fin du programme.


if __name__ == "__main__":
    main()
