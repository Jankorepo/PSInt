from django.contrib import admin
from .models import Pracownik, Salon, Wizyta, Stanowisko, Klient, Użytkownik, Dostawa
# Register your models here.

admin.site.register(Pracownik)
admin.site.register(Salon)
admin.site.register(Wizyta)
admin.site.register(Stanowisko)
admin.site.register(Klient)
admin.site.register(Użytkownik)
admin.site.register(Dostawa)