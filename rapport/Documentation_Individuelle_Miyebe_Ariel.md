# Documentation Individuelle - Miyebe Ariel Fortune Napoléon

**Nom Prénom:** Miyebe Ariel Fortune Napoléon
**Matricule:** 24G2895
**Rôle dans le groupe:** Tests et Exécution Globale du Projet

## 1. Introduction

Cette documentation individuelle détaille ma contribution au projet INF232, conformément aux exigences du Cahier des Charges [1]. Mon rôle principal a été de garantir la robustesse et la fonctionnalité de l'application développée par le groupe, en mettant en place un script de tests et d'exécution (`tests_execution.py`), en vérifiant la cohérence des sorties et en documentant les procédures. J'ai également contribué à la finalisation du fichier `README.md` du projet.

## 2. Fichier(s) de code réalisé(s) et fonction(s) principales

J'ai développé le script `tests_execution.py`, dont la fonction principale est d'orchestrer l'exécution séquentielle de tous les scripts d'analyse du projet, de vérifier les dépendances et de valider la présence des fichiers de sortie attendus. Ce script assure une exécution automatisée et reproductible de l'ensemble de la chaîne de traitement des données.

### 2.1. `tests_execution.py`

Ce script contient les fonctions clés suivantes :

-   `check_dependencies()`: Vérifie si toutes les bibliothèques Python nécessaires (pandas, numpy, matplotlib, seaborn, scikit-learn) sont installées. En cas de dépendances manquantes, une erreur est signalée.
-   `run_step(script_name)`: Exécute un script Python donné en utilisant `subprocess`. Il capture les sorties et les erreurs, et gère les dépassements de délai. Il retourne `True` en cas de succès et `False` en cas d'échec.
-   `verify_outputs()`: Contrôle la présence des fichiers de données (`eleves_theme_D_groupe63.csv`) et de toutes les figures (`.png`) générées par les scripts d'analyse dans les dossiers `data/` et `figures/`.
-   `main()`: La fonction principale qui orchestre l'appel des fonctions précédentes. Elle exécute successivement `config_seed.py`, `01_generation_donnees.py`, `02_stat_univariee.py`, `03_stat_bivariee.py`, `04_clustering.py`, et `05_classification_supervisee.py`.

## 3. Description des étapes pour copier-coller tout le code

Pour reproduire l'environnement et exécuter le projet, les étapes suivantes doivent être suivies :

1.  **Cloner le dépôt (si applicable) ou télécharger les fichiers du projet.** Assurez-vous que tous les fichiers `.py`, le `README.md`, et les dossiers `data/` et `figures/` (initialement vides ou avec les fichiers générés) sont présents dans le répertoire racine du projet.
2.  **Installer les dépendances Python.** Ouvrez un terminal et exécutez la commande suivante :
    ```bash
    sudo pip3 install pandas numpy matplotlib seaborn scikit-learn
    ```
3.  **Exécuter le script principal de tests.** Une fois les dépendances installées, lancez le script `tests_execution.py` pour vérifier l'intégralité du fonctionnement du projet :
    ```bash
    python3 tests_execution.py
    ```
    Alternativement, pour une exécution complète et directe des analyses sans les vérifications de `tests_execution.py`, vous pouvez lancer `main.py` :
    ```bash
    python3 main.py
    ```

Le script `tests_execution.py` affichera des messages de progression et de succès/échec pour chaque étape, ainsi qu'un résumé final.

## 4. Résultat obtenu, tableau, valeur calculée, graphique ou capture de code

L'exécution réussie de `tests_execution.py` (ou `main.py`) génère les sorties suivantes :

-   Un fichier CSV : `data/eleves_theme_D_groupe63.csv` contenant les 200 enregistrements d'élèves.
-   Plusieurs fichiers PNG dans le dossier `figures/` :
    -   `distribution_notes.png` (histogramme et boîte à moustaches des notes)
    -   `bivariee_regression.png` (nuage de points et droite de régression des heures de travail vs notes)
    -   `kmeans_elbow_silhouette.png` (méthode du coude et score de silhouette pour le clustering)
    -   `kmeans_clusters_k3.png` (visualisation des clusters d'élèves)
    -   `confusion_matrix.png` (matrice de confusion du modèle de classification)

Un exemple de sortie console après exécution de `tests_execution.py` (ou `main.py`) :

```text
[HH:MM:SS] === DÉBUT DE LA PROCÉDURE DE TEST GLOBALE (Responsable: Miyebe Ariel) ===
[HH:MM:SS] Vérification des dépendances...
[HH:MM:SS] Toutes les dépendances sont installées.
[HH:MM:SS] Exécution de config_seed.py...
Nom original: KENGNE GUEPOUOKSI Pierre Josué
Nom normalisé: KENGNEGUEPOUOKSIPIERREJOSUE
Graine générée: 1201603772
Numéro de groupe: 63
Test de reproductibilité (même nom): 1201603772
Test de différence (nom différent): 341399181
Test de différence (nom similaire sans accent): 1201603772
Test de différence (nom similaire sans espace): 1201603772
Test de différence (nom similaire casse différente): 1201603772
[HH:MM:SS] SUCCÈS: config_seed.py s'est terminé correctement.
[HH:MM:SS] Exécution de 01_generation_donnees.py...
Données générées pour 200 élèves et sauvegardées dans data/eleves_theme_D_groupe63.csv
Extrait des 10 premières lignes:
| id_eleve   |   heures_travail |   note_evaluation | orientation   |
|:-----------|-----------------:|------------------:|:--------------|
| E001       |               18 |              17.9 | scientifique  |
| E002       |                3 |               5.3 | littéraire    |
| E003       |               18 |              19.5 | scientifique  |
| E004       |               10 |              12.6 | littéraire    |
| E005       |               18 |              19.7 | scientifique  |
| E006       |               16 |              16.5 | littéraire    |
| E007       |                0 |               6.1 | littéraire    |
| E008       |               20 |              20   | scientifique  |
| E009       |                3 |               3.9 | scientifique  |
| E010       |               24 |              20   | littéraire    |
Statistiques descriptives rapides:
|       |   heures_travail |   note_evaluation |
|:------|-----------------:|------------------:|
| count |        200       |         200       |
| mean  |         11.55    |          13.441   |
| std   |          7.11905 |           4.81562 |
| min   |          0       |           2.1     |
| 25%   |          6       |           9.575   |
| 50%   |         10       |          13       |
| 75%   |         17.25    |          17.925   |
| max   |         25       |          20       |
[HH:MM:SS] SUCCÈS: 01_generation_donnees.py s'est terminé correctement.
[HH:MM:SS] Exécution de 02_stat_univariee.py...
--- Analyse Univariée de la Note d'Évaluation ---
Statistiques descriptives de la note d'évaluation:
|       |   note_evaluation |
|:------|------------------:|
| count |         200       |
| mean  |          13.441   |
| std   |           4.81562 |
| min   |           2.1     |
| 25%   |           9.575   |
| 50%   |          13       |
| 75%   |          17.925   |
| max   |          20       |
Premier quartile (Q1): 9.57
Troisième quartile (Q3): 17.92
Écart interquartile (IQR): 8.35
Écart-type: 4.82
Valeurs atypiques (hors de [-2.95, 30.45]):
Aucune valeur atypique détectée selon la méthode IQR.
Élèves avec une note très faible (< 8):
| id_eleve   |   note_evaluation |
|:-----------|------------------:|
| E002       |               5.3 |
| E007       |               6.1 |
| E009       |               3.9 |
| E013       |               7.9 |
| E022       |               6.6 |
| E039       |               6   |
| E059       |               3.6 |
| E069       |               7   |
| E076       |               5.2 |
| E085       |               7.4 |
| E097       |               7.3 |
| E103       |               7   |
| E113       |               6.1 |
| E114       |               4.2 |
| E115       |               2.1 |
| E123       |               6.3 |
| E129       |               7.1 |
| E142       |               7.2 |
| E145       |               7.9 |
| E147       |               7.4 |
| E158       |               6.5 |
| E161       |               7.4 |
| E166       |               4   |
| E168       |               7.6 |
| E172       |               3   |
| E177       |               5.7 |
| E183       |               5.7 |
| E191       |               7.8 |
Élèves avec une note très forte (> 16):
| id_eleve   |   note_evaluation |
|:-----------|------------------:|
| E001       |              17.9 |
| E003       |              19.5 |
| E005       |              19.7 |
| E006       |              16.5 |
| E008       |              20   |
| E010       |              20   |
| E011       |              20   |
| E012       |              20   |
| E017       |              17.8 |
| E020       |              20   |
| E023       |              20   |
| E024       |              16.3 |
| E026       |              18.4 |
| E029       |              20   |
| E031       |              19.4 |
| E032       |              20   |
| E035       |              18   |
| E036       |              20   |
| E037       |              16.8 |
| E043       |              20   |
| E045       |              20   |
| E048       |              20   |
| E049       |              17.5 |
| E053       |              17   |
| E055       |              19.5 |
| E056       |              17.5 |
| E057       |              17.1 |
| E060       |              17.1 |
| E061       |              18.8 |
| E062       |              20   |
| E066       |              17.2 |
| E070       |              16.5 |
| E074       |              19.1 |
| E077       |              19.1 |
| E080       |              18.1 |
| E083       |              17.7 |
| E086       |              17.1 |
| E087       |              16.1 |
| E093       |              19.6 |
| E095       |              20   |
| E096       |              19   |
| E099       |              19.9 |
| E104       |              20   |
| E106       |              17.1 |
| E107       |              20   |
| E109       |              17   |
| E110       |              16.2 |
| E111       |              18.5 |
| E120       |              20   |
| E121       |              18.6 |
| E122       |              20   |
| E125       |              20   |
| E126       |              20   |
| E128       |              17.4 |
| E130       |              20   |
| E131       |              18.5 |
| E135       |              20   |
| E140       |              16.5 |
| E141       |              17.2 |
| E143       |              20   |
| E146       |              20   |
| E148       |              16.3 |
| E151       |              20   |
| E154       |              19.2 |
| E162       |              18.2 |
| E173       |              20   |
| E178       |              18   |
| E179       |              16.2 |
| E180       |              16.6 |
| E185       |              20   |
| E190       |              16.1 |
| E192       |              19   |
| E195       |              20   |
| E197       |              20   |
| E198       |              17.1 |
| E199       |              20   |
Graphiques de distribution des notes sauvegardés dans figures/distribution_notes.png
[HH:MM:SS] SUCCÈS: 02_stat_univariee.py s'est terminé correctement.
[HH:MM:SS] Exécution de 03_stat_bivariee.py...
--- Analyse Bivariée (Heures de Travail vs Note d'Évaluation) ---
Coefficient de corrélation de Pearson entre heures_travail et note_evaluation: 0.93
Modèle de régression linéaire:
  Coefficient (pente): 0.64
  Ordonnée à l'origine: 5.96
  Erreur Quadratique Moyenne (MSE) sur l'ensemble de test: 3.94
  Coefficient de détermination (R^2) sur l'ensemble de test: 0.80
  Le R^2 élevé suggère que les heures de travail expliquent une grande partie de la variance des notes.
Nuage de points avec droite de régression sauvegardé dans figures/bivariee_regression.png
--- Limites d'utilisation pour la prédiction ---
La prédiction de la note d'un élève à partir de ses heures de travail devient moins fiable si:
1. Les heures de travail de l'élève sont en dehors de la plage observée dans nos données (extrapolation).
2. Le coefficient de détermination (R^2) est faible, indiquant que le modèle n'explique pas bien la variance.
3. La relation observée n'est pas strictement linéaire ou est influencée par d'autres facteurs non modélisés.
Il est crucial de considérer ces limites avant de prendre des décisions basées sur ces prédictions.
[HH:MM:SS] SUCCÈS: 03_stat_bivariee.py s'est terminé correctement.
[HH:MM:SS] Exécution de 04_clustering.py...
--- Classification Non Supervisée (Clustering K-means) ---
Données standardisées (extrait):
|   heures_travail |   note_evaluation |
|-----------------:|------------------:|
|         0.908293 |          0.928269 |
|        -1.20402  |         -1.69478  |
|         0.908293 |          1.26136  |
|        -0.218272 |         -0.175078 |
|         0.908293 |          1.30299  |
Graphiques de la méthode du coude et du score de silhouette sauvegardés dans figures/kmeans_elbow_silhouette.png
Choix du nombre de clusters optimal: 3
Centres des clusters (en valeurs originales):
|   Cluster |   heures_travail |   note_evaluation |
|----------:|-----------------:|------------------:|
|         0 |         19.8116  |          18.8594  |
|         1 |          3.90625 |           7.95469 |
|         2 |         10.3433  |          13.1015  |
Visualisation des clusters sauvegardée dans figures/kmeans_clusters_k3.png
Profils des clusters (moyennes des variables par cluster):
|   cluster |   heures_travail |   note_evaluation |
|----------:|-----------------:|------------------:|
|         0 |         19.8116  |          18.8594  |
|         1 |          3.90625 |           7.95469 |
|         2 |         10.3433  |          13.1015  |
Répartition des orientations par cluster:
|   cluster |   littéraire |   scientifique |
|----------:|-------------:|---------------:|
|         0 |     0.188406 |       0.811594 |
|         1 |     0.71875  |       0.28125  |
|         2 |     0.462687 |       0.537313 |
[HH:MM:SS] SUCCÈS: 04_clustering.py s'est terminé correctement.
[HH:MM:SS] Exécution de 05_classification_supervisee.py...
--- Classification Supervisée (Prédiction de l'Orientation) ---
Précision (Accuracy): 0.65
Précision (Precision): 0.66
Rappel (Recall): 0.76
Score F1: 0.70
Matrice de confusion:
|                    |   Prédit: Littéraire |   Prédit: Scientifique |
|:-------------------|---------------------:|-----------------------:|
| Réel: Littéraire   |                   14 |                     13 |
| Réel: Scientifique |                    8 |                     25 |
Matrice de confusion sauvegardée dans figures/confusion_matrix.png
--- Évaluation de la confiance et risques pédagogiques ---
Le modèle a une précision de 0.65. Cela signifie qu'il classe correctement 65% des élèves.
Cependant, il est important de considérer les erreurs:
  - Faux positifs (élèves littéraires prédits scientifiques): 13 cas.
  - Faux négatifs (élèves scientifiques prédits littéraires): 8 cas.
Un faux négatif peut être plus critique pédagogiquement, car un élève apte à la filière scientifique pourrait être mal orienté.
La confiance dans ce système dépendra de la tolérance de l'établissement aux erreurs, en particulier les faux négatifs.
Il est recommandé d'utiliser ce système comme un outil d'aide à la décision, et non comme un substitut au conseil de classe.
[HH:MM:SS] SUCCÈS: 05_classification_supervisee.py s'est terminé correctement.
[HH:MM:SS] Vérification des fichiers de sortie...
[HH:MM:SS] PRÉSENT: data/eleves_theme_D_groupe63.csv
[HH:MM:SS] PRÉSENT: figures/distribution_notes.png
[HH:MM:SS] PRÉSENT: figures/bivariee_regression.png
[HH:MM:SS] PRÉSENT: figures/kmeans_elbow_silhouette.png
[HH:MM:SS] PRÉSENT: figures/kmeans_clusters_k3.png
[HH:MM:SS] PRÉSENT: figures/confusion_matrix.png
[HH:MM:SS] === TOUS LES TESTS ONT RÉUSSI. LE PROJET EST PRÊT POUR LE RENDU. ===
```

## 5. Difficultés rencontrées, choix méthodologiques, limites

Lors du développement du script `tests_execution.py`, les principales difficultés ont été de s'assurer que chaque script d'analyse s'exécute correctement et que les sorties attendues sont bien générées. Cela a nécessité une attention particulière à la gestion des chemins de fichiers et à la capture des erreurs potentielles lors de l'exécution des sous-processus.

**Choix méthodologiques :**

-   Utilisation de `subprocess.run` avec `capture_output=True` pour exécuter les scripts Python de manière isolée et récupérer leurs sorties standard et erreurs. Cela permet une meilleure traçabilité des problèmes.
-   Mise en place d'un `timeout` pour chaque exécution de script afin d'éviter qu'un script bloqué ne paralyse l'ensemble du processus de test.
-   Vérification explicite de la présence des fichiers de sortie (`.csv` et `.png`) pour confirmer que les analyses ont bien produit les artefacts attendus.

**Limites :**

-   Le script `tests_execution.py` ne réalise pas de tests unitaires approfondis sur la logique interne de chaque script d'analyse. Il se concentre sur l'exécution et la vérification des sorties de haut niveau.
-   La vérification des dépendances est basique et ne gère pas les versions spécifiques des bibliothèques.

## 6. Ce que je dois savoir expliquer à l'oral

Pour une présentation orale, je devrais être capable d'expliquer :

1.  **Le rôle et l'importance du script `tests_execution.py`** dans le processus de développement du projet, notamment pour garantir la reproductibilité et la fiabilité des analyses.
2.  **Comment le script orchestre l'exécution** des différents modules d'analyse et comment il vérifie la complétude des résultats.
3.  **Les types de vérifications effectuées** (dépendances, exécution des scripts, présence des fichiers de sortie).
4.  **Les erreurs potentielles que ce script permet de détecter** (scripts manquants, erreurs d'exécution, fichiers de sortie absents).
5.  **L'utilité d'un tel script** pour un projet de groupe, en particulier pour l'intégration continue et la validation finale avant le rendu.

## 7. Références

[1] Cahier des Charges (CDC) du TP INF232 - Statistiques et Analyse de Données. Document fourni par l'utilisateur.
[2] INF232_TP_2026.pdf - Sujet du TP INF232. Document fourni par l'utilisateur.
