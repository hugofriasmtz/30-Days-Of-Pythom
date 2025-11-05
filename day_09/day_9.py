# If Condition
a = 3
if a > 0:
    print('A is a positive number')

# If Else
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# If Elif Else
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Short Hand
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# If Condition and Logical Operators
a = 0
# Operador 'and': devuelve True si ambas condiciones son True.
# En Python 'and' evalúa de izquierda a derecha y hace short-circuit:
# si la primera condición es False no evalúa la segunda (optimización).
#
# Operador 'not': invierte el valor booleano (not True -> False).
#
# Se pueden encadenar varias condiciones con and/or y usar paréntesis
# para controlar la precedencia: (cond1 and cond2) or cond3.
#
# Atención: '&' es un operador bit a bit (no lo uses para lógica booleana
# salvo que sepas lo que haces). Para comparaciones booleanas usa 'and'/'or'.
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
# Operador 'or': devuelve True si al menos una condición es True.
# Igual que 'and', 'or' hace short-circuit: si la primera es True no evalúa la segunda.
#
# Ejemplo de uso mixto: user == 'admin' or access_level >= 4
#  - Si user == 'admin' es True, Python no evalúa access_level >= 4.
#
# Nota sobre precedencia: 'and' tiene mayor precedencia que 'or',
# por eso 'a or b and c' se interpreta como 'a or (b and c)'. Usa paréntesis
# si quieres un orden distinto.
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')

