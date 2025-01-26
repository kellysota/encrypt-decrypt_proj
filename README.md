# Projet Ransomware

Ce projet fournit un ensemble de scripts Python pour chiffrer, déchiffrer et surveiller les activités utilisateur à l'aide d'un keylogger. Il inclut également des fonctionnalités d'exfiltration des fichiers et de génération aléatoire de clés de chiffrement.

## Fonctionnalités
- **Génération de Clé** : Génère une clé de chiffrement et la sauvegarde dans un fichier spécifié.
- **Chiffrement** : Chiffre tous les fichiers d’un dossier et de ses sous-dossiers, en les sauvegardant avec l’extension `.aes`.
- **Déchiffrement** : Déchiffre les fichiers `.aes` et restaure leur forme originale.
- **Exfiltration des fichiers** : Envoie les fichiers à un serveur distant avant de les chiffrer.
- **Keylogger** : Enregistre les saisies clavier de l'utilisateur dans un fichier de log.

## Prérequis
- Python 3.x
- Module `cryptography` et `pynut`

Pour installer les modules requis, exécutez:
```bash
pip install cryptography pynput
```

## Utilisation

### 1. Génération de Clé
Générez une clé de chiffrement et sauvegardez-la dans un fichier :
```bash
python generate_key.py
```
Par défaut, la clé sera sauvegardée dans un fichier nommé `key.key`.

### 2. Chiffrement
Chiffrez tous les fichiers dans un dossier spécifié :
```bash
python encrypt.py
```
Vous serez invité à fournir le chemin du dossier à chiffrer et le fichier contenant la clé.

### 3. Déchiffrement
Déchiffrez les fichiers `.aes` dans un dossier :
```bash
python decrypt.py
```
Fournissez le chemin du dossier et le fichier de clé lorsque demandé.

### 4. Keylogger
Pour exécuter le keylogger et enregistrer les saisies clavier :
```bash
python keylogger.py
```
Les saisies clavier seront enregistrées dans un fichier nommé `keylog.txt` par défaut.

## Notes
- **Exfiltration des fichiers** : Le script de chiffrement envoie les fichiers à un serveur distant avant de les chiffrer. Vous pouvez configurer l'adresse et le port du serveur dans le fichier `encrypt.py`.
- **Keylogger** : Le keylogger fonctionne en arrière-plan et peut être utilisé indépendamment ou conjointement avec les autres scripts.
