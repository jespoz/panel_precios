from django.conf.urls import url
from .views import GeneralView, ZonaGeneralView, TipoGeneralView, SectorGeneralView, TablasAperturaView, GeneralViewFiltro
from apps.panel.views import participaciones, cumplimientos, tendenciaZonaGeneral, aperturaMas, dispersion
from django.contrib.auth.views import login, logout_then_login
urlpatterns = [

	url(r'^$' , login, {'template_name':'login.html'}, name='login'),
	url(r'^logout/$' , logout_then_login, name='logout'),

	url(r'^participacion/$', participaciones),
	url(r'^cumplimiento/(?P<pk>\d+)/$', cumplimientos),
	url(r'^tendencias/(?P<pk>\d+)/$', tendenciaZonaGeneral),
	url(r'^general/$', GeneralView.as_view(), name="general"),
	url(r'^general/(?P<pk>\d+)/$', GeneralViewFiltro.as_view(), name='general_filtro'),
	url(r'^zona_general/(?P<pk>\d+)/$', ZonaGeneralView.as_view(), name="zona_general"),
	url(r'^tipo_general/(?P<pk>\d+)/$', TipoGeneralView.as_view(), name="tipo_general"),
	url(r'^sector_general/(?P<pk>\d+)/$', SectorGeneralView.as_view(), name="sector_general"),
	url(r'^apertura/(?P<pk>\d+)/(?P<apertura>\w+)/(?P<agrupacion>\w+)/(?P<nivel>\w+)/$', TablasAperturaView.as_view(), name="tablas_apertura"),
	url(r'^aperturamas/(?P<pk>\d+)/(?P<apertura>\w+)/(?P<agrupacion>\w+)/(?P<nivel>\w+)/$', aperturaMas),
	url(r'^dispersion/(?P<pk>\d+)/(?P<dispersion>\w+)/$', dispersion),

]