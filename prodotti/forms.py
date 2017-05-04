from django import  forms

class addform(forms.Form):
    nome=forms.CharField(label="Nome",max_length=100)
    prezzo=forms.IntegerField(label="Prezzo")
    qdisp=forms.IntegerField(label="Quantità")
    descr=forms.CharField(label="Descrizione",widget=forms.Textarea)
    tag=forms.CharField(label="tag",widget=forms.Textarea)

class intform(forms.Form):
    data=forms.IntegerField()