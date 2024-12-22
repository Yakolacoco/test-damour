import random

def main():
    print("Test d'amour")

    while True:
        nom1 = input("Entrez le 1er nom de la personne: ")
        nom2 = input("Entrez le 2ème nom de la personne: ")

        amour_score = random.randint(1, 100)

        print(f"Le 1er nom est : {nom1}")
        print(f"Le 2ème nom est : {nom2}")
        print(f"Le pourcentage d'amour entre {nom1} et {nom2} est de {amour_score}% ! 💖")

        print("Voulez-vous recommencer le test d'amour ? 'yes' ou 'no'")
        user_input = input("> ")

        if user_input == "no":
            break
main()
