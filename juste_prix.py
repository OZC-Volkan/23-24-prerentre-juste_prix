# Tirage au hasard d'un prix entre 1 et 10
import random
cible = random.randint(1,10)
print(cible)

essai = None
for i in range(1,6):
    # Choix du prix du joueur
    try:
        essai = int(input(f"Essai n°{i} -- Votre essai: "))
    except:
        print("La valeur est incorrect...")
        continue  # Redémarre à l'itération suivante
    # Message "Bravo" si le prix est trouvé
    if essai == cible:
        print("Bravo!!!")
        break
    # Message "Pas assez" si le prix est trop bas
    elif essai < cible:
        print("Pas assez!!!")

    # Message "Trop eleve" si le prix est trop haut
    else :
        print("Trop eleve")

# Message "Perdu" au bout de 5 essais
if cible != essai:
    print("Perdu...")

# Fin au bout de 5 essais OU si le prix est trouvé