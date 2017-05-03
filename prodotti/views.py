from django.shortcuts import render,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from .models import Prodotto

# Create your views here.
def index(request):
    template = loader.get_template('prodotti/lista.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listaprod(request):
    prod=Prodotto.objects.get(id=1);
    context={"nome":prod.nome,"prezzo":prod.prezzo,"img":prod.imgUrl}
    return render(request,"prodotti/lista.html",context)
def prodsing(request,id):
    prod = Prodotto.objects.get(id=1);
    context = {"nome": prod.nome, "prezzo": prod.prezzo, "img": prod.imgUrl,"descr":prod.descr}
    return render(request, "prodotti/lista.html", context)