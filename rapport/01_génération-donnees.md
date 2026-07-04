# **Documentation de génération du jeu de données**

## **Génération d'un jeu de données synthétique de 200 élèves**

### **1\. Variables choisies et leurs bornes**

Le jeu de données est composé de **200 élèves**.

| Variable | Format | Bornes | Description |
| :---- | :---- | :---- | :---- |
| id\_eleve | Chaîne | E001–E200 | Identifiant unique de l'élève |
| note\_evaluation | Nombre (2 déc) | 0 – 20 | Note à l'évaluation de mathématiques / raisonnement scientifique |
| heures\_travail | Nombre (2 déc.) | 0 – 25 | Heures de travail personnel déclarées par semaine |
| orientation | Chaîne | scientifique / littéraire | Orientation recommandée par le conseil de classe |

Les bornes ont été choisies afin de rester cohérentes avec un contexte scolaire réaliste :

* un élève ne peut pas travailler un nombre d'heures négatif ;  
* une charge de travail supérieure à 25 heures par semaine est considérée comme peu réaliste et est donc limitée ;  
* les notes sont comprises entre 0 et 20 conformément au système de notation utilisé.

## **2\. Logique de génération**

La génération du jeu de données repose sur un **générateur pseudo-aléatoire initialisé avec une graine** (`random.Random(graine)`).

L'utilisation d'une graine garantit que deux exécutions utilisant la même valeur produisent exactement le même jeu de données. Cette propriété assure la reproductibilité des résultats.

La génération d'un élève suit les étapes suivantes :

1. Génération du nombre d'heures de travail selon une **loi normale** de moyenne 10 heures et d'écart-type 5 heures.  
2. Limitation des heures de travail dans l'intervalle \[0 ; 25\].  
3. Génération d'un bruit aléatoire suivant une loi normale de moyenne 0 et d'écart-type 2,5.  
4. Calcul de la note en fonction des heures de travail et du bruit.  
5. Limitation de la note dans l'intervalle \[0 ; 20\].  
6. Calcul d'un score prenant principalement en compte la note, légèrement les heures de travail et un second bruit aléatoire.  
7. Attribution de l'orientation selon ce score.  
8. Enregistrement de l'ensemble des informations dans le jeu de données.

## **3\. Pourquoi les données générées sont plausibles**

Le jeu de données cherche à reproduire un comportement réaliste observé dans un contexte scolaire.

### **Répartition des heures de travail**

Les heures de travail suivent une loi normale. Ainsi, la majorité des élèves travaillent autour de 10 heures par semaine, tandis que très peu présentent des valeurs extrêmes (proches de 0 ou de 25 heures).

Cette répartition est plus réaliste qu'un tirage uniforme où toutes les valeurs auraient la même probabilité.

### **Variabilité des notes**

Deux élèves travaillant le même nombre d'heures n'obtiennent pas nécessairement la même note.

Cette variabilité est simulée grâce à un **bruit aléatoire** représentant des facteurs non observés comme :le niveau de préparation, les capacités personnelles, le stress,la difficulté de l'épreuve, la chance.

Le bruit possède une moyenne nulle afin de ne pas favoriser artificiellement les notes vers le haut ou vers le bas.

### **Orientation**

L'orientation n'est pas déterminée uniquement par la note obtenue. Dans un contexte réel, elle peut également dépendre d'autres facteurs (motivation, avis des enseignants, projet de l'élève, etc.). Ces facteurs étant difficiles à modéliser individuellement, ils sont représentés par un score combinant principalement la note, secondairement les heures de travail et un bruit aléatoire. Cette approche produit un jeu de données plus réaliste et évite une séparation artificielle entre les deux orientations.

## **4\. Implémentation de la relation entre le travail et les notes**

La relation entre le travail personnel et la réussite est modélisée par la formule :

**note \= 8 \+ 0,5 × heures\_travail \+ bruit**

Cette formule traduit plusieurs hypothèses :

* un élève possède une note de base de 8 points ;  
* chaque heure de travail supplémentaire augmente la note d'environ 0,5 point ;  
* le bruit ajoute une variabilité réaliste afin que deux élèves ayant travaillé autant puissent obtenir des résultats différents.

Cette relation crée une **corrélation positive** entre les variables **heures\_travail** et **note\_evaluation** : en moyenne, les élèves qui travaillent davantage obtiennent de meilleures notes, tout en conservant une dispersion compatible avec une situation réelle.

L'orientation est ensuite calculée à partir du score :

**score \= 0,7 × note \+ 0,1 × heures\_travail \+ bruit**

Si le score est supérieur ou égal à 10,2, l'élève est orienté vers la filière **scientifique** ; sinon, il est orienté vers la filière **littéraire**.

## **5\. Les cinq points clés à retenir**

1. **Le jeu de données est entièrement reproductible** grâce à l'utilisation d'une graine fixe et d'un générateur pseudo-aléatoire local.  
2. **Toutes les variables respectent leurs bornes**, ce qui garantit la cohérence des données produites.  
3. **Une corrélation positive est volontairement introduite** entre le nombre d'heures de travail et la note d'évaluation afin de représenter une situation réaliste.  
4. **Le bruit aléatoire permet de simuler les différences individuelles** entre les élèves et d'éviter une relation parfaitement déterministe entre le travail et les résultats.  
5. **Le score d'orientation est calculé à partir d'une combinaison pondérée de la note d'évaluation, des heures de travail et d'un bruit aléatoire.** Le coefficient 0,7 attribué à la note traduit le fait que les résultats scolaires constituent le principal critère d'orientation. Le coefficient 0,1 appliqué aux heures de travail introduit une influence secondaire liée à l'investissement personnel, sans surévaluer cette variable puisqu'elle contribue déjà à la note. Enfin, un bruit aléatoire suivant une loi normale de moyenne 0 et d'écart-type 3 représente les facteurs non observés (motivation, avis des enseignants, choix personnel, etc.) et permet d'obtenir un jeu de données plus réaliste en évitant une séparation parfaitement déterministe entre les orientations. Les coefficients ont été choisis de manière empirique afin d'obtenir une répartition cohérente des élèves et une corrélation plausible entre les variables.

   
