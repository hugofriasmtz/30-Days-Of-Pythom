
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b

# ejemplo
print( add_two_numbers(2, 3))


# 2. Area of a circle: area = π x r x r. Write a function area_of_circle.
def area_of_circle(r):
    PI = 3.14
    return PI * r * r

print( area_of_circle(10))


# 3. add_all_nums: takes arbitrary number of arguments, validate types
def add_all_nums(*nums):
    total = 0
    for n in nums:
        if not isinstance(n, (int, float)):
            return 'Error: all arguments must be numbers'
        total += n
    return total

print( add_all_nums(1, 2, 3, 4))


# 4. convert_celsius_to_fahrenheit: °F = (°C x 9/5) + 32
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print( convert_celsius_to_fahrenheit(0))


# 5. check_season(month): returns Autumn/Winter/Spring/Summer
def check_season(month):
    m = month.strip().capitalize()
    if m in ('September', 'October', 'November'):
        return 'Autumn'
    if m in ('December', 'January', 'February'):
        return 'Winter'
    if m in ('March', 'April', 'May'):
        return 'Spring'
    if m in ('June', 'July', 'August'):
        return 'Summer'
    return 'Unknown'

print( check_season('March'))


# 6. calculate_slope(x1, y1, x2, y2): slope of a line
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return 'undefined'
    return (y2 - y1) / (x2 - x1)

print( calculate_slope(1, 2, 3, 4))


# 7. solve_quadratic_eqn(a, b, c): solutions of ax^2 + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return 'Not a quadratic equation'
    disc = b*b - 4*a*c
    if disc >= 0:
        root = disc ** 0.5
        r1 = (-b + root) / (2*a)
        r2 = (-b - root) / (2*a)
        return (r1, r2)
    else:
        root = (-disc) ** 0.5
        real = -b / (2*a)
        imag = root / (2*a)
        return (complex(real, imag), complex(real, -imag))

print( solve_quadratic_eqn(1, 0, -4))


# 8. print_list(lst): prints each element of the list
def print_list(lst):
    for item in lst:
        print(item)

print('print_list ->')
print_list(['a', 'b', 'c'])


# 9. reverse_list(arr): return reversed list using loops
def reverse_list(arr):
    rev = []
    for i in range(len(arr)-1, -1, -1):
        rev.append(arr[i])
    return rev

print('reverse_list ->', reverse_list([1, 2, 3, 4, 5]))
print('reverse_list strings ->', reverse_list(['A', 'B', 'C']))


# 10. capitalize_list_items(items): return list with capitalized items
def capitalize_list_items(items):
    res = []
    for x in items:
        res.append(str(x).capitalize())
    return res

print('capitalize_list_items ->', capitalize_list_items(['potato', 'tomato', 'milk']))


# 11. add_item(lst, item): append item and return list
def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print('11 add_item food ->', add_item(food_staff.copy(), 'Meat'))
numbers = [2, 3, 7, 9]
print('11 add_item numbers ->', add_item(numbers.copy(), 5))


# 12. remove_item(lst, item): return list without the item
def remove_item(lst, item):
    return [x for x in lst if x != item]

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print('remove_item food ->', remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print('remove_item numbers ->', remove_item(numbers, 3))


# 13. sum_of_numbers(n): sum of numbers from 1 to n
def sum_of_numbers(n):
    if n < 0:
        return 'n must be non-negative'
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print('sum_of_numbers 5 ->', sum_of_numbers(5))
print('sum_of_numbers 10 ->', sum_of_numbers(10))


# 14. sum_of_odds(n): sum of odd numbers from 1 to n
def sum_of_odds(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            total += i
    return total

print('sum_of_odds 5 ->', sum_of_odds(5))


# 15. sum_of_even(n): sum of even numbers from 1 to n
def sum_of_even(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
    return total

print('sum_of_even 5 ->', sum_of_even(5))


# Level 2
# 16. evens_and_odds(n): counts evens and odds from 0..n
def evens_and_odds(n):
    if n < 0:
        return 'n must be non-negative'
    evens = 0
    odds = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

e, o = evens_and_odds(100)
print('evens_and_odds 100 -> evens:', e, 'odds:', o)


# 17. factorial(n)
def factorial(n):
    if n < 0:
        return 'n must be non-negative'
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

print('factorial 5 ->', factorial(5))


# 18. is_empty(x): checks if parameter is empty or not
def is_empty(x):
    if x is None:
        return True
    try:
        return len(x) == 0
    except Exception:
        return False

print('is_empty [] ->', is_empty([]))
print('is_empty "" ->', is_empty(''))
print('is_empty None ->', is_empty(None))


# 19. mean, median, mode, range, variance, std (using simple formulas)
def calculate_mean(nums):
    return sum(nums) / len(nums) if nums else None

print('mean [1,2,3,4,5] ->', calculate_mean([1, 2, 3, 4, 5]))


def calculate_median(nums):
    if not nums:
        return None
    s = sorted(nums)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid-1] + s[mid]) / 2

print('median [1,2,3,4] ->', calculate_median([1, 2, 3, 4]))


def calculate_mode(nums):
    if not nums:
        return None
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    return modes[0] if len(modes) == 1 else modes

print('mode [1,2,2,3] ->', calculate_mode([1, 2, 2, 3]))


def calculate_range(nums):
    return max(nums) - min(nums)

print('range [1,5] ->', calculate_range([1, 5]))


def calculate_variance(nums):
    if not nums:
        return None
    m = calculate_mean(nums)
    n = len(nums)
    s = 0
    for x in nums:
        s += (x - m) ** 2
    return s / n

print('variance [1,2,3] ->', calculate_variance([1, 2, 3]))


def calculate_std(nums):
    var = calculate_variance(nums)
    return var ** 0.5 if var is not None else None

print('std [1,2,3] ->', calculate_std([1, 2, 3]))


# Level 3
# 20. is_prime(n)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

print('is_prime 17 ->', is_prime(17))


# 21. all_unique(lst)
def all_unique(lst):
    return len(set(lst)) == len(lst)

print('all_unique [1,2,3] ->', all_unique([1, 2, 3]))
print('all_unique [1,2,2] ->', all_unique([1, 2, 2]))


# 22. same_type(lst): True if all items have same data type
def same_type(lst):
    if not lst:
        return True
    t = type(lst[0])
    for x in lst:
        if type(x) is not t:
            return False
    return True

print('same_type [1,2,3] ->', same_type([1, 2, 3]))
print('same_type [1,"a"] ->', same_type([1, 'a']))


# 23. is_valid_variable(name): check if provided variable is a valid Python identifier
def is_valid_variable(name):
    if not isinstance(name, str):
        return False
    if not name.isidentifier():
        return False
    keywords = ('def', 'class', 'if', 'else', 'for', 'while', 'return', 'import', 'from', 'as', 'with', 'try', 'except', 'finally', 'lambda', 'nonlocal', 'global', 'pass', 'break', 'continue', 'and', 'or', 'not', 'in', 'is', 'yield', 'assert', 'del', 'raise', 'True', 'False', 'None')
    if name in keywords:
        return False
    return True

print('is_valid_variable var1 ->', is_valid_variable('var1'))
print('is_valid_variable 1var ->', is_valid_variable('1var'))


# 24. most_spoken_languages(countries, top=10): returns top languages by count
def most_spoken_languages(countries, top=10):
    counts = {}
    for c in countries:
        for lang in c.get('languages', []):
            counts[lang] = counts.get(lang, 0) + 1
    items = sorted(list(counts.items()), key=lambda x: x[1], reverse=True)
    return items[:top]

# usar el archivo local `countries_data.py` (debe encontrarse en la misma carpeta)
from countries_data import countries_data as countries_list

print('most_spoken_languages (top 10) ->', most_spoken_languages(countries_list, top=10))


# 25. most_populated_countries(countries, top=10): returns top countries by population
def most_populated_countries(countries, top=10):
    items = []
    for c in countries:
        items.append((c.get('name'), c.get('population', 0)))
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:top]

print('most_populated_countries (top 10) ->', most_populated_countries(countries_list, top=10))

