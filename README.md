CultureQuiz

Description

CultureQuiz est une application interactive de quiz en français conçue pour tester vos connaissances générales tout en s'amusant. Le projet est basé sur une interface graphique conviviale, construite avec Tkinter, et propose des questions classées par niveaux de difficulté : facile, moyen et difficile.

Fonctionnalités

Interface utilisateur simple et intuitive : Navigation facile pour sélectionner les niveaux et répondre aux questions.

Trois niveaux de difficulté : Adapté pour tous les âges et niveaux de connaissances.

Score en temps réel : Affichage du score pour suivre votre progression.

Questions aléatoires : Une nouvelle sélection de questions à chaque partie.

Prérequis

Python 3.7 ou une version ultérieure

Bibliothèque Tkinter (intégrée avec Python standard)

Installation

Clonez ce dépôt sur votre machine locale :

git clone https://github.com/Deniz09OK/CultureQuiz

Placez les fichiers suivants dans le même répertoire :

quizz.py : Le script principal de l'application.

questions.json : Le fichier contenant les questions et réponses.

Assurez-vous d'avoir Python installé sur votre système.

Utilisation

Exécutez le fichier principal :

python quizz.py

Une fenêtre graphique s'ouvrira. Choisissez un niveau de difficulté pour commencer.

Répondez aux questions en sélectionnant l'option correcte.

Consultez votre score à la fin du quiz et rejouez si vous le souhaitez.

Structure des fichiers

quizz.py : Contient le code de l'application.

questions.json : Base de données des questions organisées par niveau (« facile », « moyen », « difficile »).

Exemple de contenu du fichier questions.json

{
    "facile": [
        {
            "question": "Quelle est la capitale de la France ?",
            "options": ["Paris", "Lyon", "Marseille", "Nice"],
            "answer": "Paris"
        }
    ]
}

Contribution

Les contributions sont les bienvenues ! Pour contribuer :

Forkez le projet.

Créez une nouvelle branche :

git checkout -b feature/nom_de_la_fonctionnalite

Faites vos modifications et commitez-les :

git commit -m "Description des modifications"

Poussez vos modifications :

git push origin feature/nom_de_la_fonctionnalite

Ouvrez une Pull Request.

Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Auteur

Projet réalisé par [Votre Nom/Equipe].

Amusez-vous bien avec CultureQuiz !

