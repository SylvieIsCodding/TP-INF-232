# Documentation du fichier config_seed

Ce fichier sert à préparer la graine utilisée pour générer les données.

## Étapes réalisées

### 1. Normalisation du nom du chef
On commence par normaliser le nom du chef :
- le nom est mis en majuscule ;
- les accents et les caractères spéciaux sont supprimés ;
- seuls les caractères alphanumériques sont conservés.

```python
def normaliser_nom(nom_chef):
    texte = nom_chef.upper()
    texte = ''.join(
        caractere for caractere in unicodedata.normalize('NFD', texte)
        if unicodedata.category(caractere) != 'Mn'
    )
    texte = ''.join(
        caractere for caractere in texte
        if caractere.isalnum() or caractere.isspace()
    )
    return texte
```

### 2. Calcul de la graine
Ensuite, on calcule la graine à partir de cette chaîne normalisée.

```python
def generer_graine(chaine):
    seed = 0
    modulo = 2147483647
    for position, caractere in enumerate(chaine, start=1):
        if 'A' <= caractere <= 'Z':
            valeur = ord(caractere) - ord('A') + 1
        else:
            valeur = 0

        seed = (seed * 37 + position * valeur) % modulo
    return seed
```

Le résultat obtenu permet d’obtenir une valeur stable et reproductible.
