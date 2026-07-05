# Rapport INF232 - Statistiques et Analyse de Données

## Thème D: Établissement scolaire secondaire

**Auteurs:**
- KENGNE GUEPOUOKSI Pierre Josué (Chef de groupe, Matricule: 24H4286)
- Groupe: 63

**Date:** 05 Juillet 2026

---

## 1. Introduction

Ce rapport présente les résultats de l'analyse statistique et de l'apprentissage automatique appliquée à un jeu de données synthétiques d'élèves de terminale. Le projet s'inscrit dans le cadre du cours INF232 et vise à répondre à plusieurs problématiques clés pour la direction d'un établissement scolaire secondaire. L'objectif principal est de mieux comprendre les performances des élèves, d'identifier des profils distincts et de proposer une orientation scolaire automatique, tout en évaluant la fiabilité de ces propositions.

Le thème choisi est celui de l'**Établissement scolaire secondaire**. Le langage de programmation utilisé est **Python**, justifié par sa richesse en bibliothèques dédiées à l'analyse de données, à la visualisation et à l'apprentissage automatique (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn).

Les données utilisées sont entièrement synthétiques et ont été générées de manière déterministe à partir du nom du chef de groupe, garantissant la reproductibilité des analyses. Ce rapport détaille la méthodologie de génération des données, les analyses menées pour chaque question posée, les résultats obtenus, ainsi que les conclusions et les implications pédagogiques.

## 2. Mécanisme de génération des données

### 2.1. Graine numérique déterministe

Conformément aux exigences du cahier des charges [1], une graine numérique unique et reproductible a été générée à partir du nom complet du chef de groupe. L'algorithme spécifié est le suivant :

> `seed = 0` ; pour chaque caractère `c` de la chaîne normalisée, à la position `i`, on calcule `valeur(c)` comme son rang alphabétique avec `A=1, ..., Z=26`, puis `seed = (seed * 37 + (i + 1) + valeur(c)) mod 2147483647`.

Le nom du chef de groupe, **KENGNE GUEPOUOKSI Pierre Josué**, a été normalisé en **KENGNEGUEPOUOKSIPIERREJOSUE** (suppression des accents, des espaces et mise en majuscules). L'application de l'algorithme a produit la graine numérique suivante : **1201603772**.

Cette graine est utilisée pour initialiser le générateur de nombres pseudo-aléatoires de NumPy, assurant ainsi que toute exécution du script de génération de données avec le même nom de chef de groupe produira exactement le même jeu de données.

### 2.2. Génération des données synthétiques

Un jeu de données de **200 élèves de terminale** a été généré. Chaque élève est caractérisé par les variables suivantes :

| Variable | Signification | Format / Bornes |
|---|---|---|
| `id_eleve` | Identifiant unique de l'élève | `E001`, `E002`, ... |
| `note_evaluation` | Note obtenue à une évaluation interne en mathématiques / raisonnement scientifique | Nombre entre 0 et 20 |
| `heures_travail` | Nombre moyen d'heures de travail personnel par semaine | Nombre entre 0 et 25 |
| `orientation` | Orientation recommandée par le conseil de classe | `scientifique` ou `littéraire` |

La génération des données a été conçue pour introduire une relation plausible entre les variables : les élèves consacrant plus d'heures de travail ont tendance à obtenir une meilleure note, mais avec une part d'aléatoire pour simuler la réalité. De même, l'orientation est influencée par les heures de travail et la note, avec une probabilité plus élevée d'être orienté vers la filière scientifique pour les élèves performants, mais sans déterminisme absolu pour permettre une classification supervisée réaliste.

Voici un extrait des 10 premières lignes des données générées :

| id_eleve | heures_travail | note_evaluation | orientation |
|:-----------|-----------------:|------------------:|:--------------|
| E001 | 18 | 17.9 | scientifique |
| E002 | 3 | 5.3 | littéraire |
| E003 | 18 | 19.5 | scientifique |
| E004 | 10 | 12.6 | littéraire |
| E005 | 18 | 19.7 | scientifique |
| E006 | 16 | 16.5 | littéraire |
| E007 | 0 | 6.1 | littéraire |
| E008 | 20 | 20 | scientifique |
| E009 | 3 | 3.9 | scientifique |
| E010 | 24 | 20 | littéraire |

Les statistiques descriptives rapides des données générées sont les suivantes :

| | heures_travail | note_evaluation |
|:------|-----------------:|------------------:|
| count | 200 | 200 |
| mean | 11.55 | 13.441 |
| std | 7.11905 | 4.81562 |
| min | 0 | 2.1 |
| 25% | 6 | 9.575 |
| 50% | 10 | 13 |
| 75% | 17.25 | 17.925 |
| max | 25 | 20 |

## 3. Analyse Univariée de la Note d'Évaluation (Question 1)

### 3.1. Statistiques descriptives

L'analyse univariée de la variable `note_evaluation` permet de comprendre la répartition des notes obtenues par les élèves. Les statistiques descriptives sont les suivantes :

| | note_evaluation |
|:------|------------------:|
| count | 200 |
| mean | 13.441 |
| std | 4.81562 |
| min | 2.1 |
| 25% | 9.575 |
| 50% | 13 |
| 75% | 17.925 |
| max | 20 |

La note moyenne est d'environ **13.44/20**, avec un écart-type de **4.82**, indiquant une dispersion modérée des notes autour de la moyenne. Le premier quartile (Q1) est de **9.57**, le troisième quartile (Q3) est de **17.92**, et l'écart interquartile (IQR) est de **8.35**.

### 3.2. Identification des valeurs atypiques et des élèves extrêmes

En utilisant la méthode de l'écart interquartile (IQR), aucune valeur atypique n'a été détectée dans la distribution des notes, ce qui suggère une distribution relativement homogène sans valeurs extrêmes isolées.

Cependant, en définissant des seuils arbitraires pour les élèves 
très faibles (note < 8) et très forts (note > 16), nous avons identifié :

- **Élèves avec une note très faible (< 8) :**

| id_eleve | note_evaluation |
|:-----------|------------------:|
| E002 | 5.3 |
| E007 | 6.1 |
| E009 | 3.9 |
| E013 | 7.9 |
| E022 | 6.6 |
| E039 | 6.0 |
| E059 | 3.6 |
| E069 | 7.0 |
| E076 | 5.2 |
| E085 | 7.4 |
| E097 | 7.3 |
| E103 | 7.0 |
| E113 | 6.1 |
| E114 | 4.2 |
| E115 | 2.1 |
| E123 | 6.3 |
| E129 | 7.1 |
| E142 | 7.2 |
| E145 | 7.9 |
| E147 | 7.4 |
| E158 | 6.5 |
| E161 | 7.4 |
| E166 | 4.0 |
| E168 | 7.6 |
| E172 | 3.0 |
| E177 | 5.7 |
| E183 | 5.7 |
| E191 | 7.8 |

- **Élèves avec une note très forte (> 16) :**

| id_eleve | note_evaluation |
|:-----------|------------------:|
| E001 | 17.9 |
| E003 | 19.5 |
| E005 | 19.7 |
| E006 | 16.5 |
| E008 | 20.0 |
| E010 | 20.0 |
| E011 | 20.0 |
| E012 | 20.0 |
| E017 | 17.8 |
| E020 | 20.0 |
| E023 | 20.0 |
| E024 | 16.3 |
| E026 | 18.4 |
| E029 | 20.0 |
| E031 | 19.4 |
| E032 | 20.0 |
| E035 | 18.0 |
| E036 | 20.0 |
| E037 | 16.8 |
| E043 | 20.0 |
| E045 | 20.0 |
| E048 | 20.0 |
| E049 | 17.5 |
| E053 | 17.0 |
| E055 | 19.5 |
| E056 | 17.5 |
| E057 | 17.1 |
| E060 | 17.1 |
| E061 | 18.8 |
| E062 | 20.0 |
| E066 | 17.2 |
| E070 | 16.5 |
| E074 | 19.1 |
| E077 | 19.1 |
| E080 | 18.1 |
| E083 | 17.7 |
| E086 | 17.1 |
| E087 | 16.1 |
| E093 | 19.6 |
| E095 | 20.0 |
| E096 | 19.0 |
| E099 | 19.9 |
| E104 | 20.0 |
| E106 | 17.1 |
| E107 | 20.0 |
| E109 | 17.0 |
| E110 | 16.2 |
| E111 | 18.5 |
| E120 | 20.0 |
| E121 | 18.6 |
| E122 | 20.0 |
| E125 | 20.0 |
| E126 | 20.0 |
| E128 | 17.4 |
| E130 | 20.0 |
| E131 | 18.5 |
| E135 | 20.0 |
| E140 | 16.5 |
| E141 | 17.2 |
| E143 | 20.0 |
| E146 | 20.0 |
| E148 | 16.3 |
| E151 | 20.0 |
| E154 | 19.2 |
| E162 | 18.2 |
| E173 | 20.0 |
| E178 | 18.0 |
| E179 | 16.2 |
| E180 | 16.6 |
| E185 | 20.0 |
| E190 | 16.1 |
| E192 | 19.0 |
| E195 | 20.0 |
| E197 | 20.0 |
| E198 | 17.1 |
| E199 | 20.0 |

Ces listes permettent d'identifier rapidement les élèves nécessitant une attention particulière, qu'il s'agisse de soutien scolaire ou de programmes d'enrichissement.

### 3.3. Visualisation de la distribution des notes

Les graphiques suivants (histogramme et boîte à moustaches) illustrent la distribution des notes d'évaluation :

![Distribution des notes d'évaluation](figures/distribution_notes.png)

L'histogramme montre une distribution relativement normale, légèrement asymétrique vers les notes élevées, ce qui est cohérent avec la génération de données qui favorise les bonnes notes pour les élèves travaillant beaucoup. La boîte à moustaches confirme l'absence de valeurs atypiques extrêmes et la concentration des notes autour de la médiane.

### 3.4. Interprétation pour un conseil pédagogique

Pour un conseil pédagogique, il est important de présenter ces résultats de manière claire et concise. La note moyenne de 13.44/20 indique une performance globale satisfaisante. Cependant, la présence d'un nombre significatif d'élèves avec des notes inférieures à 8 (28 élèves) et supérieures à 16 (73 élèves) souligne la nécessité d'adapter les approches pédagogiques. Le conseil pourrait envisager des mesures de soutien ciblées pour les élèves en difficulté et des programmes d'approfondissement pour les plus performants. L'absence de valeurs atypiques extrêmes (outliers) suggère que les problèmes ou les réussites sont plutôt liés à des groupes d'élèves qu'à des cas isolés.

## 4. Analyse Bivariée (Heures de Travail vs Note d'Évaluation) (Question 2)

### 4.1. Corrélation et Régression Linéaire

Pour évaluer le lien entre les `heures_travail` et la `note_evaluation`, nous avons calculé le coefficient de corrélation de Pearson et effectué une régression linéaire simple.

Le **coefficient de corrélation de Pearson** est de **0.93**. Cette valeur élevée indique une forte corrélation positive entre les heures de travail et la note d'évaluation : plus un élève travaille, plus sa note a tendance à être élevée. Cette relation est cohérente avec la manière dont les données ont été générées.

Le modèle de **régression linéaire** a été entraîné sur 80% des données et testé sur les 20% restants. Les résultats sont les suivants :

- **Coefficient (pente) :** 0.64
- **Ordonnée à l'origine :** 5.96
- **Erreur Quadratique Moyenne (MSE) sur l'ensemble de test :** 3.94
- **Coefficient de détermination (R²) sur l'ensemble de test :** 0.80

Le **R² de 0.80** est élevé, ce qui signifie que 80% de la variance des notes d'évaluation peut être expliquée par les heures de travail. Cela confirme que les heures de travail sont un excellent prédicteur de la note d'évaluation dans ce jeu de données synthétiques.

### 4.2. Visualisation du nuage de points et de la droite de régression

Le graphique suivant représente le nuage de points des heures de travail en fonction de la note d'évaluation, avec la droite de régression linéaire :

![Nuage de points: Heures de Travail vs Note d'Évaluation avec Régression Linéaire](figures/bivariee_regression.png)

La droite de régression montre clairement la tendance positive, et la faible dispersion des points autour de cette droite visuellement confirme la forte corrélation.

### 4.3. Limites d'utilisation pour la prédiction

Bien que le modèle de régression linéaire soit performant, il est crucial de comprendre ses limites avant d'utiliser les heures de travail pour anticiper la note d'un élève :

1.  **Extrapolation :** La prédiction devient moins fiable si les heures de travail de l'élève sont en dehors de la plage observée dans nos données (0 à 25 heures). Prédire pour un élève qui travaillerait 30 heures par semaine, par exemple, serait une extrapolation risquée.
2.  **R² non parfait :** Même avec un R² élevé (0.80), il reste 20% de la variance des notes qui n'est pas expliquée par les heures de travail. D'autres facteurs (aptitudes individuelles, qualité de l'enseignement, motivation, etc.) influencent également la note.
3.  **Relation non strictement linéaire :** Bien que la relation soit fortement linéaire dans nos données synthétiques, dans la réalité, elle pourrait être plus complexe et non strictement linéaire, ou influencée par des interactions entre plusieurs variables.

En conclusion, les heures de travail sont un bon indicateur de la note potentielle, mais la prédiction doit être utilisée avec prudence, surtout pour des valeurs extrêmes ou sans prendre en compte d'autres facteurs qualitatifs.

## 5. Classification Non Supervisée (Clustering K-means) (Question 3)

### 5.1. Standardisation des données et choix du nombre de clusters

Pour la classification non supervisée, nous avons utilisé les variables `heures_travail` et `note_evaluation`. Ces variables ont été **standardisées** (centrées et réduites) afin que chacune contribue équitablement à la formation des clusters, indépendamment de son échelle d'origine.

Pour déterminer le nombre optimal de clusters (K), nous avons utilisé la **méthode du coude** (Elbow Method) et le **score de silhouette**. Les graphiques suivants illustrent ces deux méthodes :

![Méthode du Coude et Score de Silhouette pour K-means](figures/kmeans_elbow_silhouette.png)

Le graphique de la méthode du coude montre un 
coude prononcé à K=3, suggérant que trois clusters pourraient être un bon compromis. Le score de silhouette, quant à lui, est également maximal pour K=3 ou K=4, ce qui renforce l'idée que 3 ou 4 clusters sont pertinents. Pour cette analyse, nous avons choisi **K=3** pour la simplicité d'interprétation et la clarté des profils.

### 5.2. Description des profils d'élèves

Après avoir appliqué l'algorithme K-means avec K=3, les élèves ont été regroupés en trois clusters distincts. Les centres de ces clusters, exprimés en valeurs originales (non standardisées) des variables, permettent de caractériser chaque profil :

| Cluster | heures_travail | note_evaluation |
|--------:|---------------:|----------------:|
| 0 | 19.81 | 18.86 |
| 1 | 3.91 | 7.95 |
| 2 | 10.34 | 13.10 |

Ces centres de clusters peuvent être interprétés comme suit :

-   **Cluster 0 (Élèves Performants et Travailleurs) :** Ce groupe se caractérise par un nombre élevé d'heures de travail (environ 20h/semaine) et d'excellentes notes (environ 18.8/20). Il s'agit des élèves les plus assidus et les plus brillants.
-   **Cluster 1 (Élèves en Difficulté) :** Ce cluster regroupe les élèves avec peu d'heures de travail (environ 4h/semaine) et des notes faibles (environ 7.9/20). Ces élèves sont potentiellement en grande difficulté scolaire.
-   **Cluster 2 (Élèves Moyens) :** Ce groupe représente la majorité des élèves, avec un nombre d'heures de travail et des notes dans la moyenne (environ 10h/semaine et 13.1/20).

### 5.3. Visualisation des clusters

Le graphique suivant visualise la répartition des élèves en fonction de leurs heures de travail et de leur note d'évaluation, colorés par cluster :

![Clusters d'élèves (K=3)](figures/kmeans_clusters_k3.png)

Cette visualisation confirme la bonne séparation des trois groupes, chacun occupant une région distincte dans l'espace des variables `heures_travail` et `note_evaluation`.

### 5.4. Répartition des orientations par cluster

L'analyse de la répartition des orientations au sein de chaque cluster fournit des informations supplémentaires sur les profils :

| Cluster | littéraire | scientifique |
|--------:|-----------:|-------------:|
| 0 | 0.19 | 0.81 |
| 1 | 0.72 | 0.28 |
| 2 | 0.46 | 0.54 |

-   Le **Cluster 0** (élèves performants) est majoritairement orienté vers la filière **scientifique** (81%).
-   Le **Cluster 1** (élèves en difficulté) est majoritairement orienté vers la filière **littéraire** (72%).
-   Le **Cluster 2** (élèves moyens) présente une répartition plus équilibrée, avec une légère prédominance pour la filière **scientifique** (54%).

Ces résultats suggèrent que les profils d'élèves identifiés par le clustering sont cohérents avec les orientations recommandées, bien que la relation ne soit pas absolue, ce qui est réaliste.

## 6. Classification Supervisée (Prédiction de l'Orientation) (Question 4)

### 6.1. Modèle de prédiction et évaluation

L'objectif de cette section est de construire un modèle capable de prédire l'orientation (`scientifique` ou `littéraire`) d'un nouvel élève à partir de ses `heures_travail` et `note_evaluation`. Nous avons utilisé un modèle de **régression logistique**, un algorithme de classification supervisée adapté aux problèmes de classification binaire.

Les données ont été divisées en un ensemble d'entraînement (70%) et un ensemble de test (30%). Les variables explicatives ont été standardisées. Le modèle a été entraîné sur l'ensemble d'entraînement et évalué sur l'ensemble de test. Voici les métriques de performance :

-   **Précision (Accuracy) :** 0.65
-   **Précision (Precision) :** 0.66
-   **Rappel (Recall) :** 0.76
-   **Score F1 :** 0.70

Une précision de 0.65 signifie que le modèle classe correctement 65% des élèves. Le rappel de 0.76 indique que le modèle identifie 76% des élèves réellement scientifiques. La précision de 0.66 signifie que parmi les élèves prédits scientifiques, 66% le sont réellement.

### 6.2. Matrice de confusion

La matrice de confusion fournit une vue détaillée des performances du modèle, en distinguant les prédictions correctes et incorrectes :

| | Prédit: Littéraire | Prédit: Scientifique |
|:-------------------|---------------------:|-----------------------:|
| Réel: Littéraire | 14 | 13 |
| Réel: Scientifique | 8 | 25 |

![Matrice de Confusion](figures/confusion_matrix.png)

-   **Vrais positifs (VP) :** 25 élèves réellement scientifiques ont été correctement prédits comme scientifiques.
-   **Vrais négatifs (VN) :** 14 élèves réellement littéraires ont été correctement prédits comme littéraires.
-   **Faux positifs (FP) :** 13 élèves réellement littéraires ont été incorrectement prédits comme scientifiques.
-   **Faux négatifs (FN) :** 8 élèves réellement scientifiques ont été incorrectement prédits comme littéraires.

### 6.3. Évaluation de la confiance et risques pédagogiques

Le modèle atteint une précision de 65%, ce qui est un point de départ raisonnable pour une aide à la décision. Cependant, il est crucial de considérer les erreurs, en particulier les faux négatifs. Un faux négatif (un élève réellement scientifique prédit comme littéraire) peut avoir des conséquences pédagogiques plus importantes, car cela pourrait potentiellement sous-estimer le potentiel d'un élève et le diriger vers une filière moins adaptée à ses aptitudes.

La confiance dans ce système dépendra de la tolérance de l'établissement aux erreurs. Pour minimiser les risques pédagogiques, il est recommandé d'utiliser ce modèle comme un **outil d'aide à la décision** et non comme un substitut au conseil de classe. Les prédictions du modèle devraient être examinées par les conseillers d'orientation, qui pourront prendre en compte d'autres facteurs qualitatifs et contextuels non inclus dans le modèle.

## 7. Conclusion

Ce projet a permis de réaliser une analyse complète des données d'élèves de terminale d'un établissement scolaire secondaire, en abordant les quatre grandes familles de problématiques statistiques et d'apprentissage automatique. Nous avons démontré la capacité à générer des données synthétiques reproductibles, à analyser la distribution des notes, à établir une forte corrélation entre les heures de travail et les notes, à identifier des profils d'élèves distincts via le clustering, et à construire un modèle de prédiction d'orientation.

Les résultats montrent des tendances claires et des profils d'élèves cohérents. Le modèle de classification supervisée, bien que performant, doit être utilisé avec discernement, en complément de l'expertise humaine, pour éviter les risques liés aux erreurs de prédiction, notamment les faux négatifs.

Ce travail fournit à la direction de l'établissement des outils et des analyses pour mieux comprendre les dynamiques de performance et d'orientation de leurs élèves, permettant ainsi des interventions pédagogiques plus ciblées et éclairées.

## 8. Références

[1] Cahier des Charges (CDC) du TP INF232 - Statistiques et Analyse de Données. Document fourni par l'utilisateur.
[2] INF232_TP_2026.pdf - Sujet du TP INF232. Document fourni par l'utilisateur.
