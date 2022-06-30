from django.shortcuts import render
from django.http import HttpResponse
from .models import Oferty, Poziom
# Create your views here.
"""
Utworzenie i zdefiniowanie zapytań dla metody index
"""
def index(request):
    #zapytanie= Oferty.objects.all()
    #wszystkie   =Oferty.objects.all()
    #jeden       =Oferty.objects.get(pk=3)
    #poz         =Oferty.objects.filter(poziom=1)
    #korepetytor_name =Oferty.objects.filter(korepetytor=3)
    #null        =Oferty.objects.filter(poziom__isnull=False)
    #zawiera     =Oferty.objects.filter(opis__icontains='szkoły')
    #test        =Oferty.objects.all(pk=1)
    #poz_name   =Poziom.objects.get(id=1)
    #oferty      =Oferty.objects.all()
    poziomy = Poziom.objects.all()
    dane={'poziomy': poziomy}
    return render(request, 'szablon.html',  dane)

    #context={ 'wszystkie': wszystkie,
              #'poziomy': poziomy}
    #return render(request, 'szablon.html', context)
"""
Utworzenie i zdefiniowanie zapytań dla metody poziom
"""
def poziom(request, id):
    poziomy = Poziom.objects.all()
    poziom_user = Poziom.objects.get(pk=id)
    poziom_oferta = Oferty.objects.filter(poziom = poziom_user)
    dane = {'poziom_user': poziom_user,
            'poziom_oferta': poziom_oferta,
            'Poziomy': poziomy}
    return render(request, 'poziom_oferta.html',dane)
    #return HttpResponse(poziom_user)

"""
Utworzenie i zdefiniowanie zapytań dla metody oferta
"""
def oferta(request, id):
    oferta_user = Oferty.objects.get(pk=id)
    poziomy = Poziom.objects.all()
    #napis = "<h1>" + str(oferta_user) + "</h1>" + \
    #       "<p>" + str(oferta_user.opis) + "</p>" + \
    #      "<p>" + str(oferta_user.cena) + "</p>"
    dane={'oferta_user': oferta_user,'poziomy': poziomy }
    return render(request, 'oferta.html',dane)
    #return HttpResponse(napis)

"""
Utworzenie i zdefiniowanie zapytania dla metody logowanie
"""
def logowanie(request):
    return render(request,'templates/logowanie.html')
    #return HttpResponse('logowanie.html')