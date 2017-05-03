from django.conf.urls import url
from . import views
from django.http import HttpResponseRedirect

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    ##CAVALO È PER PROVARE LE COSE
    url(r'^$', lambda r: HttpResponseRedirect('lista/')),
    ##AMMAZZAMI MALE ↑
    url(r'lista\/(?P<idp>[0-9]+)/?$', views.prodsing, name="prodottosingolo"),
    url(r'lista',views.listaprod,name='listaprodotti'),
]