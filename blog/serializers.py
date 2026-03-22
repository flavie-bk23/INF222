from rest_framework import serializers
from .models import Article 

#creations de mes classes et fonctions du fichier serializers

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = '__all__'
        
    