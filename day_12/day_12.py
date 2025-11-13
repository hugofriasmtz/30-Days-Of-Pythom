
# 1. Importing a Module
import mymodule 
print(mymodule.generate_full_name('Hugo', 'Frias')) # Hugo Frias

# 2. Import Functions from a Module

from mymodule import generate_full_name, sum_two_nums, person, gravity # Importa funciones y variables específicas
print(generate_full_name('Hugo','Frias')) # Hugo Frias
print(sum_two_nums(10,21)) # 31
mass = 100
weight = mass * gravity 

print(weight)
print(person['firstname'])

# 3. Import Functions from a Module and Renaming

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Hugo','Frias'))
print(total(10, 21))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

# Import Built-in Modules
# Like other programming languages we can also import modules by importing the file/function using the key word import.
#  Let's import the common module we will use most of the time. 
# Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

# 3.1 OS Module

# import the module
import os
# Creating a directory
# os.mkdir('directory_name')  # COMENTADO: crea una carpeta; descomenta sólo para pruebas controladas
# Changing the current directory
# os.chdir('path')  # COMENTADO: cambia el directorio actual; descomenta sólo si existe la ruta
# Getting current working directory
print('CWD actual:', os.getcwd())  # sólo lectura, no modifica el sistema
# Removing directory
# os.rmdir('directory_name')  # COMENTADO: elimina carpeta (debe estar vacía); descomenta con cuidado

# 3.2 Sys Module

import sys
# print(sys.argv[0], sys.argv[1], sys.argv[2])  # ejemplo: filename argument1 argument2
if len(sys.argv) >= 3:
	print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
else:
	print('Tip: run as -> python day_12/day_12.py <name> <challenge>')

# 4. Statistics Module

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# 5. Math Module
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

# Nota: Los ejercicios prácticos de este día están en `day_12/exercise.py`

# 5.1 If we want to import only a specific function from the module we import it as follows:
from math import pi
print(pi)

# 5.2 It is also possible to import multiple functions at once

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

# 5.3 But if we want to import all the function in math module we can use * .

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

# 5.4 When we import we can also rename the name of the function.

from math import pi as  PI
print(PI) # 3.141592653589793

# 6 String Module

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# Random Module
# By now you are familiar with importing modules. Let us do one more import to get very familiar with it. 
# Let us import random module which gives us a random number between 0 and 0.9999.... The random module 
# has lots of functions but in this section we will only use random and randint

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive