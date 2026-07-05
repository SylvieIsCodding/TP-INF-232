import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from config_seed import GRAINE

CHEMIN_DATASET = "dataset.csv"

try: 
    df = pd.read_csv(CHEMIN_DATASET)
except FileNotFoundError:
    raise(
        f"Erreur : le fichier '{CHEMIN_DATASET}' est introuvable. "
        "Verifie qu'il est bien dans le meme dossier que ce script "
        "(genere par 01_generation_donnees.py)."
    )

print("Apercu des donnees chargees:")
print(df.head())
print(f"\nNombre d'eleves : {len(df)}")

colonnes_features = ["note_evaluation", "heures_travail"]

for col in colonnes_features:
    if col not in df.columns:
        raise SystemExit(
            f"Erreur : la colonne '{col}' est absente du dataset. "
            "Verifie le nom exact des colonnes dans dataset.csv" 
        )

X = df[colonnes_features].copy()

scaler = StandardScaler()
X_standardise = scaler.fit_transform(X)

k_min, k_max = 2, 8
inerties = []
scores_silhouette = []
valeurs_k = range(k_min, k_max + 1)

for k in valeurs_k:
    modele_temp = KMeans(n_clusters=k, random_state=GRAINE, n_init=10)
    labels_temp = modele_temp.fit_predict(X_standardise)
    inerties.append(modele_temp.inertia_)
    scores_silhouette.append(silhouette_score(X_standardise, labels_temp))

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(list(valeurs_k), inerties, marker="o")
plt.xlabel("Nombre de groupes (k)")
plt.ylabel("Inertie")
plt.title("Methode du coude")

plt.subplot(1, 2, 1)
plt.plot(list(valeurs_k), scores_silhouette, marker="o", color="orange")
plt.xlabel("Nombre de groupe (k)")
plt.ylabel("Score de silhouette")
plt.title("Score de silhouette selon k")

plt.tight_layout()
plt.savefig("choix_nombre_groupes.png")
plt.close()
print("\nGraphique du choix de k enregistre : choix_nombre_groupes.png")

k_optimal = list(valeurs_k)[int(np.argmax(scores_silhouette))]
print(f"\nNombre de groupes retenu (meilleur score de silhouette) : {k_optimal}")

modele_final = KMeans(n_clusters=k_optimal, random_state=GRAINE, n_init=10)
df["cluster"] = modele_final.fit_predict(X_standardise)

centres_standardise = modele_final.cluster_centers_
centres_originaux = scaler.inverse_transform(centres_standardise)

df_centres = pd.DataFrame(centres_originaux, columns=colonnes_features)
df_centres.index.name = "cluster"

print("\nDescription des centres des groupes (valeurs moyennes):")
print(df_centres.round(2))

print("\nEffectif de chaque groupe :")
print(df["cluster"].value_counts().sort_index())

if "orientation" in df.columns:
    print("\nRepartition orientation / cluster (a titre indicatif):")
    print(pd.crosstab(df["cluster"], df["orientation"]))

df.to_csv("dataset_avec_clusters.csv", index=False, encoding="utf-8")
print("\nFichier exporte : dataset_avec_clusters.csv")    
    