from django.db import models
from django.utils import timezone

# Create your models here.

# ManyToOne
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date deparution")
    categorie = models.ForeignKey("Categorie",on_delete=models.CASCADE) # ManyToOne
      
    class Meta: # Classe spéciale permettant de rajouter des infos 
        verbose_name = "Article"
        ordering = ["-date"]

    def __str__(self):
        """ Permet de reconnaître facilement les différents objets que nous 
            traiterons plus tard dans l'administration
        """
        return self.titre



class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        """ Permet de reconnaître facilement les différents objets que nous 
            traiterons plus tard dans l'administration
        """
        return self.nom 

# La relation OneToOne
class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom
    
class Voiture(models.Model):
    nom = models.CharField(max_length=20)
    moteur = models.OneToOneField(Moteur,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    
# Relation: ManyToManyField
class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre', 
                                      related_name='+')
    produits_sans_prix = models.ManyToManyField(Produit, related_name="vendeurs")

    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)