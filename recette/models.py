from datetime import timezone
from django.db import models

# Create your models here.
class Recette(models.Model):
    montant=models.IntegerField(default=0)
    immatriculation=models.CharField(max_length=20,primary_key=True)
    nom_chauffeur=models.CharField(max_length=30)
    note=models.TextField(default=None)
    date_recette=models.DateField()
    date_creation=models.DateTimeField(auto_now_add=True)
    date_mis_a_jour=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.immatriculation}"
    
    class Meta:
        verbose_name='Recette'
        verbose_name_plural='Recettes'
