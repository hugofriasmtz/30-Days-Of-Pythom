
# 1. Crea una tupla vacía
empty_tuple = ()
print(
    empty_tuple)

# 2. Crea una tupla que contenga los nombres de tus hermanas y tus hermanos
brothers = ("Erwin", "Marcos")
sisters = ("Camila","Paula")
print(f"Sisters: {sisters}")
print(f"Brothers: {brothers}")

# 3. Unir tuplas de hermanos y hermanas y asignarlo a brothers
siblings = sisters + brothers
print(f"{siblings}")

# 4. ¿Cuántos hermanos tienes?
print(f"Size: {len(siblings)}")

# 5. Modifica la tupla de hermanos y agrega el nombre del padre y la madre y asígnalo a family_members
father = ("Felipe",)
mother = ("NO_Name",)
family_members = siblings + father + mother
print(f"Family members: {family_members}")


# 6. Desempaquetar hermanos y padres de family_members
*siblings_unpacked, dad, mom = family_members
print(f"Siblings desempaquetados: {siblings_unpacked}")
print(f"   Padre: {dad}")
print(f"   Madre: {mom}")

# 7. Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a food_stuff_tp
fruits = ("apple", "banana", "orange")
vegetables = ("tomato", "potato", "cabbage")
animal_products = ("milk", "eggs", "cheese")
food_stuff_tp = fruits + vegetables + animal_products
print(f"food_stuff_tp: {food_stuff_tp}")

# 8. Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print(f"food_stuff_lt (lista): {food_stuff_lt}")



# 10. Corte los primeros tres elementos y los últimos tres elementos de la lista food_stuff_lt
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"Primeros tres en food_stuff_lt: {first_three}")
print(f"Últimos tres en food_stuff_lt: {last_three}")

# 11. Elimine la tupla food_stuff_tp por completo
del food_stuff_tp

# 12. Comprueba si existe un elemento en la tupla:
# (como food_stuff_tp fue eliminado, comprobamos en la lista food_stuff_lt)
item_check = "banana"
print(f"¿Existe '{item_check}' en food_stuff_lt?", item_check in food_stuff_lt)

# 13. Comprueba si 'Estonia' es un país nórdico
# 14. Comprueba si 'Islandia' es un país nórdico

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

