
# Crear un conjunto vacío
st = set()  # Crea un conjunto sin elementos

# Crear un conjunto con elementos
st = {'item1', 'item2', 'item3', 'item4'}  # Crea un conjunto con 4 elementos únicos

# Crear un conjunto de frutas
fruits = {'banana', 'orange', 'mango', 'lemon'}  # Conjunto inicial de frutas

# Obtener la longitud del conjunto
len(fruits)  # Devuelve cuántos elementos tiene (4)

# Verificar si un elemento está en el conjunto
print('mango' in fruits)  # True si 'mango' está presente, False si no

# Agregar un solo elemento
fruits.add('lime')  # Agrega 'lime' al conjunto (si no existe ya)

# Agregar varios elementos usando update()
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')  # Tupla de vegetales
fruits.update(vegetables)  # Agrega todos los elementos de 'vegetables' al conjunto 'fruits'

# Eliminar un elemento específico
st = {'item1', 'item2', 'item3', 'item4'}  # Conjunto nuevo
st.remove('item2')  # Elimina 'item2'; si no existe, lanza un error KeyError

# Eliminar un elemento aleatorio con pop()
fruits = {'banana', 'orange', 'mango', 'lemon'}  # Nuevo conjunto
fruits.pop()  # Elimina un elemento aleatorio (ya que no hay orden)

# Guardar el elemento eliminado
removed_item = fruits.pop()  # Elimina y devuelve un elemento aleatorio
print(removed_item)  # Puedes ver cuál fue eliminado

# Vaciar un conjunto
fruits = {'banana', 'orange', 'mango', 'lemon'}  # Se reinicia el conjunto
fruits.clear()  # Elimina todos los elementos del conjunto
print(fruits)  # Muestra set() (conjunto vacío)

# Eliminar completamente el conjunto
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits  # Borra el conjunto de la memoria (ya no existe la variable)

# Convertir lista a conjunto (elimina duplicados)
lst = ['item1', 'item2', 'item3', 'item4', 'item1']  # Lista con duplicado
st = set(lst)  # Convierte a conjunto, eliminando duplicados

# Convertir lista de frutas con duplicados a conjunto
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)  # Elimina duplicados y crea un conjunto

# Unir dos conjuntos (crea uno nuevo sin modificar los originales)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)  # Une ambos conjuntos y devuelve uno nuevo

# Unión de frutas y vegetales
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables))  # Muestra un conjunto con frutas + vegetales

# Agregar el contenido de un conjunto a otro (modifica el original)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)  # Modifica st1 agregando los elementos de st2

# Otra unión de conjuntos usando update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)  # Modifica 'fruits' añadiendo 'vegetables'
print(fruits)  # Muestra el conjunto combinado

# Intersección (elementos comunes entre conjuntos)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)  # Devuelve {'item2', 'item3'}

# Intersección entre números
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)  # Devuelve los números comunes (pares)

# Intersección entre letras de dos palabras
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)  # Devuelve {'o', 'n'} (letras comunes)

# Verificar subconjunto y superconjunto
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)     # True si st2 está contenido dentro de st1
st1.issuperset(st2)   # True si st1 contiene todos los de st2

# Ejemplo con números
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)   # False (los pares no cubren todos)
whole_numbers.issuperset(even_numbers) # True (contiene a los pares)

# Subconjunto entre palabras
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.issubset(dragon)  # False (no está completamente contenido)

# Diferencia (elementos que están en uno pero no en otro)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)  # Devuelve los elementos únicos de st2
st1.difference(st2)  # Devuelve {'item1', 'item4'}

# Diferencia entre números
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers)  # Devuelve los impares

# Diferencia entre palabras
python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)  # Letras que están en 'python' pero no en 'dragon'
dragon.difference(python)  # Letras que están en 'dragon' pero no en 'python'

# Diferencia simétrica (elementos que no se repiten en ambos)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.symmetric_difference(st1)  # Devuelve {'item1', 'item4'}

# Ejemplo con números
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)  # Devuelve los que no están en ambos

# Ejemplo con palabras
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.symmetric_difference(dragon)  # Devuelve las letras diferentes entre ambas palabras

# Verificar conjuntos disjuntos (sin elementos comunes)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)  # False porque tienen elementos en común

# Ejemplo con números pares e impares
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)  # True, no hay elementos comunes

# Ejemplo con palabras
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)  # False, comparten 'o' y 'n'
