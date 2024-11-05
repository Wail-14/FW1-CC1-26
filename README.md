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
   # Exemple de test dans le shell
   from collec_management.models import Collec
   from datetime import date
   collection = Collec.objects.create(
    title="Ma première collection",
    description="Description de test",
    date=date.today()
    )
    collection.save()
   print(Collec.objects.all())