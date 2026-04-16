from django.db import models
from django.contrib.auth.models import User

                            #RELATION MANY-TO-MANY
class Etiquette(models.Model):
    tag=models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.tag
class Meta:
    Ordering=['tag']
    verbose_name='Etiquette'
    verbose_name_plural='Etiquettes'

                            #PREMIER MODELE RELATION FOREIGNKEY
class Auteur(models.Model):
    tags=models.ForeignKey(
        to=Etiquette,related_name='etiquette',default=0,on_delete=models.PROTECT
        )
    GenreListe=(
        ('F',"Feminin"),
        ('M',"Masculin"))
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    datenaiss=models.DateField()
    Genre=models.CharField(max_length=1,choices=GenreListe)
class Meta:
    Ordering=['tag']
    verbose_name='Auteur'
    verbose_name_plural='Auteurs'

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
                        # MODELE ARTICLE
class Article(models.Model):
   
       #RELATION MANY TO MANY
    tag=models.ManyToManyField(
        to=Etiquette,
        blank=True
    )
    ecrivains=models.ForeignKey(
        to=Auteur,default=0,on_delete=models.PROTECT
        )
    titre=models.CharField(max_length=50)
    date_publication=models.DateField(auto_now_add=True)
    contenu=models.TextField()
    est_publie=models.BooleanField(default=False)
    nb_vues=models.PositiveIntegerField(default=0)
class Meta:
    Ordering=['titre']
    verbose_name='Article'
    verbose_name_plural='Articles'
    
    def __str__(self):
        return self.auteur


                                        # MODELE PROFIL
#RELATION ONETOONE
class Profil(models.Model):
    # user ainsi oneToOnefield depuis model de djonago
    user=models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )
    biographie=models.TextField()
    site_web=models.URLField(null=True, blank=True)
class Meta:
    Ordering=['user']
    verbose_name='Profil'
    verbose_name_plural='Profil'
    def __str__(self):
        return self.user.username

class Parcelle(models.Model):
    proprietaire = models.CharField(max_length=100)
    coordonnees = models.JSONField()  # liste de coordonnées

    def __str__(self):
        return self.proprietaire
