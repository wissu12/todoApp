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

Une fois que l'utilisateur a terminé son travail, il peut se déconnecter en toute sécurité. Cette action le ramène à la page de connexion, garantissant que les informations restent privées et sécurisées.
