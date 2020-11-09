from file_manager import FileManager


def lists(a_list, b_list):
    lista = []
    for i in range(len(a_list)):
        if i % 2 == 0:
            lista.append(a_list[i])
    for j in range(len(b_list)):
        if j % 2 == 1:
            lista.append(b_list[j])

    return lista


def getTextData(data_text):
    return {'length': len(data_text), 'letters': list(data_text),
            'big_letters': data_text.upper(),
            'small_letters': data_text.lower()}


def removeLetter(text, letter):
    return text.replace(letter, '')


def convertTemperature(temperature, temperature_type):
    if temperature < -273.15:
        return "Temperatura nie może być niższa niż zero absolutne :>"
    if temperature_type.lower() == "fahrenheit":
        return temperature * 1.8 + 32
    if temperature_type.lower() == "rankine":
        return (temperature + 273.15) * 1.8
    if temperature_type.lower() == "kelvin":
        return temperature + 273.15
    else:
        return "Podano niepoprawny typ temperatury.\nDostępne typy:\
                Fahrenheit, Rankine, Kelvin."


class Calculator:
    def add(self, *args):
        sum = 0
        for arg in args:
            sum += arg
        return sum

    def difference(self, arg1, arg2):
        return arg1 - arg2

    def multiply(self, *args):
        product = 1
        for arg in args:
            product *= arg
        return product

    def divide(self, arg1, arg2):
        if arg2 == 0:
            return "Nie dziel .... przez zero"
        return arg1/arg2


class ScienceCalculator(Calculator):
    def power(self, arg1, arg2):
        return arg1 ** arg2

    def sqrt(self, arg1):
        return arg1 ** (1/2)


def printReverse(text):
    print(text[::-1])


print(lists([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
print(getTextData("Dog"))
print(removeLetter("Dog", "o"))

print(convertTemperature(-273.15, "keLViN"))

calc1 = Calculator()
print(calc1.add(1, 2, 3, 4, 5))
calc2 = ScienceCalculator()
print(calc2.multiply(1, 5))
print(calc2.power(2, 5))
printReverse("koteł")

fm = FileManager("test.txt")
fm.read_file()
fm.update_file("nowa linia")
fm.read_file()
