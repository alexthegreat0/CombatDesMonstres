#créé en 2023 par Alexandre Wilbur

#Modules

import random,colorama, time
from colorama import Fore
colorama.init(autoreset=True)

#Variables

healthpoints = 20

currentmonsterhealth, victoiresconsecutives, monsterhealth, victoires = -1, 0, 0, 0

while healthpoints >= 1:

    #Contexte:
    if victoiresconsecutives >= 3:
        monsterhealth = 10
    elif monsterhealth != currentmonsterhealth:
        monsterhealth = random.randint(1,7)
    print("\n---------\n\nVous vous trouvez dans un couloir avec une porte de sortie avec un monstre SUPER effrayant!!!\n")
    print("Vous avez", Fore.GREEN + str(healthpoints), "point(s) de vie\nLe monstre a", Fore.RED + str(monsterhealth), "point(s) de vie")

    #Actions:

    print(Fore.RED + "\nCombattre le monstre - 1", Fore.BLUE + "\nContourner le monstre et aller ouvrir une autre porte - 2",Fore.WHITE+("\nAfficher les règles du jeu - 3\nQuitter la partie - 4\n"))
    fightchoice = str(input("Que voulez-vous faire?\n"))
    print("\n---------\n")

    #Condition pour l'action de se battre
    if victoiresconsecutives >= 3:
        print(Fore.RED + "Vous faisez face à un BOSS!!!")
    if fightchoice == "1":
        print("\nVous roulez les dés pour battre le monstre!!! \n")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dicetotal = dice1 + dice2
        print("Vous avez roulé un", Fore.RED + str(dice1), "sur le premier dé, et un", Fore.RED + str(dice2), "sur le deuxième dé")
        #Condition pour une défaite

        if dicetotal <= monsterhealth:
            print("\nDonc, vous perdez de la vie équivalente à la vie du monstre (",monsterhealth,")")
            healthpoints = healthpoints - monsterhealth
            victoiresconsecutives = 0
        #Condition pour une victoire

        elif dicetotal > monsterhealth:
            victoires = victoires + 1
            victoiresconsecutives = victoiresconsecutives + 1
            print("\nDonc, vous gagnez de la vie équivalente à la vie du monstre (",monsterhealth,") points de vie\n")
            healthpoints = healthpoints + monsterhealth
        currentmonsterhealth = 0

    #Condition pour l'action de contourner

    elif fightchoice == "2":
        print("Vous contourner le monstre et perdez 1 point de vie en conséquence")
        healthpoints = healthpoints - 1
        currentmonsterhealth = 0
    #Condition pour l'action d'afficher les règles du jeu

    elif fightchoice == "3":
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire.\nDans ce cas, le niveau de vie de l'usager est augmenté de la force de ladversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l'usager est inférieure ou égale à la force de l'adversaire.\nDans ce cas, le niveau de vie de l'usager est diminué de la force de l'adversaire.\n\nLa partie se termine lorsque les points de vie de l'usager tombent sous 0.\n\nL'usager peut combattre ou éviter chaque adversaire, dans le cas de l'évitement, il y a une pénalité de 1 point de vie.")
        currentmonsterhealth = monsterhealth

    #Condition pour l'action de quitter la partie

    else:
        print("Merci et au revoir... ")
        healthpoints = 0

    if healthpoints >= 1: #s'assurer que le héro n'est pas mort
        print("Vouz allez dans la prochaine salle")

    print("\nVous avez",Fore.YELLOW + str(victoires), "victoires et", Fore.YELLOW + str(victoiresconsecutives), "victoires consécutives!!!")
    time.sleep(5) #pause pour lire le texte
print("Vous êtes mort...") #Fin du jeu quand tu ne rentres plus dans la boucle