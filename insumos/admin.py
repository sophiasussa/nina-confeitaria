from django.contrib import admin
from .models import Insumo

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
