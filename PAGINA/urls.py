from django.conf.urls import patterns, include, url

from django.contrib import admnin
admin.autodiscover()

urlpatterns = patterns(' ',
	url(r'^admin/', include(admin.site.urls)),

)

