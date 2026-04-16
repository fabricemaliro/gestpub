from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import articleForm,ParcelleForm,etiquetteForm,auteurForm
import json

# Create your views here.
def editer_article(request):
    artic=Article.objects.all()
    form=articleForm()
    context={
        'article':artic,
        'form':form,
        }
    return render(request, "ajouter_ouvrage.html",context)

def liste_livre(request):
    artic=Article.objects.all()
    context={
        'article':artic,
        }
    return render(request, "liste_livres.html",context)

def home(request):
       return render(request, "accueil.html")

# ENREGISTREMENT LIVRE
def enregistrer_livre(request):
    message_suc=None
    if request.method == 'POST':  # VERIFICATION SI L'UTILISATEUR A CLIQUER SUR ENVOYER
        form = articleForm(request.POST)# RECUPERATION DES INFORM DU FORMULAIRE
        if form.is_valid():# VERIFICATION DES ERREURS SURVENUES 
            #form.save()# ENREGISTREMENT 
            article = form.save(commit=False) # ATTENTE D'ENREGISTREMENT
            article.save()                     
            form.save_m2m() # MANY TO MANY
            return redirect('liste_article')  #  évite double soumission
        else:
           message_suc='Echeck' 
    else:
       form=articleForm()
    context={
        'form':form,
        'message':message_suc
   }
    return render(request,'ajouter_livres.html',context)
#LISTE TAG
def liste_tag(request):
    tag=Etiquette.objects.all()
    context={
        'tag':tag
    }
    return render(request, 'liste_tag.html',context)
# ENREGISTREMENT TAG
def enregistrer_tag(request):
    tag=Etiquette.objects.all()
    if request.method == 'POST':  # VERIFICATION SI L'UTILISATEUR A CLIQUER SUR ENVOYER
         form =etiquetteForm(request.POST)# RECUPERATION DES INFORM DU FORMULAIRE
         if form. is_valid():# VERIFICATION DES ERREURS SURVENUES 
            form.save()# ENREGISTREMENT 
            return redirect('tag')  #  évite double soumission
    else:
         context={
             'form':etiquetteForm(),
             'tag':tag
         }
    return render(request,'liste_tag.html',context)
#-----------------------------------------------------------CARTE GEOLOCALISATION-----------------
def ajouter_parcelle(request):
    if request.method == 'POST':
        form = ParcelleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carte')
    else:
        form = ParcelleForm()
    return render(request, 'ajout_carte.html', {'form': form})


def carte(request):
    parcelles = Parcelle.objects.all()
    data = []
    for p in parcelles:
        data.append({
            'proprietaire': p.proprietaire,
            'coords': p.coordonnees
        })

    return render(request, 'coor.html', {
        'parcelles': json.dumps(data)
    })

#_________________________________AUTEUR_______________
def ajouter_auteur(request):
    message_=None
    if request.method=="POST":
        form=auteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_auteur')
    else:
        form=auteurForm()
    context={
        'form_aut':form,
        'message_':message_
    }
    return render(request,'ajouter_auteur.html',context)
    
def liste_auteur(request):
    list_aut=Auteur.objects.all()
    context={
        'list_aut':list_aut
    }
    return render(request, 'liste_auteurs.html',context)
