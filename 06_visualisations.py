"""
=========================================================
INF232 - TP Analyse des données
Fichier : 06_visualisations.py

Auteur : EPOLLE NJIMAN MARIETTE ERICKA (23V2417)

Rôle :
    - Générer toutes les visualisations du projet
    - Sauvegarder les figures dans le dossier figures/
=========================================================
"""

import os
import pandas as pd

import matplotlib
matplotlib.use("Agg")  # IMPORTANT : pas d'interface graphique

import matplotlib.pyplot as plt
import seaborn as sns


# -------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

os.makedirs("figures", exist_ok=True)


# -------------------------------------------------------
# CHARGEMENT DES DONNÉES
# -------------------------------------------------------

def load_data(path="data/eleves_theme_D.csv"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    return pd.read_csv(path)


# -------------------------------------------------------
# Q1 : Distribution des notes
# -------------------------------------------------------

def graphique_q1(df):

    plt.figure()

    sns.histplot(df["note_evaluation"], bins="auto", kde=True)

    plt.title("Distribution des notes")
    plt.xlabel("Note")
    plt.ylabel("Effectif")

    plt.tight_layout()
    plt.savefig("figures/q1_histogramme.png")
    plt.close()

    plt.figure()

    sns.boxplot(x=df["note_evaluation"])

    plt.title("Boîte à moustaches des notes")

    plt.tight_layout()
    plt.savefig("figures/q1_boxplot.png")
    plt.close()


# -------------------------------------------------------
# Q2 : Travail vs note
# -------------------------------------------------------

def graphique_q2(df):

    plt.figure()

    sns.regplot(
        data=df,
        x="heures_travail",
        y="note_evaluation",
        scatter_kws={"s": 60}
    )

    plt.title("Relation entre heures de travail et note")
    plt.xlabel("Heures de travail")
    plt.ylabel("Note")

    plt.tight_layout()
    plt.savefig("figures/q2_regression.png")
    plt.close()


# -------------------------------------------------------
# Q3 : Clustering
# -------------------------------------------------------

def graphique_q3(df, labels):

    if labels is None:
        return

    if len(labels) != len(df):
        raise ValueError("Labels incompatibles avec le dataset")

    plt.figure()

    sns.scatterplot(
        x=df["heures_travail"],
        y=df["note_evaluation"],
        hue=labels,
        palette="viridis",
        legend="full"
    )

    plt.title("Clusters d'élèves")
    plt.xlabel("Heures de travail")
    plt.ylabel("Note")

    plt.tight_layout()
    plt.savefig("figures/q3_clusters.png")
    plt.close()


# -------------------------------------------------------
# Q4 : Matrice de confusion
# -------------------------------------------------------

def graphique_q4(cm):

    if cm is None:
        return

    plt.figure()

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.title("Matrice de confusion")
    plt.xlabel("Prédit")
    plt.ylabel("Réel")

    plt.tight_layout()
    plt.savefig("figures/q4_confusion_matrix.png")
    plt.close()


# -------------------------------------------------------
# PIPELINE GLOBAL
# -------------------------------------------------------

def generer_toutes_les_figures(df, labels=None, cm=None):

    graphique_q1(df)
    graphique_q2(df)

    graphique_q3(df, labels)
    graphique_q4(cm)


# -------------------------------------------------------
# TEST
# -------------------------------------------------------

if __name__ == "__main__":

    print("Chargement des données...")

    df = load_data()

    print("Création des graphiques...")

    generer_toutes_les_figures(df)

    print("Terminé ! Vérifie le dossier 'figures/'")