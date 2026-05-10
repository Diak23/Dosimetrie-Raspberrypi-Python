import random

def lecture_capteur():
    valeur = random.uniform(0.1, 5.0)

    print(f"Valeur du champ électromagnétique : {valeur:.2f} V/m")

    return valeur
