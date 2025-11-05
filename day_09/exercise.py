
# 1 Edad para aprender a conducir
age = int(input('Enter your age: '))
if age >= 18:
	print('You are old enough to learn to drive.')
else:
	missing = 18 - age
	print(f'You need {missing} more year{"s" if missing != 1 else ""} to learn to drive.')

# 2 Comparar my_age y your_age
my_age = 30
your_age = int(input('Enter your age: '))
if your_age > my_age:
	diff = your_age - my_age
	print(f'You are {diff} year{"s" if diff != 1 else ""} older than me.')
elif your_age < my_age:
	diff = my_age - your_age
	print(f'I am {diff} year{"s" if diff != 1 else ""} older than you.')
else:
	print('We are the same age.')

# 3 Comparar dos números
a = float(input('Enter number one: '))
b = float(input('Enter number two: '))
if a > b:
	print(f'{a} is greater than {b}')
elif a < b:
	print(f'{a} is smaller than {b}')
else:
	print(f'{a} is equal to {b}')



# 1 Calificación por score
score = float(input('Enter score (0-100): '))
if 80 <= score <= 100:
	print('Grade: A')
elif 70 <= score <= 89:
	print('Grade: B')
elif 60 <= score <= 69:
	print('Grade: C')
elif 50 <= score <= 59:
	print('Grade: D')
else:
	print('Grade: F')

# 2 Determinar estación por mes
month = input('Enter month: ').strip().capitalize()
if month in ('September', 'October', 'November'):
	print('Season: Autumn')
elif month in ('December', 'January', 'February'):
	print('Season: Winter')
elif month in ('March', 'April', 'May'):
	print('Season: Spring')
elif month in ('June', 'July', 'August'):
	print('Season: Summer')
else:
	print('Season: Unknown')

# 3) Lista de frutas: añadir si no existe
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').strip()
if fruit in fruits:
	print('That fruit already exist in the list')
else:
	fruits.append(fruit)
	print(f'Modified list: {fruits}')




person = {
	'first_name': 'Hugo',
	'last_name': 'Frias',
	'age': 22,
	'country': 'Mexico',
	'is_married': False,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': '15 de Mayo',
		'zipcode': '101010'
	}
}

# a Si existe 'skills', imprimir la skill del medio
skills = person.get('skills')
if skills:
	mid = len(skills) // 2
	print('Middle skill:', skills[mid])

# b Comprobar si tiene 'Python'
print("Has 'Python' skill?", 'Python' in skills if skills else False)

# c Determinar título según skills (reglas simples)
s = set(skills or [])
title = 'unknown title'
if s == {'JavaScript', 'React'}:
	title = 'He is a front end developer'
elif {'Node', 'Python', 'MongoDB'}.issubset(s):
	title = 'He is a backend developer'
elif {'React', 'Node', 'MongoDB'}.issubset(s):
	title = 'He is a fullstack developer'
print('Title guess:', title)

# d Si está casado y vive en Mexico, imprimir la frase
if person.get('is_married') and person.get('country') == 'Mexico':
	print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")
