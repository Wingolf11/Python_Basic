import random

joueurs = ["Martin", "Roland", "Anne", "Claire", "David", "Alice", "Sonia", "Paul", "Jacques", "Rose", "Alexia", "Maria", "Thomas", "Yoann", "Guillaume", "Ada", "Grace", "Jean", "Marissa", "Alain"]

while True:
    print("---->Bienvenue dans le Générateur D'Équipes<----")
    random.shuffle(joueurs)
    Equipe_1 = joueurs[:len(joueurs)//2]
    print("->Capitaine de l'équipe 1 : " + random.choice(Equipe_1) + "  <-")
    print("->Équipe 1: ")
    for joueur in Equipe_1:
        print(joueur)
    print("<----------------------------->")
    Equipe_2 = joueurs[len(joueurs)//2 :]
    print("->Capitaine de l'équipe 2 : " + random.choice(Equipe_2) + "  <-")
    print("->Équipe 2: ")
    for joueur in Equipe_2:
        print(joueur)
    reponse = input("Choisir de nouvelles équipes ? o / n:")
    if reponse == "n":
        break