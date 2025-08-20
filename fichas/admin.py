from django.contrib import admin
from .models import Ficha

@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


