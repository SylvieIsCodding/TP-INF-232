import random
import os
import csv
#import pandas as pd
from config_seed import GRAINE

#print("Graine du groupe :", GRAINE)

def generer_dataset(graine: int, n: int = 200):
    generateur = random.Random(graine)  # générateur LOCAL, isolé
    
    donnees = []
    for i in range(n):
        #    heures_travail (générée en premier) 
        # Heures de travail personnel par semaine, entre 0 et 25h
        heures_travail = generateur.gauss(10, 5)
        heures_travail = max(0, min(25, heures_travail))
        
        #   note_evaluation (corrélée à heures_travail + bruit) 
        # Relation linéaire plausible : note de base 8, +0.5 par heure de travail, + bruit
        bruit_note = generateur.gauss(0, 2.5)
        note = 8 + 0.5 * heures_travail + bruit_note
        note = round(max(0, min(20, note)), 2)
        heures_travail = round(heures_travail, 2)
        
        #   orientation (aléatoir controlé) 
        # Score combinant note (poids fort) et heures (poids faible), + bruit indépendant
        score = 0.7 * note + 0.1 * heures_travail + generateur.gauss(0, 3)
        # Seuil calé empiriquement (score moyen ~10.2) pour un partage réaliste
        orientation = "scientifique" if score >= 10.2 else "litteraire"
        
        donnees.append({
            "id_eleve": f"E{i+1:03d}",
            "note_evaluation": note,
            "heures_travail": heures_travail,
            "orientation": orientation
        })
    
    return donnees


def nettoyer_donnees(donnees):
    donnees_propres = []
    anomalies = 0

    for ligne in donnees:
        note = ligne["note_evaluation"]
        heures = ligne["heures_travail"]

        if note < 0 or note > 20 or heures < 0 or heures > 25:
            anomalies += 1

        note = min(max(note, 0), 20)
        heures = min(max(heures, 0), 25)

        note = round(note, 2)
        heures = round(heures, 2)

        donnees_propres.append({
            "id_eleve": ligne["id_eleve"],
            "note_evaluation": note,
            "heures_travail": heures,
            "orientation": ligne["orientation"]
        })

    print(f"Contrôle des valeurs terminé : {anomalies} anomalie(s) corrigée(s) sur {len(donnees)} lignes.")
    return donnees_propres


def sauvegarder_csv(donnees, chemin_fichier):
    data = os.path.dirname(chemin_fichier)
    if data and not os.path.exists(data):
        os.makedirs(data)

    with open(chemin_fichier, mode="w", newline="", encoding="utf-8") as fichier:
        colonnes = ["id_eleve", "note_evaluation", "heures_travail", "orientation"]
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(donnees)

    print(f"Fichier enregistré : {chemin_fichier}")



eleves_theme_D= generer_dataset(graine=GRAINE)
#print("Exemple de données générées :", eleves_theme_D[:5])  # Affiche les 5 premières entrées

"""
with open("eleves_theme_D.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id_eleve", "note_evaluation", "heures_travail", "orientation"])
        writer.writeheader()
        writer.writerows(eleves_theme_D)

print("\nFichier exporté : eleves_theme_D.csv")
"""

"""
# Chargement des données
df1 = pd.read_csv('eleves_theme_D.csv')
df2 = pd.read_csv('eleves_theme_D1.csv')

# Vérification d'égalité stricte
sont_identiques = df1.equals(df2)
print(f"Les tableaux sont identiques : {sont_identiques}")
"""


if __name__ == "__main__":
    #graine = calculer_graine(NOM_CHEF)
    #print(f"Graine du groupe : {graine}")

    donnees_finales = nettoyer_donnees(eleves_theme_D)

    sauvegarder_csv(donnees_finales, "data/eleves_theme_D.csv")
    #afficher_extrait(donnees_finales, 10)