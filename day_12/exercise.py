

import random
import string



# 1 random_user_id: generar un id aleatorio de 6 caracteres (a-z0-9)
def random_user_id():
    chars = string.ascii_letters + string.digits
    user_id = ''
    for i in range(6):
        user_id += random.choice(chars)
    return user_id
print(random_user_id())  # ejemplo: '1ee33d'



# 2 user_id_gen_by_user: pide por input() "<num_chars> <num_ids>" y genera ese número de IDs
def user_id_gen_by_user():
    chars = string.ascii_letters + string.digits
    num_chars = int(input("Ingrese el número de caracteres: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))

    for i in range(num_ids):
        user_id = ''
        for j in range(num_chars):
            user_id += random.choice(chars)
        print(user_id)
print(user_id_gen_by_user())


# rgb_color_gen: genera un color en formato 'rgb(r,g,b)' con r,g,b en 0..255
def rgb_color_gen():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return f'rgb({r},{g},{b})'
print(rgb_color_gen())

# Nivel 2

# 1 list_of_hexa_colors(n): devuelve lista de n colores hex '#rrggbb'
def list_of_hexa_colors(n):
    colors = []
    for i in range(n):
        hex_color = '#'
        for j in range(6):
            hex_color += random.choice('0123456789abcdef')
        colors.append(hex_color)
    return colors
print(list_of_hexa_colors(3))



# 2 list_of_rgb_colors(n): devuelve lista de n colores 'rgb(r,g,b)'
def list_of_rgb_colors(n):
	res = []
	for _ in range(n):
		res.append(rgb_color_gen())
	return res


# 3 generate_colors(type, n): genera n colores en formato hexa o rgb
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Tipo de color no válido"
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 2))


# Nivel 3
# 7) shuffle_list(lst): devolver una lista barajada (sin mutar la original)
def shuffle_list(lista):
    random.shuffle(lista)
    return lista


print(shuffle_list([1, 2, 3, 4, 5, 6]))



# 8️ Función que genera 7 números aleatorios únicos entre 0 y 9
def unique_random_numbers():
    numbers = []
    while len(numbers) < 7:
        num = random.randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    return numbers
print(unique_random_numbers())  # ejemplo: [3, 0, 7, 5, 2, 8, 4]