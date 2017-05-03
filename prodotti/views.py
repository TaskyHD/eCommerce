from django.shortcuts import render,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def listaprod(request):
    context={}
    return render(request,"prodotti/lista.html",context)