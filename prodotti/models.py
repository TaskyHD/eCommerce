from django.db import models

# Create your models here.
class Prodotto(models.Model):
    imgUrl = models.CharField(max_length=200)
    nome = models.CharField(max_length=100)
    descr = models.TextField(max_length=1000)
    prezzo = models.DecimalField(decimal_places=2, max_digits=20)
    qdisp=models.DecimalField(decimal_places=0,max_digits=5)
    tag=models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.nome
    def getimgdir(self):
        return "prodotti/"+self.imgUrl
    def create(img,nnome,descri,nprezzo,nqdisp,ntag=""):
        return Prodotto(imgUrl=img,nome=nnome,descr=descri,prezzo=nprezzo,qdisp=nqdisp,tag=ntag)

    #size ratio min(maxwidth/width, maxheight/height)
    #size= oldsize*ratio