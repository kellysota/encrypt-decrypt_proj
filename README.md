# Projet Ransomware

Ce projet fournit un script Python pour chiffrer et déchiffrer les fichiers dans un dossier spécifié en utilisant le module `cryptography.fernet`.

## Fonctionnalités
- **Génération de Clé** : Génère une clé de chiffrement et la sauvegarde dans un fichier.
- **Chiffrement** : Chiffre tous les fichiers d’un dossier, en les sauvegardant avec l’extension `.aes`.
- **Déchiffrement** : Déchiffre les fichiers `.aes` et restaure leur forme originale.

## Prérequis
- Python 3.x
- Module `cryptography`
