# Application de Collection de Films
(english below)

## Introduction
Ce projet vise à créer une application web pour gérer une collection de films. Les utilisateurs peuvent ajouter de nouveaux films, modifier les détails tels que les notes et les avis, et supprimer des films de la collection.

## Fonctionnalités
- Affiche une liste de films triés par note.
- Permet aux utilisateurs d'ajouter de nouveaux films avec des détails tels que le titre et l'année.
- Fournit une fonctionnalité de modification pour mettre à jour les notes et les avis des films.
- Prend en charge la suppression de films de la collection.

## Technologies Utilisées
- Python 3.x
- Flask : Framework web pour les applications Python.
- Flask-Bootstrap : Intégration des fonctionnalités Bootstrap dans les modèles Flask.
- Flask-WTF, WTForms : Gestion des formulaires dans l'application.
- SQLAlchemy : Mappage objet-relationnel (ORM) pour la gestion de la base de données.
- SQLite : Base de données SQL légère pour stocker les informations sur les films.

## Installation et Configuration
1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Clonez ou téléchargez les fichiers du projet à partir du dépôt.
3. Installez les packages requis à l'aide de pip et du fichier `requirements.txt` : `pip install -r requirements.txt`.
4. Configurez les variables d'environnement nécessaires :
   - `secret_key` : Clé secrète Flask pour des sessions sécurisées.
   - `api_key` : Clé API pour l'API The Movie Database (TMDB).
5. Exécutez le script `main.py` pour démarrer l'application Flask.

## Structure du Projet
- `main.py` : Script principal contenant la logique de l'application Flask.
- `templates/` : Répertoire pour les modèles HTML.
    - `index.html` : Page d'accueil affichant la liste des films.
    - `add.html` : Formulaire pour ajouter de nouveaux films.
    - `edit.html` : Formulaire pour modifier les détails des films.
- `static/` : Répertoire pour les fichiers statiques (CSS, images).
- `movies-collection.db` : Fichier de base de données SQLite pour stocker les informations sur les films.
- `requirements.txt` : Liste des packages Python requis.

## Utilisation
1. Accédez à l'application Flask via votre navigateur web.
2. Sur la page d'accueil, visualisez la liste des films avec leurs notes et avis.
3. Utilisez le bouton "Ajouter un Film" pour ajouter de nouveaux films à la collection.
4. Cliquez sur les titres des films pour modifier leurs notes et avis.
5. Utilisez l'option de suppression pour retirer des films de la collection.

## Captures d'écran
### index.html
![index.html](https://github.com/marionrobert/MovieProject/assets/107509668/8d9ae2d8-85f4-42bb-bb7d-8443efcd2417)

## Remarques
- Assurez-vous de configurer les variables d'environnement
- Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) d'Angela Yu sur la plateforme Udemy.

---
---

# Movie Collection Application

## Introduction
This project aims to create a web application for managing a collection of movies. Users can add new movies, edit movie details such as ratings and reviews, and delete movies from the collection.

## Features
- Displays a list of movies sorted by rating.
- Allows users to add new movies with details such as title and year.
- Provides editing functionality for updating movie ratings and reviews.
- Supports deletion of movies from the collection.

## Technologies Used
- Python 3.x
- Flask: Web framework for Python applications.
- Flask-Bootstrap: Integration of Bootstrap features into Flask templates.
- Flask-WTF, WTForms: Handling forms in the application.
- SQLAlchemy: Object-Relational Mapping (ORM) for database management.
- SQLite: Lightweight SQL database for storing movie information.

## Installation and Configuration
1. Make sure you have Python 3.x installed on your system.
2. Clone or download the project files from the repository.
3. Install the required packages using pip and the `requirements.txt` file: `pip install -r requirements.txt`.
4. Set up the necessary environment variables:
   - `secret_key`: Flask secret key for secure sessions.
   - `api_key`: API key for The Movie Database (TMDB) API.
5. Run the `main.py` script to start the Flask application.

## Project Structure
- `main.py`: Main script containing Flask application logic.
- `templates/`: Directory for HTML templates.
    - `index.html`: Homepage displaying the list of movies.
    - `add.html`: Form for adding new movies.
    - `edit.html`: Form for editing movie details.
- `static/`: Directory for static files (CSS, images).
- `movies-collection.db`: SQLite database file for storing movie information.
- `requirements.txt`: List of required Python packages.

## Usage
1. Access the Flask application through your web browser.
2. On the homepage, view the list of movies with their ratings and reviews.
3. Use the "Add Movie" button to add new movies to the collection.
4. Click on movie titles to edit their ratings and reviews.
5. Use the delete option to remove movies from the collection.

## Screenshots
### index.html
![index.html](https://github.com/marionrobert/MovieProject/assets/107509668/8d9ae2d8-85f4-42bb-bb7d-8443efcd2417)


## Notes
- Ensure to configure environment variables
- This project was completed as part of the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) course by Angela Yu on the Udemy platform.
