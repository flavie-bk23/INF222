# INF222
PRESENTATION DU PROJET(TP DE 222)
Flavie - Django Blog Project


[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.2-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)

 Description

**Flavie** est un projet web développé avec Django 5.2, configuré pour fonctionner avec ASGI et WSGI, et intégrant Django REST Framework pour la création d’API.  

Le projet inclut :

                - Une application `blog` pour gérer des articles
                - Routes API REST via Django REST Framework
                - Support ASGI pour un déploiement asynchrone moderne
                - Une base solide pour créer des applications web scalables et maintenables


  Technologies utilisées
 

                  - Python 3.x
                  - Django 5.2
                  - Django REST Framework
                  - SQLite (base de données développement)
                  - ASGI & WSGI (serveurs)
                  - HTML / Templates Django


  Configuration du projet

 

 Fichiers principaux

 

### 1. `settings.py`
Contient les paramètres principaux du projet :

                  - Gestion de la base de données SQLite
                  - Applications installées (`blog`, `rest_framework`, `django.contrib.*`)
                  - Middleware et templates
                  - Configuration des fichiers statiques et timezone
                  - Clé secrète et mode debug pour développement

 ### 2. `urls.py`
Gère le routage des URL :

python

              from django.contrib import admin
              from django.urls import path, include
              from . import views
              from rest_framework.routers import DefaultRouter
              from blog.views import ArticleViewSet

                

  Flavie - DJANGO BLOG PROJET


[![Python](https://img.shields.io/badge/python-3.x-blue)]()
[![Django](https://img.shields.io/badge/django-5.2-green)]()
[![DRF](https://img.shields.io/badge/DRF-3.14-yellowgreen)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

Technologies utilisées

Liste claire de tout ce qui est utilisé : Python, Django, DRF, SQLite, template

          - Python 3.x
          - Django 5.2
          - Django REST Framework
          - SQLite
          - ASGI & WSGI

### Installation et configuration


flavie/
│── flavie/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│     
Flavie - Django Blog Project
    [![Python](https://img.shields.io/badge/python-3.x-blue)]()
    [![Django](https://img.shields.io/badge/django-5.2-green)]()
    [![DRF](https://img.shields.io/badge/DRF-3.14-yellowgreen)]()
    [![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

                    Description du projet

Technologies utilisées

    - Python 3.x
    - Django 5.2
    - Django REST Framework
    - SQLite
    - ASGI & WSGI

Installation et configuration

    flavie/
    │── flavie/
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    │── blog/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── views.py
    │   ├── serializers.py
    │   └── urls.py
    │
    │── manage.py
    │── templates/
    │   └── base.html

Fonctionnalités du blog

    Ce que le projet peut faire :

        Gestion d’articles via admin

        API REST pour articles

        Page d’accueil (base.html)

        Endpoints pour /blog/ et /api/articles/
    

Perspectives / améliorations

    

        ### Authentification utilisateur

        Frontend React / Vue

        Notifications temps réel

        Déploiement cloud




│── blog/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
│── manage.py
│── templates/
│   └── base.html


### Fonctionnalités du blog



Ce que le projet peut faire :

Gestion d’articles via admin
API REST pour articles
Page d’accueil (base.html)
Endpoints pour /blog/ et /api/articles/
Comment tester l’API
Exemple de commandes curl ou Postman
Permet de montrer que le projet est fonctionnel
