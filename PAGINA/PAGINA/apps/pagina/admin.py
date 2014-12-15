from django.contrib import admin
from PAGINA.apps.pagina.models import Cuenta,Etiqueta,Contiene,Tweet
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Tweet)
admin.site.register(Etiqueta)
admin.site.register(Contiene)
