from datetime import date
text = "testy"
print('{:.4}'.format(text))
liczba = 643.21321
print('{:.1f}'.format(liczba))
text2 = "to"
print('{0} {1} {0}'.format(text2, text))
dzis = date.today()
print('{0}'.format(dzis))
list = [1, 2, 3]
print('{[1]}'.format(list))