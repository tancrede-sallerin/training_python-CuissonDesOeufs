import time


def temps_cuisson_oeufs(temps):
    d = temps
    min = d // 60  # division entière (pas de virgules)
    sec = d - min * 60

    for i in range(temps // 10):
        print(f"Temps restant : {min:02d}:{sec:02d}", end="", flush=True)

        if sec != 0:
            sec -= 10
        else:
            min -= 1
            sec = 50

        for a in range(10):
            time.sleep(1)
            print(".", end="", flush=True) # afficher 1 point toutes les secondes sur la même ligne

        print()


# choix
cuisson_oeufs = input("""
- Oeufs à la coque : 3 minutes
- Oeufs mollets : 6 minutes
- Oeufs durs : 9 minutes

Que voulez vous choisir ? #rentrez# 1, 2 ou 3 selon votre choix:

""")

if cuisson_oeufs == '1': temps_cuisson_oeufs(3*60)  # temps en seconde pour la
if cuisson_oeufs == '2': temps_cuisson_oeufs(6*60)
if cuisson_oeufs == '3': temps_cuisson_oeufs(9*60)


# fin
print()
print("Cuisson terminée")