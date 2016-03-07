from django.db import models
from apps.maestros.models import ZonaVenta, OficinaVenta, TipoCliente, Sector, SubtipoCliente, Cadena

class TotalGeneral(models.Model):
	mes = models.IntegerField()
	year = models.IntegerField()
	descuento = models.FloatField()
	diferencia = models.FloatField(default=0, null=True)
	precio_lista = models.FloatField()
	precio_real = models.FloatField()
	kilos_real = models.FloatField()
	kilos_ppto = models.FloatField()
	kilos_proy = models.FloatField(default=0, null=True)
	cumpl_kilos = models.FloatField()
	netos_real = models.FloatField(default=0, null=True)
	netos_ppto = models.FloatField(default=0, null=True)
	netos_proy = models.FloatField(default=0, null=True)
	cumpl_netos = models.FloatField(default=0, null=True)

class TendenciaGeneral(models.Model):
	fecha = models.CharField(max_length=20)
	descuento = models.FloatField()
	mes = models.IntegerField(default=0, null=True)
	year = models.IntegerField(default=0, null=True)

class PartDifSectorGeneral(models.Model):
	mes = models.IntegerField()
	year = models.IntegerField()
	sector = models.CharField(max_length=50)
	diferencia = models.FloatField()

class PartDifTipoClienteGeneral(models.Model):
	mes = models.IntegerField()
	year = models.IntegerField()
	tipo = models.CharField(max_length=50)
	diferencia = models.FloatField()

class PartDifZonaGeneral(models.Model):
	mes = models.IntegerField()
	year = models.IntegerField()
	zona = models.CharField(max_length=50)
	diferencia = models.FloatField()

class CumplPptoSectorGeneral(models.Model):
	mes = models.IntegerField()
	year = models.IntegerField()
	sector = models.CharField(max_length=50)
	cumpl_kilos = models.FloatField()
	cumpl_netos = models.FloatField(default=0, null=True)
	descuento = models.FloatField(default=0, null=True)
	ppto = models.FloatField(default=0, null=True)

class CumplPptoTipoClienteGeneral(models.Model):
	mes = models.IntegerField()
	year = models.IntegerField()
	tipo = models.CharField(max_length=50)
	cumpl_kilos = models.FloatField()
	cumpl_netos = models.FloatField(default=0, null=True)
	descuento = models.FloatField(default=0, null=True)
	ppto = models.FloatField(default=0, null=True)

class CumplPptoZonaGeneral(models.Model):
	mes = models.IntegerField()
	year = models.IntegerField()
	zona = models.CharField(max_length=50)
	cumpl_kilos = models.FloatField()
	cumpl_netos = models.FloatField(default=0, null=True)
	descuento = models.FloatField(default=0, null=True)
	ppto = models.FloatField(default=0, null=True)

class AperturaZonaGeneral(models.Model):
	zona = models.ForeignKey(ZonaVenta)
	oficina = models.ForeignKey(OficinaVenta)
	diferencia = models.FloatField()
	descuento = models.FloatField()
	mes = models.IntegerField()
	year = models.IntegerField()

class ZonaGeneral(models.Model):
	zona = models.ForeignKey(ZonaVenta)
	kilos_real = models.FloatField()
	kilos_proy = models.FloatField()
	ppto = models.FloatField()
	cumpl_kilos = models.FloatField()
	cumpl_netos = models.FloatField(default=0, null=True)
	diferencia = models.FloatField(default=0, null=True)
	descuento = models.FloatField()
	mes = models.IntegerField()
	year = models.IntegerField()

class TendenciaZonaGeneral(models.Model):
	zona = models.ForeignKey(ZonaVenta)
	fecha = models.CharField(default='', null=True, max_length=20)
	descuento = models.FloatField()
	mes = models.IntegerField(default=0, null=True)
	year = models.IntegerField(default=0, null=True)

class AperturaTipoGeneral(models.Model):
	tipo = models.ForeignKey(TipoCliente)
	subtipo = models.CharField(max_length=100)
	id_subtipo = models.CharField(max_length=100, default='', null=True)
	diferencia = models.FloatField()
	descuento = models.FloatField()
	mes = models.IntegerField()
	year = models.IntegerField()

class TipoGeneral(models.Model):
	tipo = models.ForeignKey(TipoCliente)
	kilos_real = models.FloatField()
	kilos_proy = models.FloatField()
	ppto = models.FloatField()
	cumpl_kilos = models.FloatField()
	cumpl_netos = models.FloatField(default=0, null=True)
	diferencia = models.FloatField(default=0, null=True)
	descuento = models.FloatField()
	mes = models.IntegerField()
	year = models.IntegerField()

class TendenciaTipoGeneral(models.Model):
	tipo = models.ForeignKey(TipoCliente)
	fecha = models.CharField(default='', null=True, max_length=20)
	descuento = models.FloatField()
	mes = models.IntegerField(default=0, null=True)
	year = models.IntegerField(default=0, null=True)

class AperturaSectorGeneral(models.Model):
	sector = models.ForeignKey(Sector)
	nivel2 = models.CharField(max_length=100)
	id_nivel2 = models.CharField(max_length=100, default='', null=True)
	diferencia = models.FloatField()
	descuento = models.FloatField()
	mes = models.IntegerField()
	year = models.IntegerField()

class SectorGeneral(models.Model):
	sector = models.ForeignKey(Sector)
	kilos_real = models.FloatField()
	kilos_proy = models.FloatField()
	ppto = models.FloatField()
	cumpl_kilos = models.FloatField()
	cumpl_netos = models.FloatField(default=0, null=True)
	diferencia = models.FloatField()
	descuento = models.FloatField()
	mes = models.IntegerField()
	year = models.IntegerField()

class TendenciaSectorGeneral(models.Model):
	sector = models.ForeignKey(Sector)
	fecha = models.CharField(default='', null=True, max_length=20)
	descuento = models.FloatField()
	mes = models.IntegerField(default=0, null=True)
	year = models.IntegerField(default=0, null=True)

class CumplPptoSectorApertura(models.Model):
	sector = models.ForeignKey(Sector)
	nivel2 = models.CharField(max_length=50)
	mes = models.IntegerField()
	year = models.IntegerField()
	cumplimiento = models.FloatField()
	descuento = models.FloatField()

class TablasAperturas(models.Model):
	sector = models.ForeignKey(Sector)
	nivel2 = models.CharField(max_length=50)
	zona = models.ForeignKey(ZonaVenta)
	mes = models.IntegerField()
	year = models.IntegerField()
	oficina = models.ForeignKey(OficinaVenta)
	tipo = models.ForeignKey(TipoCliente)
	subtipo = models.ForeignKey(SubtipoCliente)
	cadena_desc = models.CharField(max_length=50)
	cod_material = models.CharField(max_length=50)
	material = models.CharField(max_length=150)
	kilos = models.FloatField()
	netos = models.FloatField()
	kilos_proy = models.FloatField()
	neto_esperado = models.FloatField()
	precio_fact = models.FloatField()
	precio_lista = models.FloatField()
	diferencia = models.FloatField()
	cadena = models.ForeignKey(Cadena, null=True)
	id_nivel2 = models.CharField(max_length=100, default='', null=True)