from django.shortcuts import *
from django.http import *
from .models import Prodotto
from .forms import *

# Create your views here.
def index(request):
    template = loader.get_template('prodotti/lista.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listaprod(request):
    context={"prodotti": Prodotto.objects.all()}
    if request.method=="POST":
        prod=request.POST.get("item")
        return redirect("prodottosingolo",idp=prod)
    else:
        return render(request,"prodotti/lista.html",context)

def prodsing(request,idp):
    prod = Prodotto.objects.get(id=idp)
    context = {"nome": prod.nome, "prezzo": prod.prezzo, "img":prod.getimgdir(),"descr":prod.descr,"disp":prod.qdisp}
    return render(request, "prodotti/prodotto.html", context)

def addprod(request):
    if request.method=="POST":
        form=addform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/cacchio/")
    else :
        form=addform()
    return  render(request,"prodotti/aggiungiprod.html",{"addform":form})
    # size ratio min(maxwidth/width, maxheight/height)
    # size= oldsize*ratio