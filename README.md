# Gestion des Tâches - toDoApp

Bienvenue dans le projet toDoApp ! Cette application de gestion de tâches est conçue pour vous aider à organiser et suivre vos tâches facilement. Que vous soyez en mode À faire, En cours, ou Terminé, cette application vous permet de gérer vos tâches de manière fluide et intuitive.Gestion des Tâches - toDoApp
Bienvenue dans le projet toDoApp ! Cette application de gestion de tâches est conçue pour vous aider à organiser et suivre vos tâches facilement. Que vous soyez en mode À faire, En cours, ou Terminé, cette application vous permet de gérer vos tâches de manière fluide et intuitive.

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

Une fois que l'utilisateur a terminé son travail, il peut se déconnecter en toute sécurité. Cette action le ramène à![Signup](https://github.com/user-attachments/assets/f4ee879e-216f-4bd3-b73c-27f34b061f9c)
 la page de connexion, garantissant que les informations restent privées et sécurisées.

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
