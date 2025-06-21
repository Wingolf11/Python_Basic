import csv
import tkinter

from tkinter.filedialog import askopenfile
from collections import namedtuple

Tache = namedtuple("Tache", ["titre", "duree", "prerequis"])

def lire_taches(projet):
    taches = {}
    for rang in csv.reader(open(projet)):
        numero = int(rang[0])
        titre = rang[1]
        duree = float(rang[2])
        prerequis = set(map(int, rang[3].split()))
        taches[numero] = Tache(titre, duree, prerequis)
    return(taches)

def ordre_taches(taches):
    incomplet = set(taches)
    complet = set()
    jours_debut = {}
    while incomplet:
        for num_tache in incomplet:
            tache = taches[num_tache]
            if  tache.prerequis.issubset(complet):
                jours_debut_plustot = 0
                for num_prereq in tache.prerequis:
                    jour_fin_prerequis = jours_debut[num_prereq] + taches[num_prereq].duree
                    if  jour_fin_prerequis > jours_debut_plustot:
                        jours_debut_plustot = jour_fin_prerequis
                jours_debut[num_tache] =jours_debut_plustot
                incomplet.remove(num_tache)
                complet.add(num_tache)
                break
    return  jours_debut

def charte_graphe(taches, canvas, rangee_hauteur = 40, titre_largeur = 450, ligne_hauteur = 40, jour_largeur = 25, barre_hauteur = 20, titre_indent = 20, typo_taille = 16):
    hauteur = canvas["height"]
    largeur = canvas["width"]
    semaine_largeur = 5 * jour_largeur
    canvas.create_line(0, rangee_hauteur, largeur, ligne_hauteur, fill = "grey")
    for numero_semaine in range(5):
        x = titre_largeur + numero_semaine * semaine_largeur
        canvas.create_line(x, 0, x, hauteur, fill = "grey")
        canvas.create_text(x + semaine_largeur / 2, rangee_hauteur / 2, text = f"Semaine {numero_semaine + 1}", font = ("Helvetica", typo_taille, "bold"))
    jours_debut = ordre_taches(taches)
    y = rangee_hauteur
    for num_tache in jours_debut:
        tache = taches[num_tache]
        canvas.create_text(titre_indent, y + rangee_hauteur / 2, text = tache.titre, anchor = tkinter.W, font = ("Helvetica", typo_taille))
        barre_x = titre_largeur + jours_debut[num_tache] * jour_largeur
        barre_y = y + (rangee_hauteur - barre_hauteur) / 2
        barre_largeur = tache.duree * jour_largeur
        canvas.create_rectangle(barre_x, barre_y, barre_x + barre_largeur, barre_y + barre_hauteur, fill = "red")
        y += rangee_hauteur

        
def ouvrir_projet():
    nomfichier = askopenfile(title = "ouvrir un projet", initialdir = ".", filetypes = [("CSV Document", "*.csv")])
    taches = lire_taches(nomfichier.name)
    charte_graphe(taches, canvas)



racine = tkinter.Tk()
racine.title("Planificateur de projet")
racine.resizable(width = False, height = False)
bouton_cadre = tkinter.Frame(racine, padx = 5, pady = 5)
bouton_cadre.pack(side = "top", fill = "x")
bouton_ouvrir = tkinter.Button(bouton_cadre, text = "Ouvrir un projet ...", command = ouvrir_projet)
bouton_ouvrir.pack(side = "left")
canvas = tkinter.Canvas(racine, width = 1150, height = 400, bg = "white")
canvas.pack(side = "bottom")
tkinter.mainloop()






#Test
#resultat = lire_taches('projet.csv')
#print(resultat)
#resultat_2 = ordre_taches(resultat)
#print('\n')
#print("resultat 2: ")
#print(resultat_2)