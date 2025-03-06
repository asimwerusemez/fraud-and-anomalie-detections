# Détection de Fraude Financière

Ce dépôt contient le code source et les ressources pour un projet de détection de fraude financière utilisant des techniques de machine learning et de deep learning.

## Introduction

La détection de la fraude financière est une application cruciale de l'intelligence artificielle et de l'apprentissage automatique. Ce projet vise à développer et à évaluer des modèles capables de détecter des transactions frauduleuses avec une grande précision. Nous utilisons diverses bibliothèques Python telles que Scikit-learn, TensorFlow et Kivy pour la visualisation des données et la création d'une interface utilisateur.

## Fonctionnalités

- **Prétraitement des Données** :
    - Nettoyage et transformation des données financières pour une utilisation optimale dans les modèles.
    - Gestion des valeurs manquantes et des données aberrantes.
    - Normalisation et standardisation des données.
- **Modélisation** :
    - Implémentation de plusieurs algorithmes de machine learning (régression logistique, arbres de décision, forêts aléatoires, etc.).
    - Implémentation de modèles de deep learning (réseaux de neurones récurrents, réseaux de neurones convolutionnels, etc.).
    - Optimisation des hyperparamètres des modèles.
- **Évaluation des Modèles** :
    - Évaluation des performances des modèles en utilisant des métriques pertinentes (précision, rappel, F1-score, AUC-ROC).
    - Validation croisée pour évaluer la robustesse des modèles.
    - Comparaison des performances des différents modèles.
- **Interface Utilisateur** :
    - Utilisation de Kivy pour développer une interface utilisateur intuitive.
    - Visualisation interactive des données et des résultats des modèles.
    - Possibilité de tester les modèles avec de nouvelles données.

## Bibliothèques Utilisées

- **NumPy** : Pour les opérations numériques.
- **Pandas** : Pour la manipulation et l'analyse des données.
- **Matplotlib** et **Seaborn** : Pour la visualisation des données.
- **Scikit-learn** : Pour les algorithmes de machine learning et l'évaluation des modèles.
- **TensorFlow** : Pour les modèles de deep learning.
- **Kivy** : Pour l'interface utilisateur.

## Installation

1. **Cloner le dépôt :**

    ```bash
    git clone [https://github.com/votre-utilisateur/votre-depot.git](https://github.com/votre-utilisateur/votre-depot.git)
   cd votre-depot

2. **Créer un environnement virtuel (recommandé) :**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sous Linux/macOS
    venv\Scripts\activate  # Sous Windows

3. Installer les dépendances :

    ```bash
    pip install -r requirements.txt # si vous avez un fichier requirements.txt
    # sinon, installez les dépendances individuellement :
    pip install numpy pandas matplotlib seaborn scikit-learn tensorflow kivy kivy-deps.sdl2 kivy-deps.glew


## Utilisation

1. **Prétraiter les données :**
    Exécutez le script de prétraitement des données pour préparer les données pour l'entraînement des modèles.

2. **Entraîner les modèles :**
    Utilisez les scripts fournis pour entraîner les modèles de machine learning et de deep learning.

3. **Lancer l'application :**
    Lancez l'application Kivy pour visualiser les résultats et analyser les données.


## Contribution
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des modifications que vous proposez.

## Auteurs
Matthieu Asim