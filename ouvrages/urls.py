from django.urls import path # IMPORT DES PATH
from.import views #LIAISON URL ET VIEWS DE L'APPLICATION blog


urlpatterns = [
    path('', views.home,name='home'),
    path('ouvrage/save/', views.enregistrer_livre,name='enregistrer_livre'),
    path('carte/', views.carte,name='carte'),
    path('ajout_parcelle/', views.ajouter_parcelle,name='ajouter_parcelle'),
    path('ajout_tag/', views.enregistrer_tag,name='tag'),
    path('auteur/Ajout/', views.ajouter_auteur,name='ajouter_auteur'),
    path('table/', views.table,name='table'),
    path('liste/auteurs/', views.liste_auteur,name='liste_auteur'),
    path('liste/ville/', views.ajout_ville,name='liste_ville'),
    path('auteur/modifier/<int:id>/', views.modif_auteur,name='edit_auteur'),
    path('ville/modifier/<int:id>/', views.modifier_ville,name='edit_ville'),
    path('etiquette/modifier/<int:id>/', views.modifier_etiquette,name='edit_etiquette'),
    path('ouvrage/liste/', views.liste_livre,name='liste_article'),
    path('ouvrage/edit/', views.editer_article,name='editer_article'),
    path('Article/modif/<int:id>/', views.modif_livre,name='edit_art'),
    path('livre/detail/<int:id>/', views.detail_livre,name='detail_art'),
    path('livre/rechercher/', views.rechercher_livre,name='rechercher_livre'),
    path('livre/suppression/<int:id>/', views.supprimer_livre,name='suppression_livre'),
    path('livre/imprimer/<int:id>/', views.imprimer_livre,name='impression_livre'),
    path('livre/graphe/', views.graphe,name='graphe'),
    path('dog/', views.dog,name='inheritance'),
]


