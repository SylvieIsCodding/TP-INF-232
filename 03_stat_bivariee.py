"""
03_stat_bivariee.py
But : Étudier le lien entre heures de travail et note d'évaluation.
Étapes : nuage de points → corrélation → régression → prédiction
"""

import csv, math, os
import matplotlib.pyplot as plt

# ── 1. CHARGEMENT DES DONNÉES ────────────────────────────────
def charger(fichier):
    heures, notes = [], []
    with open(fichier, newline="", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            heures.append(float(ligne["heures_travail"]))
            notes.append(float(ligne["note_evaluation"]))
    return heures, notes

# ── 2. OUTILS STATISTIQUES ──────────────────────────────────
def moy(v):  return sum(v) / len(v)
def std(v):  return math.sqrt(sum((x - moy(v))**2 for x in v) / len(v))

def correlation(x, y):
    """Pearson r : mesure la force du lien linéaire entre x et y."""
    mx, my = moy(x), moy(y)
    cov = sum((x[i]-mx)*(y[i]-my) for i in range(len(x))) / len(x)
    return cov / (std(x) * std(y))

def regression(x, y):
    """Calcule a et b de la droite  ŷ = a·x + b  (moindres carrés)."""
    mx, my = moy(x), moy(y)
    a = sum((x[i]-mx)*(y[i]-my) for i in range(len(x))) / \
        sum((x[i]-mx)**2         for i in range(len(x)))
    return a, my - a*mx

def r_carre(x, y, a, b):
    """R² : proportion de la variance de y expliquée par x."""
    my = moy(y)
    return 1 - sum((y[i]-(a*x[i]+b))**2 for i in range(len(y))) / \
                   sum((yi-my)**2 for yi in y)

# ── 3. PROGRAMME PRINCIPAL ───────────────────────────────────
heures, notes = charger(os.path.join("data", "eleves_theme_D.csv"))

r        = correlation(heures, notes)
a, b     = regression(heures, notes)
r2       = r_carre(heures, notes, a, b)

print(f"Données : {len(heures)} élèves")
print(f"Corrélation Pearson  r  = {r:+.4f}  → lien {'fort' if abs(r)>=0.6 else 'modéré'} et {'positif' if r>0 else 'négatif'}")
print(f"Droite de régression     ŷ = {a:.4f}·x + {b:.4f}")
print(f"  • +1h de travail  ≈  +{a:.2f} point(s) de note")
print(f"  • Sans travail      ≈  {b:.1f}/20")
print(f"Coefficient R²       = {r2:.4f}  → {r2*100:.1f}% de la variance expliquée\n")

print(f"{'Heures':>8}  {'Note prédite':>14}")
for h in [0, 5, 10, 15, 20, 25]:
    note = round(max(0, min(20, a*h+b)), 2)
    print(f"{h:>7}h  {note:>12.2f}/20")

# ── 4. GRAPHIQUE ─────────────────────────────────────────────
os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(9, 5))
plt.scatter(heures, notes, color="steelblue", alpha=0.6, label="Élèves")
x_range = [min(heures), max(heures)]
plt.plot(x_range, [a*x+b for x in x_range], color="tomato", linewidth=2,
         label=f"ŷ = {a:.3f}·x + {b:.3f}  (R²={r2:.3f})")
plt.xlabel("Heures de travail par semaine")
plt.ylabel("Note d'évaluation (sur 20)")
plt.title("Lien entre heures de travail et note d'évaluation")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("figures/03_nuage_regression.png", dpi=150)
plt.show()
print("Graphique sauvegardé → figures/03_nuage_regression.png")
