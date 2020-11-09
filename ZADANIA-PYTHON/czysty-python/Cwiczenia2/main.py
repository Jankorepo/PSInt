# 1
print("########## Zadanie 1 ##########")
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def funkcja(a_list, b_list):
    c_list = []
    for x in a_list:
        if a_list.index(x) % 2 == 0:
            c_list.append(x)
    for x in b_list:
        if b_list.index(x) % 2 == 1:
            c_list.append(x)
    return (c_list)

nowa_lista = funkcja(a_list, b_list)
print(nowa_lista)

# 2
print("########## Zadanie 2 ##########")
data_text = "kott"
def funkcja2(data_text):
    slownik_data = dict()
    slownik_data['dlugosc'] = len(data_text)
    for x in data_text:
        slownik_data[x] = slownik_data.get(x, 0) + 1
    slownik_data['duzy'] = data_text.upper()
    slownik_data['maly'] = data_text.lower()
    return(slownik_data)

print(funkcja2(data_text))

# 3
print("########## Zadanie 3 ##########")
text = "Kot ma ale"
letter = "a"
def funkcja3(text, letter):
    lista = []
    for x in text:
        for y in letter:
            if x != y:
                lista.append(x)
    return lista
print(''.join(funkcja3(text, letter)))

# 4
print("########## Zadanie 4 ##########")
def funkcja4(temperature_type, celsjusze):
    if temperature_type == "c":
        return celsjusze
    if temperature_type == "f":
        return (celsjusze * 9/5) + 32
    if temperature_type == "k":
        return (celsjusze + 273.15)
    if temperature_type == "r":
        return (celsjusze + 273.15) * 9 / 5
    else:
        return "Błąd"

print(funkcja4("f", 23))

# 5
