from django.shortcuts import render_to_response
from django.template import RequestContext
from PAGINA.apps.pagina.models import Cuenta,Etiqueta,Tweet,Contiene
from PAGINA.apps.home.forms import ContactForm,ContactForm2

def index_view(request):
	tweets = Tweet.objects.filter()
	ctx = {'tweets':tweets}
	return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def about_view(request):
        tweets = Tweet.objects.filter(tipo_Tweet = True).order_by("-fecha")
        tweets2 = Tweet.objects.filter(tipo_Tweet = False).order_by("-fecha")
        ctx = {'tweets':tweets,'tweets2':tweets2}
        return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def singleCuenta_view(request,idcuenta):
	cuenta = Cuenta.objects.get(id_Cuenta = idcuenta)
	ctx = {'cuenta':cuenta}
	return render_to_response('home/singlecuenta.html',ctx,context_instance=RequestContext(request))

def cuentas_view(request):
	cuentas = Cuenta.objects.filter(tipo_Cuenta=False)
 	cuentas2 = Cuenta.objects.filter(tipo_Cuenta=True)
	ctx = {'cuentas':cuentas, 'cuentas2':cuentas2}
	return render_to_response('home/cuenta.html',ctx,context_instance=RequestContext(request))

def singleTweet_view(request,idtw):
	tweet = Tweet.objects.get(id_Tweet = idtw)
	ctx = {'tweet':tweet}
	return render_to_response('home/singletweet.html',ctx,context_instance=RequestContext(request))

def fechas_view(request):
	info_enviado = False
	fecha1 = '2001-10-10'
	fecha2 = '2014-12-15'
	if request.method == "POST":
		formulario = ContactForm2(request.POST)
		if formulario.is_valid():
			info_enviado = True
			fecha1 = formulario.cleaned_data['FECHA1']
			fecha2 = formulario.cleaned_data['FECHA2']
	else:		
		formulario = ContactForm2()
	tweets = Tweet.objects.filter(fecha__range=(fecha1, fecha2))
	ctx = {'form':formulario,'fecha1':fecha1,'fecha2':fecha2,'info_enviado':info_enviado,'tweets':tweets}
	return render_to_response('home/fecha.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado = False
	hashtag = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			hashtag = formulario.cleaned_data['Texto'] 
	else:		
		formulario = ContactForm()
	tweets = Tweet.objects.filter(texto__icontains = hashtag)
	ctx = {'form':formulario,'hashtag':hashtag,'info_enviado':info_enviado,'tweets':tweets}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))

