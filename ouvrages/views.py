from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .forms import articleForm,ParcelleForm,etiquetteForm,auteurForm,articleFormMod,villeForm
import json
from django.contrib import messages #IMPORTATION DES MESSAGES ERREURS

#GESTION CODEBAR
import barcode
import qrcode
import base64

# GESTION CODEBAR
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from barcode import Code128
#########3-------------------------CODE BAR---------------------------

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
    article=Article.objects.count()
    auteur=Auteur.objects.count()
    ville=Ville.objects.count()
    etiquette=Etiquette.objects.count()
    context={
    'article':article,
    'auteur':auteur,
    'ville':ville,
    'categorie':etiquette,
    }
    return render(request, "index.html",context)

# OPERATIONS SUR LE LIVRE
def enregistrer_livre(request):
    message_suc=None
    if request.method == 'POST':  # VERIFICATION SI L'UTILISATEUR A CLIQUER SUR ENVOYER
        form = articleForm(request.POST, request.FILES)# RECUPERATION DES INFORM DU FORMULAIRE
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
        'formArtic':form,
        'message':message_suc
   }
    return render(request,'ajouter_livres.html',context)
#MODIFICATION DU LIVRE
def modif_livre(request,id):
    article=get_object_or_404(Article,id=id)
    form=articleFormMod(instance=article)
    if request.method=="POST":
        form=articleFormMod(request.POST,instance=article)
        if form.is_valid():
            form.save()
            messages.success(request,"la modification a reussie")
            return redirect('liste_article')
        else:
            messages.error(request,f'formulaire invalide:{form.errors.as_text}')
    else:
        context={
            'form':form,
            'article':article,
        }
    return render(request,'modifier_article.html',context)

# SELECTION LIVRE
def detail_livre(request, id):

    article = get_object_or_404(Article, id=id)
    #CODE SIMPLIFIER--------

     # Génération QRCode APPEL FONCTION GENERER_qrcode
    qr_code = generer_qrcode(
        article.link_livre
    )

    # Génération Code Barre APPEL FONCTION
    barcode = generer_barcode(
        f"{article.id}-{article.code_livre}"
    )
    # =========================
    # CONTEXT
    # =========================

    context = {
        'article': article,
        'qr_code': qr_code,
        'barcode': barcode,
    }
    return render(request,'detail_article.html',context)
#recherche livre
def rechercher_livre(request):

    motrecherche = request.GET.get('mot_cle', '')

    liv_recherche = Article.objects.prefetch_related(
        'tag',
        'auteur',
        'ville'
    ).filter(
        Q(tag__tags__icontains=motrecherche) |
        Q(auteur__nom__icontains=motrecherche) |
        Q(auteur__prenom__icontains=motrecherche) |
        Q(ville__designationville__icontains=motrecherche) |
        Q(titre__icontains=motrecherche) |
        Q(code_livre__icontains=motrecherche) |
        Q(contenu__icontains=motrecherche)
    ).distinct()

    context = {
        "mot_recherche": motrecherche,
        "article": liv_recherche,
        "nbretrouve": liv_recherche.count(),
    }

    return render(request, "tableau_livre.html", context)
                # def rechercher_livre(request):
            # if request.method=="GET":
            # # import time
            # # time.sleep(2)
            #     motrecherche=request.GET.get('mot_cle','')
            #     liv_recherche=Article.objects.prefetch_related('tag','auteur','ville')
            #     #liv_tag=Article.objects.prefetch_related('tag')
            #     #liv_tag=liv_tag.filter(Q(tag__tags__icontains=motrecherche))
            #     liv_recherche=liv_recherche.filter(
            #         Q(tag__tags__icontains=motrecherche)|
            #         Q(auteur__nom__icontains=motrecherche)|
            #         Q(auteur__prenom__icontains=motrecherche)|
            #         Q(ville__designationville__icontains=motrecherche)|
            #         Q(titre__icontains=motrecherche)|
            #         Q(code_livre__icontains=motrecherche)|
            #         Q(contenu__icontains=motrecherche)
            #         ).distinct()
            #     if liv_recherche.exists():
            #         context={
            #             "mot_recherche":motrecherche,
            #             "liv_recherche":liv_recherche,
            #             "article":liv_recherche,
            #         # 'article1':liv_tag,
            #             'nbretrouve':liv_recherche,}
            #         return render(request, "tableau_livre.html",context)
            #     else:
            #         context={
            #             "ech_mot_recherche":motrecherche,
            #             'liv_no_dispo':liv_recherche,
            #         }
            #         return render(request, "tableau_livre.html",context)
            #         #return HttpResponse(f"<p><p><b/>Aucun enregistrement trouvee correspondant au mot de recherche <mark><b style=color:red;> {context}</b></mark></b>")
            # else:
            #     context={
            #     "article":Article.object.all()
            #     }
            # return render(request,'liste_livres.html',context)

#------------------------------Supprimer livres-----------------------------
def supprimer_livre(request,id):
     # Récupère l'article ou retourne une erreur 404
    sup_article=get_object_or_404(Article,id=id)
    # Vérifie si la requête est en POST
    if request.method == "POST":
        sup_article.delete()
        return redirect('liste_article')
    context={
        'article':sup_article
    }
    return render(request,'suppression_livre.html',context)
#--------------------------------IMPRIMER---------------------------------------
def imprimer_livre(request,id):
     # Récupère l'article ou retourne une erreur 404
    imp_article=get_object_or_404(Article,id=id)
    
    # Génération QRCode APPEL FONCTION GENERER_qrcode
    qr_code = generer_qrcode(
        imp_article.link_livre
    )

    # Génération Code Barre APPEL FONCTION
    barcode = generer_barcode(
        f"{imp_article.id}-{imp_article.code_livre}"
    )
    context={
        'article':imp_article,
        'qr_code': qr_code,
        'barcode': barcode,
    }
    return render(request,'imprimer_livre.html',context)
#-----------------------------------------------------------------------UPDATE AUTEUR----------
def modif_auteur(request,id):
    auteur=get_object_or_404(Auteur,id=id)
    form=auteurForm(instance=auteur)
    if request.method=="POST":
        form=auteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
            messages.success(request,"la modification a reussie")
            return redirect('liste_auteur')
        else:
            messages.error(request,f'formulaire invalide:{form.errors.as_text}')
    else:
        context={
            'formAut':form,
            'auteur':auteur,
            'messages':messages.error(request,f'formulaire invalide:{form.errors.as_text}')
        }
    return render(request,'modifier_auteur.html',context)

#-----------------------------------------------------------------------UPDATE ETIQUETTE----------
def modifier_etiquette(request,id):
    etiquette=get_object_or_404(Etiquette,id=id)
    form=etiquetteForm(instance=etiquette)
    if request.method=="POST":
        form=etiquetteForm(request.POST or None,instance=etiquette)
        if form.is_valid():
            form.save()
            messages.success(request,"la modification a reussie")
            return redirect('tag')
        else:
            messages.error(request,f'formulaire invalide:{form.errors.as_text}')
    else:
        context={
            'formetiq':form,
            'etiquette':etiquette
        }
    return render(request,'modifier_etiquette.html',context)
#-----------------------------------------------------------------UPDATE VILLE---------
def modifier_ville(request,id):
    ville=get_object_or_404(Ville,id=id)  
    form=villeForm(instance=ville)  
    if request.method=="POST":
        form=villeForm(request.POST, instance=ville)  
        if form.is_valid():
            form.save()
            messages.success(request,"la modification a reussie")
            return redirect('liste_ville')
        else:
             messages.error(request,f'formulaire invalide:{form.errors.as_text}')
    else:
        context={
            'form':form,
            'ville':ville
        }
    return render(request,'modifier_ville.html',context)

def liste_tag(request):
    tag=Etiquette.objects.all()
    context={
        'tag':tag
    }
    return render(request, 'liste_tag.html',context)

def ajout_ville(request):
    form=villeForm()
    ville=Ville.objects.all()
    if request.method=="POST":
        form=villeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"la modification a reussie")
            return redirect('liste_ville')
        else:
            messages.error(request,f'formulaire invalide:{form.errors.as_text}')
    else:
        context={
        
        'formville':form,
        'ville':ville
        }
    return render(request,'liste_ville.html',context)
        
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

def table(request):
    return render(request, 'pages/tables/data.html')
def ville(request):
    return render(request, 'liste_ville.html')

# ======================================
# FONCTION QRCODE
# ======================================

def generer_qrcode(data):

    qr = qrcode.make(data)

    buffer = BytesIO()

    qr.save(buffer, format='PNG')

    qr_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode('utf-8')

    return qr_base64
# ======================================
# FONCTION CODE BARRE
# ======================================

def generer_barcode(data):
    
    barcode = Code128(
        str(data),
        writer=ImageWriter()
    )

    buffer = BytesIO()

    barcode.write(buffer)

    barcode_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode('utf-8')

    return barcode_base64
def graphe(request):
    graph = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,0],
    [0,1,0,0]
    ]
    context={
        'graph':graph
    }
    return render(request,'parties/graphe.html',context)
class Animal:
    def sound(self):
        print('Aminal makes sound')
class dog(Animal):
    def sound(self):
        print('Dog bark')
        
d=dog()
d.sound()
