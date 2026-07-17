# Raccourcisseur de liens

Une application web simple développée avec Flask permettant de raccourcir des URL et de suivre le nombre de clics sur chaque lien.

## Aperçu

L'utilisateur colle une URL dans le formulaire de la page d'accueil. L'application génère un code court aléatoire, l'associe à l'URL d'origine, puis affiche le lien raccourci ainsi qu'un historique de tous les liens créés durant la session, avec leur nombre de clics respectif.

## Prérequis

- Python 3.7 ou version supérieure
- Flask

## Installation

```bash
pip install flask
```

## Utilisation

Exécuter le script suivant :

```bash
python app.py
```

Ouvrir ensuite un navigateur à l'adresse `http://127.0.0.1:5000/`.

## Fonctionnalités

- Génération d'un code court aléatoire unique (6 caractères alphanumériques)
- Ajout automatique du préfixe `https://` si absent de l'URL saisie
- Redirection vers l'URL d'origine via le lien court
- Comptage du nombre de clics par lien
- Historique des liens créés, affiché sur la page d'accueil

## Structure du code

- `make_short_code` : génère un code court unique
- `is_code_taken` : vérifie qu'un code n'est pas déjà utilisé
- `normalize_url` : nettoie et complète l'URL saisie
- `find_link` : recherche un lien à partir de son code
- `go_to_target` : route de redirection (`/<code>`)
- `home` : route principale (formulaire et historique)

## Stockage des données

⚠️ Les liens sont actuellement stockés en mémoire (liste Python), sans base de données. Cela signifie que **tous les liens sont perdus au redémarrage du serveur**. Cette version convient pour une démonstration ou un usage local, mais une base de données persistante (SQLite, PostgreSQL, etc.) serait nécessaire pour un usage en production.

## Licence

Projet libre d'utilisation à des fins d'apprentissage.
