from django.conf.urls import patterns,url

urlpatterns = patterns('PAGINA.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^about/(?P<idtw>.*)/$','singleTweet_view',name='vista_single_tweet'),
	url(r'^cuentas/$','cuentas_view',name='vista_cuenta'),
	url(r'^cuentas/(?P<idcuenta>.*)/$','singleCuenta_view',name='vista_single_cuenta'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
	url(r'^fechas/$','fechas_view',name ='vista_fechas'),
)
