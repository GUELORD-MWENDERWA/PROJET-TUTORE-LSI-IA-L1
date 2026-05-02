@echo off
REM Script de lancement pour l'application IA
echo.
echo ==========================================
echo   Reconnaissance d'Objets sur Images
echo ==========================================
echo.

REM Vérifier si l'environnement virtuel existe
if not exist "env\Scripts\activate.bat" (
    echo [*] Environnement virtuel non trouvé, création...
    python -m venv env
)

REM Activer l'environnement virtuel
call env\Scripts\activate.bat

REM Installer les dépendances si nécessaire
echo [*] Vérification des dépendances...
pip install -q -r requirements.txt 2>nul

REM Lancer l'entrainement + evaluation
echo [*] Entrainement et evaluation...
python src/main.py

REM Maintenir la fenêtre ouverte en cas d'erreur
if errorlevel 1 (
    echo.
    echo [!] L'application s'est terminée avec une erreur.
    pause
)
