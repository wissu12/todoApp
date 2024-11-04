# Gestion des Tâches - toDoApp

Bienvenue dans le projet toDoApp ! Cette application de gestion de tâches est conçue pour vous aider à organiser et suivre vos tâches facilement. Que vous soyez en mode À faire, En cours, ou Terminé, cette application vous permet de gérer vos tâches de manière fluide et intuitive.Gestion des Tâches - toDoApp
Bienvenue dans le projet toDoApp ! Cette application de gestion de tâches est conçue pour vous aider à organiser et suivre vos tâches facilement. Que vous soyez en mode À faire, En cours, ou Terminé, cette application vous permet de gérer vos tâches de manière fluide et intuitive.


## Pourquoi ce choix de projet ?
J’ai choisi de développer une application de gestion de tâches, toDoApp, pour répondre aux critères du test technique. Ce projet est conçu pour offrir une expérience utilisateur intuitive et engageante, tout en répondant à des besoins courants d’organisation personnelle et professionnelle.
L’organisation des tâches est un besoin universel, et j’ai pensé que créer une application pratique pour cela permettrait de mettre en valeur mes compétences tant en développement back-end qu’en front-end. En utilisant React.js pour le front-end et Django pour le back-end, j’ai pu structurer une API REST qui permet de synchroniser les tâches et de gérer l'inscription,login et logout de manière fluide.

## Quelques Défis et Apprentissages

L’un des principaux défis de ce projet a été de travailler avec React pour la première fois. Étant habituée à utiliser Angular, j’ai trouvé ce changement stimulant, et cela m’a permis de challenge myself pour découvrir une nouvelle technologie en un temps très court. J’ai vraiment pris plaisir à me familiariser avec React et à intégrer les spécificités de sa logique et de ses composants dans le projet. Cette expérience a été enrichissante, car elle m'a permis d'élargir mes compétences en développement front-end et de m'adapter rapidement à un nouveau framework.

📖 Fonctionnalités Principales

### Page d'Accueil et Authentification :

Lorsqu'un utilisateur accède à http://localhost:3000, il est d'abord accueilli par une page d'accueil offrant la possibilité de se connecter ou de créer un compte.
Si l'utilisateur ne possède pas de compte, il peut facilement en créer un via le bouton Sign Up. S'il est déjà enregistré, il peut directement se connecter avec ses identifiants via Login.

### Interface de Gestion des Tâches :

Une fois connecté, l’utilisateur accède à une interface affichant la liste des tâches. Celles-ci sont classées en trois catégories : À faire, En cours, et Terminées, offrant une vue d’ensemble claire de toutes les tâches.

### Ajouter une Nouvelle Tâche :

Les utilisateurs peuvent ajouter une tâche en entrant un titre et une description. Les champs Date de début et Date de fin seront automatiquement calculés selon l’état de progression de la tâche.

### Changer l'État d'une Tâche :

Lorsqu'une tâche est dans l'état À faire, un bouton Start est disponible pour démarrer la tâche.
En cliquant sur Start, la date de début est automatiquement enregistrée, et la tâche passe à l'état En cours. Le bouton Start disparaît, et le bouton End s'affiche.
En cliquant sur End, la date de fin est automatiquement enregistrée, et l'état de la tâche passe à Terminée.

### Modifier les Informations d'une Tâche :

Les utilisateurs peuvent modifier le titre et la description d'une tâche. Cependant, les champs État, Date de début, et Date de fin sont automatiquement gérés par l'application en fonction de l'avancement de la tâche.
Après la modification, l'utilisateur est redirigé vers la liste des tâches avec les mises à jour visibles instantanément.

### Suppression de Tâche avec Confirmation :

Pour éviter les suppressions accidentelles, une confirmation est demandée avant de supprimer définitivement une tâche. Cette mesure permet de prévenir la perte de données importantes et offre à l'utilisateur une possibilité de retour en arrière.

### Déconnexion Sécurisée :

Une fois que l'utilisateur a terminé son travail, il peut se déconnecter en toute sécurité. Cette action le ramène à la page de connexion, garantissant que les informations restent privées et sécurisées.

## Conception 

![MCD](https://github.com/user-attachments/assets/0261d9d3-6636-47c8-9212-1a91a89db573)

Pour la conception de notre base de données, nous avons défini deux entités principales : User et Task.

L’entité User représente les utilisateurs de l’application et contient les attributs suivants :

id : identifiant unique de l’utilisateur.
username : nom d’utilisateur unique.
password : mot de passe de l’utilisateur, sécurisé.
L’entité Task représente les tâches créées par les utilisateurs et comporte les attributs suivants :

id : identifiant unique de la tâche.
title : titre de la tâche.
description : description détaillée de la tâche.
start_date : date de début de la tâche.
end_date : date de fin de la tâche.
status : état de la tâche (à faire, en cours, terminée).
user_id : identifiant de l’utilisateur associé à la tâche, qui établit la relation avec l’entité User.
La relation entre User et Task est de type un-à-plusieurs. Chaque utilisateur peut avoir une ou plusieurs tâches, mais une tâche est liée à un seul utilisateur. Cette relation est représentée par la clé étrangère user_id dans l’entité Task, qui fait référence à l’attribut id de l’entité User.


📸 Aperçu de l’Interface Utilisateur
### Page d’Accueil

![Page d'accueil](https://github.com/user-attachments/assets/570aa601-d954-40aa-9a0d-09aeee0f7cdc)

### Page d'inscription

![Signup](https://github.com/user-attachments/assets/9773aab4-da3a-4b6c-8cee-4dbf8538c37a)


### Page de connexion

![login](https://github.com/user-attachments/assets/05953b3f-da08-4deb-9c3f-f20a259907d9)


### Liste des Tâches avec États

![Liste des taches](https://github.com/user-attachments/assets/f2f90555-f1fb-44c6-9423-5b2fd346f1c7)


### Ajout de Nouvelle Tâche

![Add task](https://github.com/user-attachments/assets/82076981-7df0-496d-8ae1-dc221d653021)


### Modification d’une Tâche

![edit task](https://github.com/user-attachments/assets/f22b9fd5-3148-4486-9771-ad32eb1c66ef)


### Suppression d’une Tâche avec Confirmation

![delete task](https://github.com/user-attachments/assets/784800aa-af72-406e-ac42-7195106f62a1)


🛠️ Technologies Utilisées
Front-end : React.js
Back-end : API REST Django
Base de Données : SQLite

