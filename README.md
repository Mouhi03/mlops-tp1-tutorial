# TP1 — Bonnes Pratiques Logiciels pour le MLOps

> **Cours :** 51ASD — Déploiement d'IA (2026-2027)
> **Filière :** 5IASD
> **Auteur :** Mouhieddine Bouktib et Ahlam Assamsadi
> **Groupe :** G6

---

## 🎯 Objectifs

Ce TP introduit les bonnes pratiques fondamentales du MLOps à travers :

* la transformation d'un workflow ML en **script Python** ;
* la gestion d'un environnement isolé avec **Conda** ;
* le versionnage du projet avec **Git et GitHub** ;
* la gestion des fichiers générés avec `.gitignore`.

---

## 🏗️ Structure du projet

```text
tpl-git-env/
│
├── .gitignore
├── environment.yml
├── train.py
├── README.md
│
└── models/
    └── iris_model.pkl
```

> Le dossier `models/` et le modèle `.pkl` sont ignorés par Git.

---

## ⚙️ Environnement technique

| Élément       | Technologie   |
| ------------- | ------------- |
| Langage       | Python 3.10   |
| Environnement | Conda         |
| IDE           | VS Code       |
| Versionnage   | Git / GitHub  |
| Dataset       | Iris          |
| Modèle        | Random Forest |

### Bibliothèques

* `pandas`
* `scikit-learn`
* `ipykernel`
* `python-dotenv`

---

## 📦 Environnement Conda

Le projet utilise `environment.yml` afin de définir les dépendances nécessaires :

```yaml
name: mlops_base_env

channels:
  - defaults
  - conda-forge

dependencies:
  - python=3.10
  - pip
  - ipykernel
  - pandas
  - scikit-learn
  - pip:
      - python-dotenv
```

### Création de l'environnement

```bash
conda env create -f environment.yml
conda activate mlops_base_env
```

---

# 🚀 Installation et exécution

## 1. Cloner le dépôt

```bash
git clone https://github.com/Mouhi03/mlops-tp1-tutorial.git
cd mlops-tp1-tutorial
```

## 2. Activer l'environnement

```bash
conda env create -f environment.yml
conda activate mlops_base_env
```

## 3. Exécuter le pipeline

```bash
python train.py
```

### Résultat attendu

```text
[MLOps Pipeline] Starting pipeline execution...
[MLOps Pipeline] Target model successfully cached! Score: 0.9667
```

Le modèle est sauvegardé dans :

```text
models/iris_model.pkl
```

---

# 🧠 Pipeline `train.py`

Le script réalise automatiquement les étapes suivantes :

1. **Chargement** du dataset Iris avec `load_iris`.
2. **Séparation** des données en 80 % entraînement et 20 % test.
3. **Entraînement** d'un `RandomForestClassifier` avec `n_estimators=100`.
4. **Évaluation** du modèle sur les données de test.
5. **Sauvegarde** du modèle avec `pickle`.

Le paramètre `random_state=42` garantit la reproductibilité des résultats.

Le pipeline est exécuté uniquement lorsque le script est lancé directement grâce à :

```python
if __name__ == '__main__':
    execute_pipeline()
```

---

# 🚫 `.gitignore`

Le fichier `.gitignore` empêche Git de suivre les fichiers qui ne doivent pas être versionnés :

```gitignore
# Environnements Python
.conda/
env/
venv/
__pycache__/
*.pyc

# Données et modèles
data/
models/
*.pkl
*.h5

# Configuration locale
.vscode/
```

### Vérifier qu'un fichier est ignoré

```bash
git check-ignore -v models/iris_model.pkl
```

Les règles :

```gitignore
models/
*.pkl
```

sont responsables de l'exclusion du modèle.

---

# 📋 Questions d'évaluation

## Question 1 — Git & `.gitignore`

`models/iris_model.pkl` n'apparaît pas dans `git status` car il est exclu par `.gitignore`.

Les règles concernées sont :

```gitignore
models/
*.pkl
```

Le fichier existe sur la machine mais n'est pas suivi par Git.

---

## Question 2 — Pourquoi utiliser `environment.yml` ?

`environment.yml` permet de :

* définir les dépendances du projet ;
* recréer facilement le même environnement ;
* garantir une meilleure reproductibilité ;
* partager une configuration commune avec toute l'équipe.

L'environnement peut être recréé avec :

```bash
conda env create -f environment.yml
```

---

## Question 3 — Pourquoi utiliser un script Python plutôt qu'un notebook ?

Un script Python présente notamment deux avantages :

* **Automatisation :** il peut être exécuté directement dans un terminal, une pipeline CI/CD ou un conteneur.
* **Maintenabilité :** le code est organisé en fonctions, facilement versionnable et testable.

---

## Question 4 — Pourquoi éviter les gros fichiers dans Git ?

Un fichier CSV de 2 Go peut :

* augmenter fortement la taille du dépôt ;
* ralentir `clone`, `pull` et `fetch` ;
* alourdir l'historique Git ;
* poser des problèmes avec les limites de GitHub.

Pour les gros datasets et modèles, il est préférable d'utiliser des solutions comme :

* **DVC** ;
* **Git LFS** ;
* **S3 / stockage objet**.

---

# 📸 Preuves d'exécution

Les preuves demandées pour le TP sont :

| Preuve            | Vérification                                |
| ----------------- | ------------------------------------------- |
| `python train.py` | Pipeline exécuté avec succès                |
| `git status`      | Fichiers sources suivis et `models/` ignoré |
| GitHub            | Dépôt contenant les fichiers du projet      |

---

# 📚 Concepts MLOps

Ce TP met en pratique :

* scripts Python orientés production ;
* reproductibilité des environnements ;
* gestion des dépendances avec Conda ;
* versionnage avec Git ;
* collaboration via GitHub ;
* utilisation de `.gitignore` ;
* séparation entre code source et artefacts ML.

---

# 🔗 Ressources

* [Conda](https://docs.conda.io/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Scikit-learn](https://scikit-learn.org/)

---

# 📤 Publication sur GitHub

Après avoir créé ou modifié le `README.md` :

```bash
git add README.md
git commit -m "Add TP1 README"
git push
```

Pour envoyer tous les fichiers du projet :

```bash
git add .gitignore environment.yml train.py README.md
git commit -m "Complete TP1 MLOps project"
git push
```

---

## 👨‍💻 Auteur

**Mouhieddine Bouktib et Ahlam Assamsadi — 5IASD, Groupe G6**

Projet académique — EMSI
Module **51ASD — Déploiement d'IA**
Année **2026-2027**
