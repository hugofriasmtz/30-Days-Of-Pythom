# =============================
# Exercises: Level 1
# =============================

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

count = 0
while count <= 10:
    print(count)
    count +=1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

count = 10
while count >= 0:
    print(count)
    count -=1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print('#' * i)

# 4. Use nested loops to create the following:
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# 5. Print the following pattern: Multiplication pattern.
for i in range(11):
    print (f'{i} x {i} = {i*i}')

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
    print(language)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(f'{i} is an even number')

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(f'{i} is an odd number')

# =============================
# Exercises: Level 2
# =============================

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}")

# 1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")

# =============================
# Exercises: Level 3
# =============================

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries import countries

for country in countries:
    if 'land' in country:
        print(country)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)

# 3. Go to the data folder and use the countries_data.py file.
from countries_data import countries_data

#   What are the total number of languages in the data
languages = set()

for country in countries_data:
    for lang in country['languages']:
        languages.add(lang)

print("Total number of languages:", len(languages))

#   Find the ten most spoken languages from the data
from collections import Counter

lang_counter = Counter()

for country in countries_data:
    lang_counter.update(country['languages'])

most_spoken = lang_counter.most_common(10)
print("Top 10 most spoken languages:")
for lang, count in most_spoken:
    print(f"{lang}: {count}")

#   Find the 10 most populated countries in the world
# Sort countries by population in descending order
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Top 10 most populated countries:")
for country in sorted_countries[:10]:
    print(f"{country['name']}: {country['population']}")