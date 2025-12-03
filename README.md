# Game Database

Ce projet permet de charger un fichier CSV contenant des données de jeux
vidéo et de l'insérer proprement dans une base de données relationnelle
via SQLAlchemy. L'objectif est de normaliser les données, d'éviter les
doublons, et de gérer toutes les relations (jeux, plateformes, éditeurs,
genres, années...).

## Fonctionnalités principales

### Initialisation de la base de données

La fonction `init_bdd_game()` crée automatiquement les entrées
obligatoires ("no publisher", "no genre", etc.) si elles n'existent pas
encore.

### Déduplication intelligente

Le système : 
- détecte et ignore les doublons dans le dataset, 
- vérifie les entrées déjà présentes en base, 
- crée uniquement ce qui manque.

### Création progressive des entités

Les tables sont remplies dans cet ordre pour les jeux: 
1. Publishers\ + Genres\ + Release_years\ + Platforms\
2. Games\
3. Games ↔ Platform (relation N-N)

Les tables sont remplies dans cet ordre pour les players: 
1. Countries\
2. Cities\ + Postal_codes\ + Street_types\
3. City_pc_corresps (relation N-N)
4. Addresses\ + Contacts\
5. Players\

La table de review qui fait le lien entre les deux : 
1. Reviews (relation N-N)

## Utilisation 
### Creation de la base de donnée
```bash
python main.py
```

## Licence

Projet interne -- libre d'utilisation.
