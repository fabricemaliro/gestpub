from django import forms
from .models import Article,Etiquette,Auteur,Profil,Parcelle

class articleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['titre','ecrivains','tag','contenu']
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','autofocus':True}),
            'ecrivains':forms.Select(attrs={'class':'form-control my-1','required':True}),
            'tag':forms.SelectMultiple(attrs={'class':'form-control my-1','text-transform':'capitalize'}),
            'contenu':forms.Textarea(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','rows':3,'cols':1})
        }
        labels={
                'titre':'titre'
            }
class etiquetteForm(forms.ModelForm):
    class Meta:
        model=Etiquette
        fields="__all__"
        widgets={
            'tag':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','autofocus':True})
        }
        labels={
                #'tag':'Etique des livres'
            }
class auteurForm(forms.ModelForm):
    class Meta:
        model=Auteur
        fields="__all__"
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','autofocus':True}),
            'prenom':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize'}),
            'tags':forms.Select(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize'}),
            'datenaiss':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','type':'date'}),
            'Genre':forms.Select(attrs={'class':'form-control my-1 md-2','required':True,'text-transform':'capitalize',})
        }
        labels={
            'noms':"nom de l'auteur"
        }

class profilForm(forms.ModelForm):
    class Meta:
        model=Profil
        fields="__all__"
        widgets={
            'user':forms.Select(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','autofocus':True}),
            'bibiographie':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize'}),
            'site_web':forms.TextInput(attrs={'class':'form-control my-1'}),
            'Genre':forms.Select(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize'})
        }
        labels={
            'user':"Utilisateur"
        }
class ParcelleForm(forms.ModelForm):
    class Meta:
        model = Parcelle
        fields = '__all__'