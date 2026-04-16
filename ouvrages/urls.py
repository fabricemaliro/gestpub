from django.urls import path # IMPORT DES PATH
from.import views #LIAISON URL ET VIEWS DE L'APPLICATION blog


urlpatterns = [
    path('', views.home,name='home'),
    path('ouvrage/liste/', views.liste_livre,name='liste_article'),
    path('ouvrage/edit/', views.editer_article,name='editer_article'),
    path('ouvrage/save/', views.enregistrer_livre,name='enregistrer_livre'),
    path('carte/', views.carte,name='carte'),
    path('ajout_parcelle/', views.ajouter_parcelle,name='ajouter_parcelle'),
    path('ajout_tag/', views.enregistrer_tag,name='tag'),
    path('liste/auteurs', views.liste_auteur,name='liste_auteur'),
    path('auteur/Ajout', views.ajouter_auteur,name='ajouter_auteur'),
]

