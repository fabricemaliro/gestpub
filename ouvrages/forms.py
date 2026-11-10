from django import forms
from .models import Article,Etiquette,Auteur,Profil,Parcelle,Ville
class villeForm(forms.ModelForm):
    class Meta:
        model=Ville
        fields="__all__"
        widgets={
            'designationville':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','autofocus':True}),
        
        }
        libels={'ville':'Nom ville'}
class articleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['titre','auteur','tag','code_livre','image_livre','contenu','ville','link_livre']
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','autofocus':True}),
            'auteur':forms.Select(attrs={'class':'form-control my-1','required':True}),
            'code_livre':forms.TextInput(attrs={'class':'form-control my-1','required':True}),
            'image_livre':forms.ClearableFileInput(attrs={'class': 'form-control my-1','required': True}),
            'tag':forms.SelectMultiple(attrs={'class':'form-control my-1','text-transform':'capitalize'}),
            'contenu':forms.Textarea(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','rows':3,'cols':1}),
            'ville':forms.Select(attrs={'class':'form-control my-1','required':True}),
            'link_livre':forms.TextInput(attrs={'class':'form-control my-1'}),
        }
        labels={
                'titre':'titre'
            }
        
class articleFormMod(forms.ModelForm):
    class Meta:
        model=Article
        fields=['titre','auteur','tag','contenu','code_livre','image_livre','ville','est_publie','link_livre']
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control my-1','text-transform':'capitalize','autofocus':True}),
            'auteur':forms.Select(attrs={'class':'form-control my-1'}),
            'tag':forms.SelectMultiple(attrs={'class':'form-control my-1','text-transform':'capitalize'}),
            'code_livre':forms.TextInput(attrs={'class':'form-control my-1'}),
            'image_livre':forms.ClearableFileInput(attrs={'class': 'form-control my-1'}),
            'contenu':forms.Textarea(attrs={'class':'form-control my-1','text-transform':'capitalize','rows':3,'cols':1}),
            'ville':forms.Select(attrs={'class':'form-control my-1'}),
            'est_publie':forms.CheckboxInput(attrs={'class':'form-control my-1'}),
             'link_livre':forms.TextInput(attrs={'class':'form-control my-1'}),
        }
        labels={
                'titre':'titre'
            }
class etiquetteForm(forms.ModelForm):
    class Meta:
        model=Etiquette
        fields="__all__"
        widgets={
            'tag':forms.TextInput(attrs={'class':'form-control','required':True,'text-transform':'capitalize','autofocus':True})
        }
        labels={
            'tag':"nom de l'etiquette"
        }
class auteurForm(forms.ModelForm):
    class Meta:
        model=Auteur
        fields="__all__"
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','autofocus':True}),
            'prenom':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize'}),
            'Genre':forms.Select(attrs={'class':'form-control my-1 md-2','required':True,'text-transform':'capitalize',}),
            'datenaiss':forms.TextInput(attrs={'class':'form-control my-1','required':True,'text-transform':'capitalize','type':'date'}),
            'ville':forms.Select(attrs={'class':'form-control my-1','text-transform':'capitalize'}),
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