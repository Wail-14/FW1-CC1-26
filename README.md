## Membres du Groupe

- **Prénom Nom** - wail.demnati@etu.univ-orleans.fr
- **Prénom Nom** - inouk.buigne@etu.univ-orleans.fr
- **Prénom Nom** - tolunay.akkaya@etu.univ-orleans.fr
- **Prénom Nom** - achraf.attioui@etu.univ-orleans.fr

## Commandes Django Utilisées pour la Question 1

1. Création du projet : `django-admin startproject cc .`
2. Création de l'application : `python manage.py startapp collec_management`
3. Appliquer les migrations : `python manage.py migrate`
4. Démarrer le serveur : `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Django Utilisées pour la Question 2

1. Création de la vue **about** dans `collec_management/views.py`.
2. Mise à jour des URL dans `cc/urls.py` et creation de `collec_management/urls.py` pour inclure la route `about/`.
   - Commande pour `cc/urls.py` : `path('', include('collec_management.urls'))`,
   - commande pour `collec_management/urls.py`  : `path('about/', views.about, name='about')`
3. Création du template HTML pour la page de présentation dans `collec_management/templates/about.html`.
4. Vérification et lancement du serveur pour voir la page about : `python manage.py runserver 0.0.0.0:8000 &` avec le lien `http://localhost:8088/about/`

## Commandes Django Utilisées pour la Question 3

1. Générer les fichiers de migration avec `python manage.py makemigrations` pour les changements de `models.py`
2. Appliquer la migration avec `python manage.py migrate`
3. Ouvrir le Python Shell `python manage.py shell`

   #### Exemple de test dans le shell
    ```python
      from collec_management.models import Collec
      from datetime import date
      collection = Collec.objects.create(
      title="Ma première collection",
      description="Description de test",
      date=date.today()
      )
      collection.save()
      print(Collec.objects.all())

## Commandes Django Utilisées pour la Question 4

   1. Création du répertoire `collec_management/fixtures` avec `mkdir collec_management/fixtures`
   2. Ajout de 12 collections en exécutant `python manage.py shell`

      #### Exemple d'ajout de deux collections :
      ```python
         from collec_management.models import Collec
         from datetime import date

         collections = [
            Collec(title="Collection de Livres Anciens", description="Une collection d'ouvrages rares du XIXe siècle.", date=date(2022, 5, 10)),
            Collec(title="Vinyles Classiques", description="Disques vinyles de musique classique.", date=date(2023, 3, 15)),
         ]

         # Enregistrer chaque collection dans la base de données
         for collec in collections:
            collec.save()
   3. Génération d’un fichier examples.json avec dumpdata (le paramètre --indent 4 permet de formater avec des espacements) `python manage.py dumpdata collec_management.Collec --indent 4 > collec_management/fixtures/examples.json`
   4. on peut maintenant charger ces données avec `python manage.py loaddata examples`   

## Commandes Django Utilisées pour la Question 5

   1. Création de la vue **collection** dans `collec_management/views.py`.
   2. Définir l'URL dans `collec_management/urls.py` pour accéder à la vue avec `path("collection/<int:n>", views.collection, name ="collection")`
   3. Création de la template `collection.html` dans le répertoire `collec_management/templates/`


 ## Commandes Django Utilisées pour la Question 6

   1. Création de la vue **collec_list** dans `collec_management/views.py`.
   2. Définir l'URL dans `collec_management/urls.py` pour accéder à la vue avec `path ("all", views.colleclist , name ="colleclist"),`
   3. Création de la template `collec_list.html` dans le répertoire `collec_management/templates/`


 ## Commandes Django Utilisées pour la Question 7

   1. Création du fichier forms.py dans le repertoire `collec_management/` 
   2. Création de la vue **new_collec** dans `collec_management/views.py`.
   3. Définir l'URL dans `collec_management/urls.py` pour accéder à la vue avec `path('new', views.new_collec, name='new_collec'),`
   4. Création de la template `new_collec.html` dans le répertoire `collec_management/templates/`
