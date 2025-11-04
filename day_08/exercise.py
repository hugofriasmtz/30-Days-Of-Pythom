# 1. Crear un diccionario vacío llamado dog
dog = {}

# 2. Agregar name, color, breed, legs, age al diccionario dog
dog['name'] = 'Max'
dog['color'] = 'Negro'
dog['breed'] = 'Pastor Alemán'
dog['legs'] = 4
dog['age'] = 6

# 3. Crear un diccionario llamado student con las siguientes claves
student = {
    'first_name': 'Hugo',
    'last_name': 'Frias',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python'],
    'country': 'Mexico',
    'city': 'Querétaro',
    'address': '123 15 de Mayo'
}

# 4. Obtener la longitud del diccionario student
print(len(student))

# 5. Obtener el valor de skills y verificar el tipo de dato
skills = student['skills']
print(skills)
print("Tipo de dato:", type(skills))  # Debe ser <class 'list'>

# 6. Modificar skills usando append()
student['skills'].append('HTML')
student['skills'].append('CSS')
# 6.1. Alternativa usando extend()
student['skills'].extend(['Git', 'Docker'])

# 7. Obtener las claves del diccionario como lista
keys = list(student.keys())
print(keys)

# 8. Obtener los valores del diccionario como lista
values = list(student.values())
print(values)

# 9. Convertir el diccionario en una lista de tuplas usando items()
items = list(student.items())
print(items)

# 10. Eliminar un elemento del diccionario (por ejemplo, marital_status)
del student['marital_status']
print(student)

# 11. Eliminar uno de los diccionarios (por ejemplo, dog)
del dog
# print(dog)  # Esto causaría error porque dog ya no existe

# 12. Ejemplo de .pop(clave) — elimina un elemento específico
edad = student.pop('age')
print(edad)
print(student)

# 13. Ejemplo de .popitem() — elimina el último elemento insertado
ultimo = student.popitem()
print(ultimo)
print(student)
