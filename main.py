
import os
import subprocess

def run_script(script_name):
    print(f"\nExécution de {script_name}...")
    process = subprocess.run(["python3", script_name], capture_output=True, text=True)
    print(process.stdout)
    if process.stderr:
        print(f"Erreur lors de l'exécution de {script_name}:\n{process.stderr}")
    print(f"Fin de l'exécution de {script_name}.")

if __name__ == "__main__":
    # S'assurer que le dossier 'data' existe
    if not os.path.exists("data"):
        os.makedirs("data")
    # S'assurer que le dossier 'figures' existe
    if not os.path.exists("figures"):
        os.makedirs("figures")

    # 1. Configuration de la graine et génération des données
    run_script("config_seed.py")
    run_script("01_generation_donnees.py")

    # 2. Analyses statistiques
    run_script("02_stat_univariee.py")
    run_script("03_stat_bivariee.py")
    run_script("04_clustering.py")
    run_script("05_classification_supervisee.py")

    print("\nToutes les analyses ont été exécutées. Les données sont dans 'data/' et les figures dans 'figures/'.")
