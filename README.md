# TP1 — Au-delà du Notebook : Bonnes Pratiques Logiciels pour le MLOps

> **Cours :** 51ASD — Déploiement d'IA (2026-2027)
> **Sujet :** Mise en place d'un écosystème MLOps fondamental — scripts Python de production, environnements Conda isolés et versionnage Git/GitHub.
> **Auteur :** Mouhi
> **Filière :** 5IASD
> **Groupe :** Gx

---

## 🎯 Objectifs pédagogiques

Ce TP marque la transition entre le développement exploratoire en notebook et les bonnes pratiques du génie logiciel industriel.

Il pose les fondations des outils MLOps qui seront étudiés par la suite, notamment **DVC, MLflow, Docker et Kubernetes**.

| Objectif | Description                                                             |
| -------- | ----------------------------------------------------------------------- |
| **A**    | Migrer des notebooks vers des scripts Python de production dans VS Code |
| **B**    | Structurer les dépendances avec des environnements Conda isolés         |
| **C**    | Mettre en place un versionnage Git propre et un dépôt distant GitHub    |

---

## 🏗️ Architecture du projet

```text
tpl-git-env/
│
├── .gitignore              # Règles d'exclusion Git
├── environment.yml         # Définition de l'environnement Conda
├── train.py                # Pipeline d'entraînement
├── README.md               # Documentation du projet
│
└── models/                 # Ignoré par Git
    └── iris_model.pkl      # Modèle entraîné
```

---

## ⚙️ Environnement technique

### Technologies utilisées

* **Python :** 3.10
* **Gestionnaire d'environnement :** Conda
* **IDE :** Visual Studio Code
* **Versionnage :** Git
* **Dépôt distant :** GitHub

### Bibliothèques Python

* **pandas** — manipulation et analyse des données
* **scikit-learn** — entraînement et évaluation du modèle
* **ipykernel** — support Jupyter/VS Code
* **python-dotenv** — gestion des variables d'environnement

---

## 📦 Fichier `environment.yml`

L'environnement Conda est défini de manière déclarative afin de faciliter la reproductibilité du projet.

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

---

# 🚀 Installation et exécution

## 1. Cloner le dépôt

Depuis un terminal :

```bash
git clone https://github.com/Mouhi03/mlops-tp1-tutorial.git
cd mlops-tp1-tutorial
```

---

## 2. Créer l'environnement Conda

Créer l'environnement à partir du fichier `environment.yml` :

```bash
conda env create -f environment.yml
```

Puis l'activer :

```bash
conda activate mlops_base_env
```

Pour vérifier que le bon environnement est actif :

```bash
conda env list
```

L'environnement `mlops_base_env` doit apparaître comme environnement actif.

---

## 3. Lancer le pipeline d'entraînement

Exécuter le script Python :

```bash
python train.py
```

### Sortie attendue

```text
[MLOps Pipeline] Starting pipeline execution...
[MLOps Pipeline] Target model successfully cached! Score: 0.9667
```

Le modèle entraîné est ensuite sauvegardé dans :

```text
models/iris_model.pkl
```

> **Remarque :** le fichier `iris_model.pkl` est volontairement exclu du dépôt Git grâce au fichier `.gitignore`.

---

# 🧠 Description du pipeline `train.py`

Le script `train.py` encapsule l'ensemble du workflow Machine Learning dans une fonction principale :

```python
execute_pipeline()
```

Le pipeline est composé des étapes suivantes :

### 1. Chargement des données

Le dataset **Iris** est chargé grâce à :

```python
from sklearn.datasets import load_iris
```

Le dataset contient les caractéristiques de fleurs Iris ainsi que leurs classes.

---

### 2. Séparation des données

Les données sont séparées en deux ensembles :

* **80 %** pour l'entraînement
* **20 %** pour le test

Avec :

```python
random_state=42
```

L'utilisation d'un `random_state` permet d'obtenir des résultats reproductibles.

---

### 3. Entraînement du modèle

Le modèle utilisé est un :

```text
RandomForestClassifier
```

avec :

```python
n_estimators=100
```

Le modèle est entraîné sur les données d'entraînement.

---

### 4. Évaluation

Une fois entraîné, le modèle est évalué sur les données de test.

Le score obtenu est affiché dans la console.

Exemple :

```text
Score: 0.9667
```

Cela correspond à une précision d'environ **96,67 %** sur le jeu de test.

---

### 5. Persistance du modèle

Le modèle entraîné est sauvegardé grâce à la bibliothèque `pickle`.

Le fichier généré est :

```text
models/iris_model.pkl
```

Cette étape permet de réutiliser le modèle sans avoir besoin de le réentraîner.

---

## 🔒 Pourquoi utiliser `if __name__ == '__main__'` ?

Le script utilise :

```python
if __name__ == '__main__':
    execute_pipeline()
```

Cette structure garantit que le pipeline est exécuté uniquement lorsque `train.py` est lancé directement.

Par exemple :

```bash
python train.py
```

Si le fichier est importé depuis un autre script :

```python
import train
```

le pipeline ne sera pas automatiquement exécuté.

Cela rend le code plus facilement **réutilisable et testable**.

---

# 🚫 Fichier `.gitignore`

Le fichier `.gitignore` permet d'empêcher Git de suivre certains fichiers ou dossiers.

Voici le contenu utilisé dans ce projet :

```gitignore
# Environnements Python
.conda/
env/
venv/
__pycache__/
*.pyc

# Données et modèles binaires
data/
models/
*.pkl
*.h5

# Configuration locale VS Code
.vscode/
```

---

## 🔍 Pourquoi utiliser `.gitignore` ?

Les fichiers suivants ne doivent généralement pas être versionnés directement dans Git :

* environnements virtuels ;
* fichiers temporaires Python ;
* datasets volumineux ;
* modèles binaires ;
* fichiers de configuration locaux ;
* fichiers générés automatiquement.

Cela permet de conserver un dépôt **propre, léger et maintenable**.

---

# 📋 Réponses aux questions d'évaluation

## Question 1 — Git & `.gitignore`

### a) Pourquoi `models/iris_model.pkl` n'apparaît-il pas dans `git status` ?

Le fichier :

```text
models/iris_model.pkl
```

existe bien sur le disque après l'exécution du pipeline.

Cependant, Git applique les règles présentes dans `.gitignore`.

Le dossier `models/` est donc ignoré et son contenu n'est pas proposé comme fichier non suivi dans :

```bash
git status
```

Le fichier existe donc physiquement, mais Git l'ignore volontairement.

### b) Quelles sont les règles responsables ?

Les deux règles suivantes permettent d'ignorer le modèle :

```gitignore
models/
*.pkl
```

La première ignore tout le dossier `models/`.

La seconde ignore tous les fichiers ayant l'extension `.pkl`.

---

# Question 2 — Environnements reproductibles

## Pourquoi utiliser `environment.yml` ?

Un fichier `environment.yml` est préférable à une simple liste informelle de bibliothèques pour plusieurs raisons.

### 1. Reproductibilité

Le fichier décrit les dépendances nécessaires au projet et permet de recréer l'environnement sur une autre machine.

```bash
conda env create -f environment.yml
```

### 2. Automatisation

L'environnement peut être recréé automatiquement dans différents contextes :

* développement ;
* CI/CD ;
* serveurs ;
* conteneurs ;
* machines de production.

### 3. Cohérence de l'équipe

Tous les membres du projet utilisent la même définition d'environnement.

Le fichier devient une **source de vérité versionnée avec le code**.

### 4. Maintenance

Les dépendances sont centralisées dans un seul fichier, ce qui facilite leur modification et leur maintenance.

---

# Question 3 — Scripts Python orientés production

## Quels sont les avantages des scripts Python par rapport aux notebooks ?

### 1. Exécution automatisable

Un script peut être lancé directement depuis un terminal :

```bash
python train.py
```

Il peut également être intégré dans :

* CI/CD ;
* cron ;
* Airflow ;
* Docker ;
* pipelines MLOps ;
* systèmes de production.

Il n'est donc pas nécessaire d'exécuter manuellement plusieurs cellules dans un notebook.

### 2. Testabilité et versionnage

Un script Python correctement structuré permet :

* de créer des fonctions réutilisables ;
* d'écrire des tests unitaires ;
* de faciliter les revues de code ;
* d'obtenir des différences Git plus propres ;
* de mieux organiser le projet.

---

# Question 4 — Gros fichiers et repositories Git

## Pourquoi ne faut-il pas commiter un fichier CSV de 2 Go dans Git ?

Un fichier de plusieurs gigaoctets peut poser plusieurs problèmes.

### 1. Saturation du dépôt

Le fichier augmente considérablement la taille du dépôt et de son historique.

Chaque membre de l'équipe doit potentiellement télécharger une quantité importante de données.

### 2. Opérations Git plus lentes

Les opérations suivantes peuvent devenir beaucoup plus lourdes :

```bash
git clone
git fetch
git pull
git status
```

### 3. Nettoyage difficile

Supprimer le fichier du dernier commit ne suffit pas nécessairement à le supprimer de l'historique Git.

Des outils spécialisés peuvent être nécessaires, comme :

```text
git filter-repo
```

ou **BFG Repo-Cleaner**.

### 4. Limites de GitHub

GitHub impose des limites concernant la taille des fichiers et recommande des solutions adaptées aux fichiers volumineux.

### 5. Mauvaise pratique MLOps

Dans un projet Machine Learning, les datasets et les modèles volumineux doivent généralement être gérés avec des outils adaptés, par exemple :

* DVC ;
* Git LFS ;
* stockage objet ;
* Amazon S3 ;
* Google Cloud Storage.

Git doit principalement conserver le **code, la configuration et les métadonnées**, plutôt que les gros fichiers binaires.

---

# 📸 Preuves d'exécution

Les principales preuves de réalisation du TP sont les suivantes :

| Capture           | Description                                         |
| ----------------- | --------------------------------------------------- |
| `python train.py` | Exécution du pipeline et affichage du score         |
| `git status`      | Vérification des fichiers suivis et ignorés         |
| GitHub            | Présence des fichiers sources dans le dépôt distant |

### Exemple de sortie du pipeline

```text
[MLOps Pipeline] Starting pipeline execution...
[MLOps Pipeline] Target model successfully cached! Score: 0.9667
```

### Exemple de vérification Git

```bash
git status
```

Les fichiers sources suivants doivent apparaître :

```text
.gitignore
environment.yml
train.py
README.md
```

Le dossier :

```text
models/
```

ne doit pas apparaître comme fichier non suivi.

---

# 🧪 Vérifications supplémentaires

Pour vérifier qu'un fichier est bien ignoré par Git :

```bash
git check-ignore -v models/iris_model.pkl
```

Git doit afficher la règle responsable de l'exclusion.

Cette commande est particulièrement utile pour comprendre le fonctionnement de `.gitignore`.

---

# 🌐 Dépôt GitHub

Le projet est disponible sur GitHub :

**Repository :** `mlops-tp1-tutorial`

**GitHub :**
https://github.com/Mouhi03/mlops-tp1-tutorial

---

# 📂 Structure finale du projet

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

> Le dossier `models/` est généré localement après l'exécution du pipeline mais n'est pas versionné dans Git.

---

# 📚 Concepts MLOps couverts

Ce TP permet de mettre en pratique plusieurs concepts fondamentaux du MLOps :

* séparation entre exploration et production ;
* transformation d'un notebook en script Python ;
* création d'un pipeline d'entraînement ;
* reproductibilité des environnements ;
* utilisation de Conda ;
* gestion déclarative des dépendances ;
* contrôle de version avec Git ;
* collaboration avec GitHub ;
* gestion des fichiers ignorés ;
* bonnes pratiques concernant les datasets et modèles ;
* préparation aux outils MLOps avancés.

---

# 🔗 Liens utiles

* [Documentation Conda](https://docs.conda.io/)
* [Git SCM](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Scikit-learn](https://scikit-learn.org/)

---

# 📝 Licence

Projet académique réalisé dans le cadre du module :

**51ASD — Déploiement d'IA**

**EMSI — Filière 5IASD**

**Année universitaire : 2026-2027**

---

# 👨‍💻 Auteur

**Mouhi**
Filière **5IASD**
Groupe **Gx**

---

## 🚀 Commandes Git utilisées

Après avoir créé ou modifié le `README.md` :

```bash
git status
```

Ajouter le fichier :

```bash
git add README.md
```

Créer le commit :

```bash
git commit -m "Add comprehensive README describing TP1 MLOps project"
```

Envoyer les modifications sur GitHub :

```bash
git push
```

Pour ajouter tous les fichiers sources du projet en une seule fois :

```bash
git add .gitignore environment.yml train.py README.md
git commit -m "Complete TP1 MLOps project"
git push
```

---

## ✅ TP1 terminé

Le projet met en place les fondations d'un environnement MLOps propre :

**Code → Environnement → Git → GitHub → Reproductibilité**

Ces bases pourront ensuite être utilisées pour intégrer des outils plus avancés tels que **DVC, MLflow, Docker et Kubernetes**.
