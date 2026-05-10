import time

def mesurer_exposition(duree_secondes):
    print("début de la mesure d'exposition")

    for secondes in range(1, duree_secondes +1):
        print(f"expositions encours: {secondes} s")
        time.sleep(1)

    print("FIN DE LA MESURE")
