# 1
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sagittis viverra justo ut euismod. Nullam " \
       "porttitor consequat dolor at consectetur. Donec at viverra metus. Aliquam vel eleifend mauris. Suspendisse " \
       "pulvinar pharetra tristique. Nunc viverra urna eu scelerisque porta. Suspendisse in maximus magna, " \
       "ac aliquet massa. "

# 2
#text1 = "W tekście jest {} liter oraz {} liter."
#ERROR

# 3 - in other file

# 4
text2 = "test"
print(dir(text2))
help(text2.split)

# 5
imie = "Dominik"
nazwisko = "Saczuk"
print(imie[::-1].title() + " " + nazwisko[::-1].title())

# 6
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = list[5:]
del list[5:]
print(list)
print(list1)

# 7
list2 = list + list1
list2.insert(0, 0)
list3 = list2
list3.sort(reverse=True)
print(list3)

# 8
krotka = ((15423, "Jacek Kowalski"),(23432, "Marian Takise"),(23478, "Andrzej Bjerecki"))
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
