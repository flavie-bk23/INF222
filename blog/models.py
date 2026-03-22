from django.db import models

# Create your models here.
class  Article(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.CharField(max_length=255)
    auteur = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    category= models.CharField(max_length=254)
    tags = models.TextField()

    class Meta:
        ordering =['-date']

    def __str__(self):
        return self.titre

