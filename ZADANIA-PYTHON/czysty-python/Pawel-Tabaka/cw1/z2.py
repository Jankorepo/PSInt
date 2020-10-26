from datetime import datetime

imie_nazwisko = "Paweł Tabaka"
print("{:^18}".format(imie_nazwisko))
pi = 3.14159265359
print("{:.2f}".format(pi))
print("{:.7}".format(imie_nazwisko))
print("{:%Y-%m-%d}".format(datetime.now()))
print("{:*>20}".format(imie_nazwisko))
