# 1
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sagittis viverra justo ut euismod. Nullam " \
       "porttitor consequat dolor at consectetur. Donec at viverra metus. Aliquam vel eleifend mauris. Suspendisse " \
       "pulvinar pharetra tristique. Nunc viverra urna eu scelerisque porta. Suspendisse in maximus magna, " \
       "ac aliquet massa. "

# 2
imie = "Dominik"
imiec = text.count(imie[1])
nazwisko = "Saczuk"
nazwiskoc = text.count(nazwisko[2])
text1 = "W tekście jest {0} liter {1} oraz {2} liter {3}.".format(imiec, imie[1], nazwiskoc, nazwisko[2])
print(text1)

# 3 - in other file

# 4
text2 = "test"
print(dir(text2))
help(text2.split)

# 5
print(imie[::-1].title() + " " + nazwisko[::-1].title())

# 6
listap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = listap[5:]
del listap[5:]
print(listap)
print(list1)

# 7
list2 = listap + list1
list2.insert(0, 0)
list3 = list2
list3.sort(reverse=True)
print(list3)

# 8
krotka = ((15423, "Jacek Kowalski"), (23432, "Marian Takise"), (23478, "Andrzej Bjerecki"))
slownik = dict((y, x) for x, y in krotka)

# 9


# 10
listt = [333666999, 333666999, 555666777, 666555777, 666555777]
listt = set(listt)
print(listt)

# 11
for n in range(1, 11):
    print(n)

# 12
for n in range(100, 19, -5):
    print(n)

# 13
jedenstring = ""
lista13 = [{'jacek': 2}, {"ryszard": 5}, {"mateusz": 7}]
z = len(lista13)
for n in range(z):
    for x, y in lista13[n].items():
        jedenstring += "{} {} ".format(x, y)
print(jedenstring)
