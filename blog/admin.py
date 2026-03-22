from django.contrib import admin
from .models import Article

# Register your models here.
class AdminArtcile(admin.ModelAdmin):
    list_display = ('titre','contenu','auteur','date','category','tags')

admin.site.register(Article,AdminArtcile)
