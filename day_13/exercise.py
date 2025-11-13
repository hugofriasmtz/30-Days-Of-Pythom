
# 1 Filtrar solo los negativos y el cero en la lista
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [i for i in numbers if i <= 0]
print(negatives_and_zero)          # [-4, -3, -2, -1, 0]


# 2 Aplanar una lista de listas de listas
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flattened)                   # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 3 Crear lista de tuplas con potencias usando list comprehension

powers = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(powers)


# 4 Aplanar lista de países a una lista con formato personalizado
countries = [[('Mexico', 'Cuidad de Mexico')], [('Colombia', 'Bogota')], [('Italia', 'Roma')]]
formatted = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]
print(formatted)



# 5 Convertir lista de países a lista de diccionarios
countries = [[('Mexico', 'Cuidad de Mexico')], [('Colombia', 'Bogota')], [('Italia', 'Roma')]]
country_dicts = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]
print(country_dicts)


# 6 Convertir lista de listas a lista de cadenas concatenadas
names = [[('Hugo', 'Frias')], [('Marcos', 'Frias')], [('Erwin', 'Frias')], [('Felipe', 'Frias')]]
full_names = [f"{first} {last}" for [(first, last)] in names]
print(full_names) 


# 7 Función lambda para pendiente (slope) e intersección (y-intercept)


# slope = (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(2, 4, 6, 8))          # 1.0

# intersección con el eje y: b = y - m*x
intercept = lambda x, y, m: y - m * x
print(intercept(2, 4, 1))         # 2