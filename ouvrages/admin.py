from django.contrib import admin
# LIAISON ADMINISTRATION DJANGO AUX FICHIER MODELES DANS ADMIN DE L'APPP
from.models import *# SELECTION DE TOUS LES MODELES
from.models import Auteur# SELECTION DE TOUS LES MODELES
from.models import Article# SELECTION DE TOUS LES MODELES
from.models import Profil# SELECTION DE TOUS LES MODELES
from.models import Parcelle# SELECTION DE TOUS LES MODELES
from.models import Etiquette # SELECTION DE TOUS LES MODELES



class parcelleGrille(admin.ModelAdmin):
    list_display=('proprietaire','coordonnees')
    
# ENREGISTREMENT MODELES DANS ADMIN DE L'APPP
class auteurGrille(admin.ModelAdmin):
    list_display=('nom','tags','prenom','datenaiss','Genre')


# ENREGISTREMENT MODELES DANS ADMIN DE L'APPP
class etiquetteGrille(admin.ModelAdmin):
    list_display=('tag',)

class articleGrille(admin.ModelAdmin):
    list_display=('titre','ecrivains','contenu','date_publication','est_publie','nb_vues')# COLONNES
    list_filter=('titre','ecrivains','contenu','date_publication','est_publie','nb_vues')# FILTRE
    search_fields=('titre','ecrivains','contenu','date_publication')# OUTIL DE RECHERCHE

class profilGrille(admin.ModelAdmin):
    list_display=('biographie','site_web','user')


admin.site.register(Auteur,auteurGrille)
admin.site.register(Article,articleGrille)
admin.site.register(Profil,profilGrille)
admin.site.register(Parcelle,parcelleGrille)
admin.site.register(Etiquette,etiquetteGrille)
