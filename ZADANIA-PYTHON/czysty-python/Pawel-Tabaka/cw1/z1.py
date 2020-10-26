# ZADANIE 1 i 2

lorem = "Lorem Ipsum jest tekstem stosowanym jako  przykładowy wypełniacz w \
    przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez \
    nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć \
    wieków później zaczął być używany przemyśle elektronicznym, pozostając \
    praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z \
    publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a \
    ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem \
    przeznaczonym do realizacji druków na komputerach osobistych, jak \
    Aldus PageMaker"

imie = "Paweł"
nazwisko = "Tabaka"
print("W tekście jest {} liter {} oraz {} liter {}."
      .format(lorem.count(nazwisko[2]),
              nazwisko[2], lorem.count(imie[1]), imie[1]))

# ZADANIE 4

tekst = "Jakiś string"

print(dir(tekst))
help(tekst.translate)

# ZADANIE 5

print("paweł tabaka"[::-1].title())

# ZADANIE 6 i 7

lista = [i for i in range(1, 11)]

lista_nowa = lista[5:]
lista = lista[:5]

print(lista)
print(lista_nowa)

lista = [0] + lista + lista_nowa
print(lista)

kopia_listy = lista
kopia_listy.sort(reverse=True)
print(kopia_listy)

# ZADANIE 8 i 9

lista_studentow = [("123456", "Student Pierwszy"), ("654321", "Student Drugi"),
                   ("321654", "Student Trzeci")]
print(lista_studentow)

lista_studentow_slownik = []

for i in range(len(lista_studentow)):
    lista_studentow_slownik.append({"numer albumu": lista_studentow[i][0],
                                    "dane": lista_studentow[i][1]})

print(lista_studentow_slownik)

dodatkowe_dane = [("20", "studentpierwszy@mail.com", "Stołowa 8"),
                  ("21", "studentdrugi@mail.com", "Dolna 7"),
                  ("21", "studenttrzeci@mail.com", "Metalowa 8")]

for i in range(len(lista_studentow)):
    lista_studentow_slownik[i]["wiek"] = dodatkowe_dane[i][0]
    lista_studentow_slownik[i]["mail"] = dodatkowe_dane[i][1]
    lista_studentow_slownik[i]["adres"] = dodatkowe_dane[i][2]

print(lista_studentow_slownik)

# ZADANIE 10

numery_telefonow = ["123456789", "123456789", "987654321", "987654321",
                    "123654789"]
numery_telefonow = set(numery_telefonow)
print(numery_telefonow)

# ZADANIE 11

for i in range(1, 11):
    print(i)

# ZADANIE 12

for i in range(100, 19, -5):
    print(i)

# ZADANIE 13
# WYKORZYSTAŁEM LISTĘ ZE SŁOWNIKAMI, KTÓRE ZAWIERAJĄ DANE STUDENTÓW

for i in range(len(lista_studentow_slownik)):
    for k, v in lista_studentow_slownik[i].items():
        print("{} studenta numer {} to {}".format(k, i+1, v))
    print("\n")
