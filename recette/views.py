'''
from django.shortcuts import render
from .models import Recette


# Create your views here.
def index(request):
    context={'recettes': Recette.objects.all(),'cpt':0}
    return render(request, 'recette/index.html', context)

    '''

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Recette

def index(request):
    recettes = Recette.objects.all().order_by('-date_recette')

    paginator = Paginator(recettes, 7)  

    nombre_page = request.GET.get('page')  
    page_recettes = paginator.get_page(nombre_page)

    context = {
        'recettes': page_recettes,
        'taille':'len(recettes)'
    }
    return render(request, 'recette/index.html', context)



def details(request, immatriculation):
    context={'recette': Recette.objects.get(immatriculation=immatriculation)}
    return render(request, 'recette/details.html', context)

