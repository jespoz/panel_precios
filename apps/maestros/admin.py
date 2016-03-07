from django.contrib import admin
from apps.maestros.models import *

@admin.register(ZonaVenta)
class ZonaVentaAdmin(admin.ModelAdmin):
	pass

@admin.register(OficinaVenta)
class OficinaVentaAdmin(admin.ModelAdmin):
	pass

@admin.register(TipoCliente)
class TipoClienteAdmin(admin.ModelAdmin):
	pass

@admin.register(SubtipoCliente)
class SubtipoClienteAdmin(admin.ModelAdmin):
	pass

@admin.register(ListaPrecio)
class ListaPrecioAdmin(admin.ModelAdmin):
	pass
