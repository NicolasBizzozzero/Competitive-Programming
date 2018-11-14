# HuaweiHackaton
## Liens utiles
* http://bit.ly/EmailHackHuawei18
* https://drivendata.github.io/cookiecutter-data-science/#directory-structure


## TODO
* Ecriture d'un tuto
** pytorch avancé
** git ?
* Dév d'une librairie
** Outils de pré-traitement TALN (filtrage de caractères, mise sous N-gram (1, 2 et 3), jointure de caractères en un label, ...)
** Outils de manipulation dataframe (chargement, concaténation, swap, split, normalisation, dénormalisation, ...)
** Outils de manipulation tenseurs (chargement et sauvegarde modèles, ...)
** Clsses templates de création d'un NN, CNN et RNN (avec exmeples d'utilisation).
** Outils matplotlib simples (plot de courbes, ...)
* Recherche de papiers


## Conseils
* Chercher du biais dans les données dès le départ :
** Il arrive parfois que les données de test ne soient pas mélangées. Les exemples de chaque classes sont alors donnés par blocs. On pourra lisser nos résultats par fenêtre glissante pour améliorer nos scores.
* Chercher
* Chercher des features corrélées entre-elles (matrice de corrélation). Possiblement les réduire par la suite.
* Chercher les features corrélées aux labels (matrice de corrélation, encore).


## Organisation du repository
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py


## Message original
Message from Paul Ahanda:
I am contacting you as we are organising a 24H hackathon in Paris with Huawei on November 9-10th only for ParisTech, CentraleSupelec, ENS Paris-Saclay, Polytechnique, UPMC: 
The goal is to process more than 150k data points to identify malwares and propose an algorithm to improve cybersecurity. You’ll be given access to datasets, Huawei’s powerful cloud infrastructure, and mentoring will be provided by Huawei’s experts. 
I thought it could be a good assignment or experience for one of your classes. The winning team will get  a chance to discover Huawei’s Headquarters in China, meet Huawei’s top management and share the €10K prize pool, internship.
Do you think your students would find this interesting? If so, would you mind relaying the information? 
Info: http://bit.ly/EmailHackHuawei18
Thank you in advance for your time,
Looking forward to hearing from you.
Paul
