from django.contrib import admin
from .models import Recette

# Register your models here.

@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'nom_chauffeur', 'montant', 'date_recette','date_creation','date_mis_a_jour')
    search_fields = ('immatriculation', 'nom_chauffeur')
    list_filter = ('date_recette',)