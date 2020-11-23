from django.db import models

# Create your models here.


class Stanowisko(models.Model):
    _id = models.DecimalField(max_digits=5, decimal_places=0)
    nazwa = models.CharField(max_length=45)
    tworzy_uzytkownika = models.BooleanField()
    modyfikuje_uzytkownika = models.BooleanField()
    usuwa_uzytkowinka = models.BooleanField()
    tworzy_spotkanie = models.BooleanField()
    modyfikuje_spotkanie = models.BooleanField()
    usuwa_spotkanie = models.BooleanField()
    wyswietla_spotkanie = models.BooleanField()


class Salon(models.Model):
    _id = models.DecimalField(max_digits=5, decimal_places=0)
    miasto = models.CharField(max_length=45, null=False)
    adres = models.CharField(max_length=45, null=False)
    kierownik_id = models.ManyToManyField('Pracownik')


class Pracownik(models.Model):
    _id = models.DecimalField(max_digits=5, decimal_places=0)
    imie = models.CharField(max_length=60, null=False)
    nazwisko = models.CharField(max_length=60, null=False)
    login = models.CharField(max_length=32, null=False)
    haslo_hash = models.CharField(max_length=256, null=False)
    pensja_podstawowa = models.DecimalField(max_digits=9, decimal_places=2,
                                            default=2800)
    stanowiska_id = models.ForeignKey('Stanowisko',
                                      on_delete=models.SET_NULL, default=1, null=True)
    salony_id = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True)


class Wizyta(models.Model):
    _id = models.DecimalField(max_digits=5, decimal_places=0)
    data = models.DateField()
    klienci_id = models.ForeignKey('Klient', on_delete=models.SET_NULL, null=True), 
    pracownicy_id = models.ForeignKey('Pracownik', on_delete=models.SET_NULL, null=True)
    salony_id = models.ForeignKey('Salon', on_delete=models.SET_NULL, null=True)





