# -*- coding: utf-8 -*-
import decimal
import json
from django.db.models import Count, Sum, F
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, DetailView
from .models import *
from apps.maestros.models import ZonaVenta, Sector, Nivel2, TipoCliente, SubtipoCliente, Cadena, OficinaVenta, DetalleCalculo, Actualizacion
from datetime import date

d = date.today()
# month = d.month
# year = d.year

month = 2
year = 2016

def monthText(monthInt):
	month = ''
	if monthInt == 1:
		month = 'Enero '
	if monthInt == 2:
		month = 'Febrero '
	if monthInt == 3:
		month = 'Marzo '
	if monthInt == 4:
		month = 'Abril '
	if monthInt == 5:
		month = 'Mayo '
	if monthInt == 6:
		month = 'Junio '
	if monthInt == 7:
		month = 'Julio '
	if monthInt == 8:
		month = 'Agosto '
	if monthInt == 9:
		month = 'Septiembre '
	if monthInt == 10:
		month = 'Octubre '
	if monthInt == 11:
		month = 'Noviembre '
	if monthInt == 12:
		month = 'Diciembre '
	return month

class GeneralView(TemplateView):
	template_name = "general.html"

	def get_context_data(self, **kwargs):
		context = super(GeneralView, self).get_context_data(**kwargs)
		context['descuento'] = TotalGeneral.objects.values('descuento', 'precio_lista', 'precio_real', 'cumpl_kilos', 'kilos_ppto', 'kilos_real', 'diferencia', 'netos_ppto', 'netos_real', 'cumpl_netos', 'id', 'kilos_proy', 'netos_proy').filter(mes=month, year=year)
		context['periodo'] = monthText(month) + str(year)
		if month - 1 == 0:
			monthBefore = 12
			yearBefore = year - 1
		else:
			monthBefore = month - 1
			yearBefore = year
		if TotalGeneral.objects.filter(mes=monthBefore, year=yearBefore).exists():
			context['anterior'] = monthText(monthBefore) + str(yearBefore)
			anterior = TotalGeneral.objects.values('id').filter(mes=monthBefore, year=yearBefore)
			for x in anterior:
				context['id_anterior'] = x['id']
		actualizacion = Actualizacion.objects.all()[:1]
		for x in actualizacion:
			context['actualizacion'] = x.fecha
		return context

class GeneralViewFiltro(DetailView):
	template_name = "general.html"
	model = TotalGeneral

	def get_context_data(self, **kwargs):
		context = super(GeneralViewFiltro, self).get_context_data(**kwargs)
		context['descuento'] = TotalGeneral.objects.values('id', 'descuento', 'precio_lista', 'precio_real', 'cumpl_kilos', 'kilos_ppto', 'kilos_real', 'diferencia', 'netos_ppto', 'netos_real', 'cumpl_netos', 'mes', 'year', 'kilos_proy', 'netos_proy').filter(id=self.get_object().pk)
		for x in context['descuento']:
			month = x['mes']
			year = x['year']
		context['periodo'] = monthText(month) + str(year)
		if month - 1 == 0:
			monthBefore = 12
			yearBefore = year - 1
		else:
			monthBefore = month - 1
			yearBefore = year
		if TotalGeneral.objects.filter(mes=monthBefore, year=yearBefore).exists():
			context['anterior'] = monthText(monthBefore) + str(yearBefore)
			anterior = TotalGeneral.objects.values('id').filter(mes=monthBefore, year=yearBefore)
			for x in anterior:
				context['id_anterior'] = x['id']
		if month + 1 == 13:
			monthAfter = 1
			yearAfter = year + 1
		else:
			monthAfter = month + 1
			yearAfter = year
		if TotalGeneral.objects.filter(mes=monthAfter, year=yearAfter).exists():
			context['posterior'] = monthText(monthAfter) + str(yearAfter)
			anterior = TotalGeneral.objects.values('id').filter(mes=monthAfter, year=yearAfter)
			for x in anterior:
				context['id_posterior'] = x['id']
		actualizacion = Actualizacion.objects.all()[:1]
		for x in actualizacion:
			context['actualizacion'] = x.fecha
		return context

class ZonaGeneralView(DetailView):
	template_name = "zona_general.html"
	model = TotalGeneral

	def get_context_data(self, **kwargs):
		context = super(ZonaGeneralView, self).get_context_data(**kwargs)
		context['descuento'] = TotalGeneral.objects.values('id', 'descuento', 'precio_lista', 'precio_real', 'cumpl_kilos', 'kilos_ppto', 'kilos_real', 'diferencia', 'netos_ppto', 'netos_real', 'cumpl_netos', 'mes', 'year', 'kilos_proy', 'netos_proy').filter(id=self.get_object().pk)
		for x in context['descuento']:
			month = x['mes']
			year = x['year']
		context['apertura'] = AperturaZonaGeneral.objects.all().filter(mes=month, year=year).order_by('diferencia')
		context['zonas'] = ZonaGeneral.objects.all().filter(mes=month, year=year)
		context['periodo'] = monthText(month) + str(year)
		actualizacion = Actualizacion.objects.all()[:1]
		for x in actualizacion:
			context['actualizacion'] = x.fecha
		return context

class TipoGeneralView(DetailView):
	template_name = "tc_general.html"
	model = TotalGeneral

	def get_context_data(self, **kwargs):
		context = super(TipoGeneralView, self).get_context_data(**kwargs)
		context['descuento'] = TotalGeneral.objects.values('id', 'descuento', 'precio_lista', 'precio_real', 'cumpl_kilos', 'kilos_ppto', 'kilos_real', 'diferencia', 'netos_ppto', 'netos_real', 'cumpl_netos', 'mes', 'year', 'kilos_proy', 'netos_proy').filter(id=self.get_object().pk)
		for x in context['descuento']:
			month = x['mes']
			year = x['year']
		context['apertura'] = AperturaTipoGeneral.objects.all().filter(mes=month, year=year).exclude(tipo__codigo=60).order_by('diferencia')
		context['tipos'] = TipoGeneral.objects.all().exclude(tipo__codigo=60).filter(mes=month, year=year)
		context['periodo'] = monthText(month) + str(year)
		actualizacion = Actualizacion.objects.all()[:1]
		for x in actualizacion:
			context['actualizacion'] = x.fecha
		return context

class SectorGeneralView(DetailView):
	template_name = "sector_general.html"
	model = TotalGeneral

	def get_context_data(self, **kwargs):
		context = super(SectorGeneralView, self).get_context_data(**kwargs)
		context['descuento'] = TotalGeneral.objects.values('id', 'descuento', 'precio_lista', 'precio_real', 'cumpl_kilos', 'kilos_ppto', 'kilos_real', 'diferencia', 'netos_ppto', 'netos_real', 'cumpl_netos', 'mes', 'year', 'kilos_proy', 'netos_proy').filter(id=self.get_object().pk)
		for x in context['descuento']:
			month = x['mes']
			year = x['year']
		context['apertura'] = AperturaSectorGeneral.objects.all().filter(mes=month, year=year).order_by('diferencia')
		context['sectores'] = SectorGeneral.objects.all().filter(mes=month, year=year).order_by('sector_id')
		context['periodo'] = monthText(month) + str(year)
		actualizacion = Actualizacion.objects.all()[:1]
		for x in actualizacion:
			context['actualizacion'] = x.fecha
		return context

class TablasAperturaView(DetailView):
	template_name = "tablas_apertura.html"
	model = TotalGeneral

	def get_context_data(self, **kwargs):
		context = super(TablasAperturaView, self).get_context_data(**kwargs)
		context['tabla'] = []
		context['descuento'] = TotalGeneral.objects.values('id', 'descuento', 'precio_lista', 'precio_real', 'cumpl_kilos', 'kilos_ppto', 'kilos_real', 'diferencia', 'netos_ppto', 'netos_real', 'cumpl_netos', 'mes', 'year', 'kilos_proy', 'netos_proy').filter(id=self.get_object().pk)
		for x in context['descuento']:
			month = x['mes']
			year = x['year']
		context['periodo'] = monthText(month) + str(year)
		actualizacion = Actualizacion.objects.all()[:1]
		for x in actualizacion:
			context['actualizacion'] = x.fecha
		if self.kwargs['apertura'] == 'tipo':
			context['tipo_apertura'] = 'Zona de Ventas'
			context['tipo_nivel'] = self.kwargs['nivel']
			tipo = TipoCliente.objects.values('tipo').filter(codigo=self.kwargs['agrupacion'])
			for x in tipo:
				context['filtro'] = 'Tipo de Cliente ' + x['tipo'] + ' - '
			if self.kwargs['agrupacion'] != '20':
				nivel = SubtipoCliente.objects.values('subtipo').filter(codigo=self.kwargs['nivel'])
				for x in nivel:
					context['filtro'] = context['filtro'] + x['subtipo']
				tabla = TablasAperturas.objects.values('zona__zona', 'zona_id').filter(mes=month, year=year, subtipo_id=self.kwargs['nivel']).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				nivel = Cadena.objects.values('cadena').filter(codigo=self.kwargs['nivel'])
				for x in nivel:
					context['filtro'] = context['filtro'] + x['cadena']
				tabla = TablasAperturas.objects.values('zona__zona', 'zona_id').filter(mes=month, year=year, cadena_id=self.kwargs['nivel']).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				facturado = x['netos'] / x['kilos']
				if x['kilos'] == 0:
					lista = 0
				else:
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context['tabla'].append({'zona_id': x['zona_id'], 'zona__zona': x['zona__zona'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': facturado, 'lista': lista, 'descuento': descuento, 'diferencia': x['diferencia']})
		if self.kwargs['apertura'] == 'zona':
			context['tipo_apertura'] = 'Tipo de Cliente'
			context['tipo_nivel'] = self.kwargs['nivel']
			zona = ZonaVenta.objects.values('zona').filter(id=self.kwargs['agrupacion'])
			for x in zona:
				context['filtro'] = 'Zona ' + x['zona'] + ' - '
			oficina = OficinaVenta.objects.values('oficina').filter(codigo=self.kwargs['nivel'])
			for x in oficina:
				context['filtro'] = context['filtro'] + x['oficina']
			tabla = TablasAperturas.objects.values('tipo__tipo', 'tipo_id').filter(mes=month, year=year, zona_id=self.kwargs['agrupacion'], oficina_id=self.kwargs['nivel']).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				facturado = x['netos'] / x['kilos']
				if x['kilos'] == 0:
					lista = 0
				else:
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context['tabla'].append({'zona_id': x['tipo_id'], 'zona__zona': x['tipo__tipo'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': facturado, 'lista': lista, 'descuento': descuento, 'diferencia': x['diferencia']})
		if self.kwargs['apertura'] == 'sector':
			context['tipo_apertura'] = 'Zona de Ventas'
			context['tipo_nivel'] = self.kwargs['nivel']
			sector = Sector.objects.values('sector').filter(codigo=self.kwargs['agrupacion'])
			for x in sector:
				context['filtro'] = 'Sector ' + x['sector'] + ' - '
			nivel = Nivel2.objects.values('nivel').filter(codigo=self.kwargs['nivel'])
			for x in nivel:
				context['filtro'] = context['filtro'] + x['nivel']
			tabla = TablasAperturas.objects.values('zona__zona', 'zona_id', 'sector_id').filter(mes=month, year=year, sector_id=self.kwargs['agrupacion'], nivel2=x['nivel']).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				facturado = x['netos'] / x['kilos']
				if x['kilos'] == 0:
					lista = 0
				else:
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context['tabla'].append({'zona_id': str(x['zona_id']) + str(x['sector_id']), 'zona__zona': x['zona__zona'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': facturado, 'lista': lista, 'descuento': descuento, 'diferencia': x['diferencia']})
		return context

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def participaciones(request):
	if request.is_ajax():
		participacion_sector = PartDifSectorGeneral.objects.extra(select={'name': 'sector', 'y': 'diferencia'}).values('name', 'y').filter(mes=month, year=year).order_by('-y')
		diccionario_sector = ValuesQuerySetToDict(participacion_sector)
		participacion_tc = PartDifTipoClienteGeneral.objects.extra(select={'name': 'tipo', 'y': 'diferencia'}).values('name', 'y').filter(mes=month, year=year).order_by('-y')
		diccionario_tc = ValuesQuerySetToDict(participacion_tc)
		participacion_zona = PartDifZonaGeneral.objects.extra(select={'name': 'zona', 'y': 'diferencia'}).values('name', 'y').filter(mes=month, year=year).order_by('-y')
		diccionario_zona = ValuesQuerySetToDict(participacion_zona)
		json_data = json.dumps({'participacion_sector': diccionario_sector, 'participacion_tc': diccionario_tc, 'participacion_zona': diccionario_zona})
		return HttpResponse(json_data, content_type='application/json; charset=utf8')
	else:
		raise Http404

def cumplimientos(request, pk):
	if request.is_ajax():
		general = TotalGeneral.objects.values('mes', 'year').filter(id=pk)
		for x in general:
			month = x['mes']
			year = x['year']
		cumplimiento_sector = CumplPptoSectorGeneral.objects.values('sector', 'cumpl_kilos', 'descuento').filter(mes=month, year=year).order_by('-cumpl_kilos')
		diccionario_cumpl_sector = ValuesQuerySetToDict(cumplimiento_sector)
		cumplimiento_tc = CumplPptoTipoClienteGeneral.objects.values('tipo', 'cumpl_kilos', 'descuento').filter(mes=month, year=year).exclude(tipo='Consumidor').order_by('-cumpl_kilos')
		diccionario_cumpl_tc = ValuesQuerySetToDict(cumplimiento_tc)
		cumplimiento_zona = CumplPptoZonaGeneral.objects.values('zona', 'cumpl_kilos', 'descuento').filter(mes=month, year=year).order_by('-cumpl_kilos')
		diccionario_cumpl_zona = ValuesQuerySetToDict(cumplimiento_zona)
		json_data = json.dumps({'cumplimiento_sector': diccionario_cumpl_sector, 'cumplimiento_tipocliente': diccionario_cumpl_tc, 'cumplimiento_zona': diccionario_cumpl_zona})
		return HttpResponse(json_data, content_type='application/json; charset=utf8')
	else:
		raise Http404

def tendenciaZonaGeneral(request, pk):
	if request.is_ajax():
		general = TotalGeneral.objects.values('mes', 'year').filter(id=pk)
		for x in general:
			month = x['mes']
			year = x['year']
		tendencia_general = TendenciaGeneral.objects.values('fecha', 'descuento').filter(mes=month, year=year).order_by('fecha')
		diccionario_tendencia_general = ValuesQuerySetToDict(tendencia_general)
		tendencia_zona = TendenciaZonaGeneral.objects.values('zona_id', 'fecha', 'descuento').filter(mes=month, year=year).order_by('fecha')
		diccionario_tendencia_zona = ValuesQuerySetToDict(tendencia_zona)
		fechas = TendenciaZonaGeneral.objects.values('fecha').annotate(cuenta=Count('fecha')).filter(mes=month, year=year).order_by('fecha')
		diccionario_fechas = ValuesQuerySetToDict(fechas)
		tendencia_tipo = TendenciaTipoGeneral.objects.values('tipo_id', 'fecha', 'descuento').filter(mes=month, year=year).order_by('fecha')
		diccionario_tendencia_tipo = ValuesQuerySetToDict(tendencia_tipo)
		tendencia_sector = TendenciaSectorGeneral.objects.values('sector_id', 'fecha', 'descuento').filter(mes=month, year=year).order_by('fecha')
		diccionario_tendencia_sector = ValuesQuerySetToDict(tendencia_sector)
		json_data = json.dumps({'tendencia_zona': diccionario_tendencia_zona, 'fechas': diccionario_fechas, 'tendencia_tipo': diccionario_tendencia_tipo, 'tendencia_sector': diccionario_tendencia_sector, 'tendencia_general': diccionario_tendencia_general})
		return HttpResponse(json_data, content_type='application/json; charset=utf8')
	else:
		raise Http404

def aperturaMas(request, apertura, agrupacion, nivel, pk):
	if request.is_ajax():
		general = TotalGeneral.objects.values('mes', 'year').filter(id=pk)
		for x in general:
			month = x['mes']
			year = x['year']
		context = []
		dict_nivel = []
		nivel2 = ""
		sector = 0
		cadena = ""
		id_cadena = 0
		sector_id_qs = ''
		if apertura == 'cadenazona':
			if agrupacion[:1] == "C" or agrupacion[:1] == "#":
				tabla = TablasAperturas.objects.values('oficina__oficina', 'oficina__codigo').filter(mes=month, year=year, cadena_id=agrupacion, zona_id=nivel).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				tabla = TablasAperturas.objects.values('oficina__oficina', 'oficina__codigo').filter(mes=month, year=year, subtipo_id=agrupacion, zona_id=nivel).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'oficina': x['oficina__oficina'], 'oficina__codigo': x['oficina__codigo'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'nivel2zona':
			dict_nivel = Nivel2.objects.values('nivel').filter(codigo=agrupacion)
			if len(nivel) == 2:
				sector_id_qs = nivel[-1:]
			if len(nivel) == 3:
				sector_id_qs = nivel[-2:]
			for x in dict_nivel:
				nivel2 = x['nivel']
			tabla = TablasAperturas.objects.values('oficina__oficina', 'oficina__codigo', 'sector_id').filter(mes=month, year=year, nivel2=nivel2, zona_id=nivel[:1], sector_id=sector_id_qs).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'oficina': x['oficina__oficina'], 'oficina__codigo': x['oficina__codigo'] + str(x['sector_id']), 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'cadenaoficina':
			if agrupacion[:1] == "C" or agrupacion[:1] == "#":
				tabla = TablasAperturas.objects.values('sector__sector', 'oficina__codigo', 'sector_id').filter(mes=month, year=year, oficina_id=nivel, cadena_id=agrupacion).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				tabla = TablasAperturas.objects.values('sector__sector', 'oficina__codigo', 'sector_id').filter(mes=month, year=year, oficina_id=nivel, subtipo_id=agrupacion).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'tipo': x['sector__sector'], 'tipo_id': x['sector_id'], 'oficina__codigo': x['oficina__codigo'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'nivel2oficina':
			dict_nivel = Nivel2.objects.values('nivel').filter(codigo=agrupacion)
			if len(nivel) == 5:
				sector_id_qs = nivel[-1:]
			if len(nivel) == 6:
				sector_id_qs = nivel[-2:]
			for x in dict_nivel:
				nivel2 = x['nivel']
			tabla = TablasAperturas.objects.values('tipo__tipo', 'tipo_id', 'oficina__codigo', 'sector_id').filter(mes=month, year=year, nivel2=nivel2, oficina_id=nivel[:4], sector_id=sector_id_qs).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'tipo': x['tipo__tipo'], 'oficina__codigo': x['oficina__codigo'], 'tipo_id': str(x['tipo_id']) + str(x['sector_id']), 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'cadenaoficinasector':
			if len(nivel) == 5:
				sector_id_qs = nivel[-1:]
			else:
				sector_id_qs = nivel[-2:]
			if agrupacion[:1] == "C" or agrupacion[:1] == "#":
				tabla = TablasAperturas.objects.values('nivel2', 'oficina__codigo', 'sector_id', 'id_nivel2').filter(mes=month, year=year, oficina_id=nivel[:4], sector_id=sector_id_qs, cadena_id=agrupacion).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				tabla = TablasAperturas.objects.values('nivel2', 'oficina__codigo', 'sector_id', 'id_nivel2').filter(mes=month, year=year, oficina_id=nivel[:4], sector_id=sector_id_qs, subtipo_id=agrupacion).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'id_nivel2': str(x['id_nivel2']) + str(x['sector_id']), 'oficina__codigo': x['oficina__codigo'], 'sector_id': x['sector_id'], 'tipo': x['nivel2'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'zonatipo':
			if nivel == '20':
				cadena = "cadena_desc"
				id_cadena = "cadena_id"
			else:
				cadena = "subtipo__subtipo"
				id_cadena = "subtipo_id"
			tabla = TablasAperturas.objects.values(cadena, id_cadena, 'oficina__codigo', 'tipo_id').filter(mes=month, year=year, oficina_id=agrupacion, tipo_id=nivel).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'tipo': x[cadena], 'id_tipo': x[id_cadena], 'oficina__codigo': x['oficina__codigo'], 'tc': x['tipo_id'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'nivel2oficinatipo':
			dict_nivel = Nivel2.objects.values('nivel').filter(codigo=agrupacion)
			if len(nivel) == 7:
				sector_id_qs = nivel[-1:]
			if len(nivel) == 8:
				sector_id_qs = nivel[-2:]
			for x in dict_nivel:
				nivel2 = x['nivel']
			if nivel[:6][-2:] == '20':
				cadena = "cadena_desc"
				id_cadena = "cadena_id"
			else:
				cadena = "subtipo__subtipo"
				id_cadena = "subtipo_id"
			tabla = TablasAperturas.objects.values(cadena, id_cadena, 'oficina__codigo', 'tipo_id', 'sector_id').filter(mes=month, year=year, nivel2=nivel2, oficina_id=nivel[:4], tipo_id=nivel[:6][-2:], sector_id=sector_id_qs).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'tipo': x[cadena], 'id_tipo': str(x[id_cadena]) + str(x['sector_id']), 'oficina__codigo': x['oficina__codigo'], 'tc': x['tipo_id'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'cadenaoficinatipomaterial':
			if len(nivel) == 9:
				nivel_id_qs = nivel[:8][-4:]
				sector_id_qs = nivel[-1:]
			if len(nivel) > 9:
				nivel_id_qs = nivel[:9][-5:]
				sector_id_qs = nivel[-2:]
			if nivel[:5][-1:] == '9':
				nivel_id_qs = '9999'
			if agrupacion[:1] == "C" or agrupacion[:1] == "#":
				cadena = "cadena_id"
				tabla = TablasAperturas.objects.values('cod_material', 'material', 'oficina_id', cadena).filter(mes=month, year=year, id_nivel2=nivel_id_qs, cadena_id=agrupacion, oficina_id=nivel[:4], sector_id=sector_id_qs).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				cadena = "subtipo_id"
				tabla = TablasAperturas.objects.values('cod_material', 'material', 'oficina_id', cadena).filter(mes=month, year=year, id_nivel2=nivel_id_qs, subtipo_id=agrupacion, oficina_id=nivel[:4], sector_id=sector_id_qs).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'dispersion': x['cod_material'] + x['oficina_id'] + x[cadena], 'material': x['cod_material'] + ' - ' + x['material'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'zonatipocadena':
			if nivel[:1] == "C" or nivel[:1] == "#":
				id_cadena = "cadena_id"
				tabla = TablasAperturas.objects.values('sector__sector', 'sector_id', id_cadena).filter(mes=month, year=year, oficina_id=agrupacion, cadena_id=nivel).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				id_cadena = "subtipo_id"
				tabla = TablasAperturas.objects.values('sector__sector', 'sector_id', id_cadena).filter(mes=month, year=year, oficina_id=agrupacion, subtipo_id=nivel).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'sector_id': x['sector_id'], 'sector': x['sector__sector'], 'tipo': x[id_cadena], 'netos': x['netos'], 'kilos': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'zonatipocadenasector':
			if nivel[-2:][:1] == 'C':
				cadena = "cadena_desc"
				id_cadena = "cadena_id"
			else:
				cadena = "subtipo__subtipo"
				id_cadena = "subtipo_id"
			if nivel[-2:][:1] == "C":
				tabla = TablasAperturas.objects.values('nivel2', 'id_nivel2', cadena, 'sector_id', id_cadena).filter(mes=month, year=year, oficina_id=agrupacion, cadena_id=nivel[-2:], sector_id=int(nivel[:2])).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				tabla = TablasAperturas.objects.values('nivel2', 'id_nivel2', cadena, 'sector_id', id_cadena).filter(mes=month, year=year, oficina_id=agrupacion, subtipo_id=int(nivel[-2:]), sector_id=int(nivel[:2])).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'sector_id': x['sector_id'], 'id_nivel2': x['id_nivel2'], 'nivel2': x['nivel2'], 'tipo':x[cadena], 'tipo_id': x[id_cadena], 'netos': x['netos'], 'kilos': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'zonatipocadenasectormaterial':
			var_nivel_2 = ''
			if len(nivel) == 8:
				var_nivel_2 = nivel[-4:]
			else:
				var_nivel_2 = nivel[-5:]
			if nivel[:3][-1:] == "C":
				cadena = "cadena_id"
				tabla = TablasAperturas.objects.values('cod_material', 'material', 'oficina_id', cadena).filter(mes=month, year=year, oficina_id=agrupacion, cadena_id=nivel[:4][-2:], sector_id=int(nivel[:2]), id_nivel2=var_nivel_2).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				cadena = "subtipo_id"
				tabla = TablasAperturas.objects.values('cod_material', 'material', 'oficina_id', cadena).filter(mes=month, year=year, oficina_id=agrupacion, subtipo_id=int(nivel[:4][-2:]), sector_id=int(nivel[:2]), id_nivel2=var_nivel_2).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'dispersion': x['cod_material'] + x['oficina_id'] + x[cadena], 'material': x['cod_material'] + ' - ' + x['material'], 'netos': x['netos'], 'kilos': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		if apertura == 'nivel2oficinatipomaterial':
			dict_nivel = Nivel2.objects.values('nivel').filter(codigo=agrupacion)
			if len(nivel) == 9:
				sector_id_qs = nivel[-1:]
			if len(nivel) == 10:
				sector_id_qs = nivel[-2:]
			for x in dict_nivel:
				nivel2 = x['nivel']
			if nivel[:6][-2:] == '20':
				cadena = "cadena_id"
				tabla = TablasAperturas.objects.values('cod_material', 'material', 'oficina_id', cadena).filter(mes=month, year=year, nivel2=nivel2, sector_id=sector_id_qs, cadena_id=nivel[:8][-2:], oficina_id=nivel[:4]).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			else:
				cadena = "subtipo_id"
				tabla = TablasAperturas.objects.values('cod_material', 'material', 'oficina_id', cadena).filter(mes=month, year=year, nivel2=nivel2, sector_id=sector_id_qs, subtipo_id=nivel[:8][-2:], oficina_id=nivel[:4]).annotate(kilos=Sum('kilos'), netos=Sum('netos'), kilos_proy=Sum('kilos_proy'), netos_esperados=Sum('neto_esperado'), diferencia=Sum('diferencia')).order_by('diferencia')
			for x in tabla:
				if x['kilos'] == 0:
					facturado = 0
					lista = 0
				else:
					facturado = x['netos'] / x['kilos']
					lista = x['netos_esperados'] / x['kilos']
				if x['netos_esperados'] == 0:
					descuento = 0
				else:
					descuento = ((x['netos'] - x['netos_esperados']) / x['netos_esperados']) * 100
				context.append({'dispersion': x['cod_material'] + x['oficina_id'] + x[cadena], 'material': x['cod_material'] + ' - ' + x['material'], 'kilos': x['kilos'], 'netos': x['netos'], 'kilos_proy': x['kilos_proy'], 'netos_esperados': x['netos_esperados'], 'facturado': round(facturado, 0), 'lista': round(lista), 'descuento': round(descuento, 1), 'diferencia': x['diferencia']})
		json_data = json.dumps({'tabla': context})
		return HttpResponse(json_data, content_type='application/json; charset=utf8')
	else:
		raise Http404

def dispersion(request, dispersion, pk):
	# if request.is_ajax():
		general = TotalGeneral.objects.values('mes', 'year').filter(id=pk)
		for x in general:
			month = x['mes']
			year = x['year']
		material = "'" + str(dispersion[:7]) + "'"
		oficina = "'" + str(dispersion[:11][-4:]) + "'"
		context = []
		descuento = 0.0
		if dispersion[-2:][:1] == 'C' or dispersion[-2:][:1] == '#':
			cadena = Cadena.objects.values('cadena').filter(codigo=dispersion[-2:])
			tabla = DetalleCalculo.objects.values('kilos', 'precio_promedio', 'precio_lista', 'cod_local', 'cliente_local').filter(mes=month, year=year, cod_material=str(material), oficina_id=str(oficina), cadena=str(cadena))
		else:
			tabla = DetalleCalculo.objects.values('kilos', 'precio_promedio', 'precio_lista', 'cod_local', 'cliente_local').filter(mes=month, year=year, cod_material=str(material), oficina_id=str(oficina), subtipo_id=dispersion[-2:])
		for x in tabla:
			if x['precio_lista'] == 0:
				descuento = 0
			else:
				descuento = round(((x['precio_promedio'] - x['precio_lista']) / x['precio_lista']) * 100, 1)
			context.append({'x': x['kilos'], 'y': descuento, 'dataLabels': x['cod_local'] + ' - ' + x['cliente_local']})
		json_data = json.dumps({'tabla': context})
		return HttpResponse(json_data, content_type='application/json; charset=utf8')
	# else:
	# 	raise Http404