from django.db import models

# Create your models here.
"""
Klasa Korepetytor przechowuje ponizej zdefiniowane metode str oraz pola( nazwa, opis)
"""
class Korepetytor(models.Model):
    # Metoda zwraca nazwe wpisu
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name="Korepetytor"
        verbose_name_plural="Korepetytorzy"

"""
Klasa Poziom przechowuje ponizej zdefiniowane metode str oraz pola( )
"""
'''
@:param xxx
@:return xxx
'''

class Poziom(models.Model):
    # Metoda zwraca nazwe wpisu
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)

    class Meta:
        verbose_name="Poziom"
        verbose_name_plural="Poziomy"

"""
Klasa Oferty przechowuje ponizej zdefiniowane metode str oraz pola( poziom, korepetytor, nazwa, opis, cena)
"""
class Oferty(models.Model):
    # Metoda zwraca nazwe wpisu
    def __str__(self):
        return self.nazwa

    poziom = models.ForeignKey(Poziom,blank=True,on_delete=models.CASCADE,null=True)
    korepetytor = models.ForeignKey(Korepetytor,on_delete=models.CASCADE,null=True)
    nazwa = models.CharField(max_length=60)
    opis=models.TextField(blank=True)
    cena=models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name="Oferta"
        verbose_name_plural="Oferty"
"""
Klasa Konto przechowuje ponizej zdefiniowane pola( przedmiot, imie, nazwisko, opis, cena)
"""

class Konto(models.Model):
    #Metoda zwraca nazwe wpisu
    def __str__(self):
        return self.nazwakor
    przedmiot = models.CharField(max_length=60)
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    opis=models.TextField(blank=True)
    cena=models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name="O"
        verbose_name_plural="Oferty"

