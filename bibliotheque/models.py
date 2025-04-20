from django.db import models
from django.contrib.auth.models import User

class Livre(models.Model):
    titre = models.CharField(
        max_length=200, 
        verbose_name="Titre du livre", 
        help_text="Entrez le titre complet du livre"
    )
    auteur = models.CharField(
        max_length=100, 
        verbose_name="Auteur", 
        help_text="Nom complet de l'auteur"
    )
    isbn = models.CharField(
        max_length=13, 
        verbose_name="ISBN", 
        help_text="Numéro ISBN à 13 chiffres"
    )
    date_publication = models.DateField(
        verbose_name="Date de publication", 
        help_text="Choisissez la date de publication"
    )
    ajout_par = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self) :
        return self.titre
    
