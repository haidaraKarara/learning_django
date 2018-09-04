from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from datetime import datetime
from django.http import Http404
from blog.models import Article
# Create your views here.

def home(request,id):
    """ Exemple """
    if id > 100:
        raise Http404
    #return HttpResponse("""Le blog d'id {}""".format(id))
    return redirect("rd",permanent=False)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé")

def date_actuelle(request):
    titre = "Urgence en France, il parrait que Jean..."
    date = datetime.now()
    return render(request, 'blog/date.html', locals())


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
   # articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})