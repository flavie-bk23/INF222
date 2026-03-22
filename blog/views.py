from django.shortcuts import render
from .serializers import ArticleSerializers
from .models import Article 
from rest_framework import viewsets 
from rest_framework.decorators  import  action 
from django.db.models import Q
from rest_framework.response import Response


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Article.objects.all()

        category = self.request.query_params.get('category')

        auteur = self.request.query_params.get('auteur')

        if category :
            queryset = queryset.filter(category_icontains=category)
        
        if auteur :
            queryset = queryset.filter(auteur_icontains=auteur)
    
        return queryset 
    
    serializer_class = ArticleSerializers

    @action(detail=False,methods=['get'])
    def search(self,request):
        query = request.query_params.get('query')

        if query:
            articles = Article.objects.all()
            serializer = ArticleSerializers(articles,many=True)

        return Response(serializer.data)


def home(request):
    return render(request,'page/home.html')
