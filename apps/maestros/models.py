from django.db import models

class ZonaVenta(models.Model):
	zona = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Zona de Venta"
		verbose_name_plural = "Zona de Ventas"

	def __unicode__(self):
		return self.zona

class OficinaVenta(models.Model):
	codigo = models.CharField(primary_key=True, max_length=50)
	oficina = models.CharField(max_length=50)
	zona = models.ForeignKey(ZonaVenta)

	class Meta:
		verbose_name = "Oficina de Venta"
		verbose_name_plural = "Oficina de Ventas"

	def __unicode__(self):
		return self.oficina

class TipoCliente(models.Model):
	codigo = models.IntegerField(primary_key=True)
	tipo = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Tipo de Cliente"
		verbose_name_plural = "Tipo de Clientes"

	def __unicode__(self):
		return self.tipo

class SubtipoCliente(models.Model):
	codigo = models.CharField(primary_key=True, max_length=50)
	subtipo = models.CharField(max_length=100)
	tipocliente = models.ForeignKey(TipoCliente)

	class Meta:
		verbose_name = "Subtipo cliente"
		verbose_name_plural = "Subtipo clientes"

	def __unicode__(self):
		return self.subtipo

class ListaPrecio(models.Model):
	oficina = models.ForeignKey(OficinaVenta)
	subtipo = models.ForeignKey(SubtipoCliente)
	lista = models.CharField(max_length=2)

	def __unicode__(self):
		return self.lista

class MARM(models.Model):
	material = models.CharField(max_length=50)
	um = models.CharField(max_length=10)
	contador = models.FloatField(default=0)
	denominador = models.FloatField(default=0)

	def __unicode__(self):
		return '%s - %s' %(self.material, self.um)

class A900(models.Model):
	lista = models.CharField(max_length=2)
	material = models.CharField(max_length=50)
	inicio = models.DateField()
	fin = models.DateField()
	registro = models.CharField(max_length=50)

	def __unicode__(self):
		return '%s - %s - %s' %(self.material, self.lista, self.inicio)

class A900_Paso(models.Model):
	lista = models.CharField(max_length=2)
	material = models.CharField(max_length=50)
	inicio = models.DateField()
	fin = models.DateField()
	registro = models.CharField(max_length=50)

	def __unicode__(self):
		return '%s - %s - %s' %(self.material, self.lista, self.inicio)

class KONP(models.Model):
	registro = models.CharField(max_length=50)
	importe = models.FloatField(default=0)
	um = models.CharField(max_length=10)

	def __unicode__(self):
		return self.registro

class KONP_Paso(models.Model):
	registro = models.CharField(max_length=50)
	importe = models.FloatField(default=0)
	um = models.CharField(max_length=10)

	def __unicode__(self):
		return self.registro

class PrecioKilo(models.Model):
	lista = models.CharField(max_length=2)
	material = models.CharField(max_length=50)
	inicio = models.DateField()
	fin = models.DateField()
	precio = models.FloatField(default=0)

	def __unicode__(self):
		return '%s - %s - %s' %(self.material, self.lista, self.inicio)

class CargaVenta(models.Model):
	oficina = models.ForeignKey(OficinaVenta)
	tipocliente = models.ForeignKey(TipoCliente)
	subtipo = models.ForeignKey(SubtipoCliente)
	cod_local = models.CharField(max_length=50)
	cliente_local = models.CharField(max_length=150)
	fecha = models.DateField()
	factura = models.CharField(max_length=50)
	cod_material = models.CharField(max_length=50)
	material = models.CharField(max_length=150)
	sector = models.CharField(max_length=2)
	marca = models.CharField(max_length=50)
	nivel2 = models.CharField(max_length=50)
	nivel3 = models.CharField(max_length=50)
	mes = models.IntegerField()
	year = models.IntegerField()
	unidades = models.FloatField()
	kilos = models.FloatField()
	netos = models.FloatField()
	cadena = models.CharField(max_length=50, null=True, default='')
	nivel2_agrupado = models.CharField(max_length=50, null=True, default='')

class Sector(models.Model):
	codigo = models.IntegerField(primary_key=True)
	sector = models.CharField(max_length=50)

class PresupuestoVentas(models.Model):
	sector = models.ForeignKey(Sector)
	marca = models.CharField(max_length=50)
	nivel2 = models.CharField(max_length=50)
	nivel3 = models.CharField(max_length=50)
	oficina = models.ForeignKey(OficinaVenta)
	tipocliente = models.ForeignKey(TipoCliente)
	mes = models.IntegerField()
	year = models.IntegerField()
	kilo = models.FloatField()
	neto = models.FloatField()

class DetalleCalculo(models.Model):
	oficina = models.ForeignKey(OficinaVenta)
	tipocliente = models.ForeignKey(TipoCliente)
	subtipo = models.ForeignKey(SubtipoCliente)
	cod_local = models.CharField(max_length=50)
	cliente_local = models.CharField(max_length=150)
	fecha = models.DateField()
	factura = models.CharField(max_length=50)
	cod_material = models.CharField(max_length=50)
	material = models.CharField(max_length=150)
	sector = models.ForeignKey(Sector, db_index=True)
	marca = models.CharField(max_length=50)
	nivel2 = models.CharField(max_length=50, db_index=True)
	nivel3 = models.CharField(max_length=50)
	mes = models.IntegerField(db_index=True)
	year = models.IntegerField(db_index=True)
	unidades = models.FloatField()
	kilos = models.FloatField()
	netos = models.FloatField()
	precio_promedio = models.FloatField()
	precio_lista = models.FloatField()
	diferencia = models.FloatField()
	neto_esperado = models.FloatField()
	lista = models.CharField(max_length=2)
	mes = models.CharField(max_length=2)
	nivel2_agrupado = models.CharField(max_length=50, null=True, default='')
	cadena = models.CharField(max_length=50, null=True, default='')

class Nivel2(models.Model):
	codigo = models.CharField(max_length=50, primary_key=True)
	nivel = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nivel

class Cadena(models.Model):
	codigo = models.CharField(max_length=50, primary_key=True)
	cadena = models.CharField(max_length=50)

	def __unicode__(self):
		return self.cadena

class Fecha(models.Model):
	fecha = models.DateField()
	habil = models.IntegerField()

	def __unicode__(self):
		return self.fecha

class Actualizacion(models.Model):
	fecha = models.DateField()

	def __unicode__(self):
		return self.fecha