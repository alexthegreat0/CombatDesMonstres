#créé en 2023 par Alexandre Wilbur
import random 
import colorama
import time
from colorama import Fore

colorama.init(autoreset=True)
healthpoints = 20
monsterhealth = 1

while healthpoints >= 1:
    print("Vous vous trouvez dans un couloir avec une porte de sortie avec un monstre SUPER effrayant!!!\n")
    print("Vous avez", Fore.GREEN + str(healthpoints), "point(s) de vie\nLe monstre a", Fore.RED + str(monsterhealth), "point(s) de vie")
    print("Vous pouvez:\n")
    print(Fore.RED + "Combattre le monstre - 1\n")
    print(Fore.BLUE + "Contourner le monstre et aller ouvrir une autre porte - 2\n")
    fightchoice = str(input(Fore.WHITE + "Que voulez-vous faire?\n"))

    #Condition pour l'action de se battre

    if fightchoice == "1":
        print("Vous roulez les dés pour battre le monstre!!! \n")
        numberonthedice = random.randint(1,6)
        if numberonthedice <= 4:
            print("Vous avez roulé un", numberonthedice, "\n, donc vous allez perdre un nombre de points de vie équivalent au nombre de points de vie du monstre (", monsterhealth, ")")
            healthpoints = healthpoints - monsterhealth
        elif numberonthedice > 1:
            print("Vous avez roulé un", numberonthedice, "\n, donc vous avez battu le montre qui avait", monsterhealth, "points de vie")

    #Condition pour l'action de contourner

    elif fightchoice == "2":
        print("Vous contourner le monstre pour passer dans la porte. \nVous perdez 1 point de vie en consequence")
        healthpoints = healthpoints - 1
    monsterhealth = monsterhealth + 1
    if healthpoints >= 1:
        print("Vouz allez dans la prochaine salle\n\n")
    time.sleep(5)

print("Vous etes mort...")
