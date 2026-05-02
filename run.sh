#!/bin/bash
# Script de lancement pour l'application IA

echo ""
echo "=========================================="
echo "  Reconnaissance d'Objets sur Images"
echo "=========================================="
echo ""

# Vérifier si l'environnement virtuel existe
if [ ! -d "env" ]; then
    echo "[*] Environnement virtuel non trouvé, création..."
    python3 -m venv env
fi

# Activer l'environnement virtuel
source env/bin/activate

# Installer les dépendances
echo "[*] Vérification des dépendances..."
pip install -q -r requirements.txt

# Lancer l'entrainement + evaluation
echo "[*] Entrainement et evaluation..."
python src/main.py

# Maintenir le terminal ouvert en cas d'erreur
if [ $? -ne 0 ]; then
    echo ""
    echo "[!] L'application s'est terminée avec une erreur."
    read -p "Appuyez sur Entrée pour fermer..."
fi
