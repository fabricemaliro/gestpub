from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator



                            #RELATION MANY-TO-MANY
class Etiquette(models.Model):
    tags=models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.tags
class Meta:
    Ordering=['tags']
    verbose_name='Etiquette'
    verbose_name_plural='Etiquettes'

                            #PREMIER MODELE RELATION FOREIGNKEY
class Ville(models.Model):
    designationville=models.CharField(max_length=50)

    def __str__(self):
        return self.designationville
class Meta:
    Ordering=['ville']
    verbose_name='Ville'
    verbose_name_plural='Villes'
    
    
class Auteur(models.Model):
    GenreListe=(
        ('F',"Feminin"),
        ('M',"Masculin"))
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    datenaiss=models.DateField()
    Genre=models.CharField(max_length=1,choices=GenreListe)
    ville=models.ForeignKey(to=Ville, on_delete=models.SET_NULL,null=True, related_name='ville_autre')

    def __str__(self):
        return f"{self.nom} {self.prenom}"
class Meta:
    Ordering=['auteur']
    verbose_name='Auteur'
    verbose_name_plural='Auteurs'

  
    
                        # MODELE ARTICLE
class Article(models.Model):
    titre=models.CharField(max_length=50)
           #RELATION MANY TO MANY
    tag=models.ManyToManyField(
        to=Etiquette,
        blank=True, related_name='tag'
    )
    auteur=models.ForeignKey(
        to=Auteur,on_delete=models.SET_NULL,null=True,related_name='auteur'
    )
    ville=models.ForeignKey(to=Ville, on_delete=models.SET_NULL,null=True, related_name='ville')
    date_publication=models.DateField(auto_now_add=True)
    code_livre=models.CharField(max_length=15,null=True,unique=True,validators=[MinLengthValidator(5)])
    image_livre=models.ImageField(upload_to='cover_pict_liv/',null=True, blank=True)
    contenu=models.TextField()
    est_publie=models.BooleanField(default=False)
    nb_vues=models.PositiveIntegerField(default=0)
    link_livre=models.URLField(max_length=200,null=True)

    def __str__(self):
        return self.titre
#GENERATION CODE BAR
                            # def save(self, *args, **kwargs):

                            #     is_new = self.pk is None

                            #     # Liste des champs à mettre à jour
                            #     update_fields = []

                            #     # Initialisation
                            #     old = None
                            #     old_code_livre = None

                            # # Récupération ancienne valeur
                            #     if not is_new:
                            #         old = self.__class__.objects.filter(pk=self.pk).first()

                            #     if old:
                            #         old_code_livre = old.code_livre

                            # # Sauvegarde normale
                            #     super().save(*args, **kwargs)

                            #     # Génération code barre
                            #     if is_new or old_code_livre != self.code_livre:

                            #         contenu = f"{self.id}{self.code_livre}"

                            #         barcode_img = Code128(
                            #             str(contenu),
                            #             writer=ImageWriter()
                            #         )

                            #         buffer_barcode = BytesIO()
                            #         barcode_img.write(buffer_barcode)
                            #         buffer_barcode.seek(0)

                            #         self.code_barre.save(
                            #             f'article_{self.id}.png',
                            #             File(buffer_barcode),
                            #             save=False
                            #         )

                            #         update_fields.append('code_barre')

                            #     # Génération QR code
                            #     if not self.qr_code:
                            #         #data = f"http://127.0.0.1:8000/article/{self.id}/"
                            #         data = self.link_livre

                            #         qr_img = qrcode.make(data)

                            #         buffer_qr = BytesIO()
                            #         qr_img.save(buffer_qr, format='PNG')
                            #         buffer_qr.seek(0)

                            #         self.qr_code.save(
                            #             f'article_{self.id}.png',
                            #             File(buffer_qr),
                            #             save=False
                            #         )

                            #         update_fields.append('qr_code')

                            #     # Sauvegarde finale
                            #     if update_fields:
                            #         super().save(update_fields=update_fields)
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
