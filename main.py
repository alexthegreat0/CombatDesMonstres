#créé en 2023 par Alexandre Wilbur

#Modules

import random,colorama, time
from colorama import Fore
colorama.init(autoreset=True)

#Variables

healthpoints = 20
monsterhealth = 1
victoires = 0

while healthpoints >= 1:

    #Contexte:

    print("\n---------\n\nVous vous trouvez dans un couloir avec une porte de sortie avec un monstre SUPER effrayant!!!\n")
    print("Vous avez", Fore.GREEN + str(healthpoints), "point(s) de vie\nLe monstre a", Fore.RED + str(monsterhealth), "point(s) de vie")

    #Actions:

    print(Fore.RED + "\nCombattre le monstre - 1", Fore.BLUE + "\nContourner le monstre et aller ouvrir une autre porte - 2\n")
    fightchoice = str(input(Fore.WHITE + "Que voulez-vous faire?\n"))
    print("\n---------\n")
    #Condition pour l'action de se battre

    if fightchoice == "1":
        print("Vous roulez les dés pour battre le monstre!!! \n")
        numberonthedice = random.randint(1,6)

        #Condition pour une défaite

        if numberonthedice <= 4:
            print("Vous avez roulé un", Fore.RED + str(numberonthedice), "\nDonc, vous perdez de la vie équivalente à la vie du monstre (", monsterhealth, ")")
            healthpoints = healthpoints - monsterhealth
        
        #Condition pour une victoire

        elif numberonthedice > 1:
            victoires = victoires + 1
            print("Vous avez roulé un", Fore.GREEN + str(numberonthedice), "\nDonc, vous avez battu le montre qui avait", monsterhealth, "points de vie\n")

    #Condition pour l'action de contourner

    elif fightchoice == "2":
        print("Vous contourner le monstre et perdez 1 point de vie en consequence")
        healthpoints = healthpoints - 1
    monsterhealth = monsterhealth + 1 #Le prochain monstre sera plus puissant

    if healthpoints >= 1: #s'assurer que le héro n'est pas mort
        print("Vouz allez dans la prochaine salle")

    print(Fore.YELLOW + "\nVous avez %d victoires!!!"%victoires)
    time.sleep(5) #pause pour lire le texte
print("Vous êtes mort...") #Fin du jeu quand tu ne rentres plus dans la boucle