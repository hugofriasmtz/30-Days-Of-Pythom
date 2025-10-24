# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
items = ['apple', 'banana', 'cherry', 'orange', 'mango', 'grape']

# 3. Find the length of your list
print("Length of items:", len(items))

# 4. Get the first, middle, and last item of the list
first_item = items[0]
middle_item = items[len(items)//2]
last_item = items[-1]
print(f"First: {first_item} | Middle: {middle_item} | Last: {last_item}")

# 5. Declare a list called mixed_data_types
mixed_data_types = ['Hugo', 25, 1.78, 'Frias', 'QRO']
print(f"Mixed Data Types: {mixed_data_types}")

# 6. Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f"IT Companies: {it_companies}")

# 7. Print the number of companies
print(f"Number of IT companies: {len(it_companies)}")

# 8. Print the first, middle, and last company
print(f"First: {it_companies[0]} | Middle: {it_companies[len(it_companies)//2]} | Last: {it_companies[-1]}")

# 9. Modify one of the companies
it_companies[2] = 'Microsoft Corp'
print(f"Modified list: {it_companies}")

# 10. Add an IT company
it_companies.append('Erwcode')
print(f"After adding one: {it_companies}")

# 11. Insert an IT company in the middle
it_companies.insert(len(it_companies)//2, 'Intel')
print(f"After inserting in the middle: {it_companies}")

# 12. Change one company to uppercase (excluding IBM)
it_companies[1] = it_companies[1].upper()
print(f"Uppercase modification: {it_companies}")

# 13. Join the companies with a string '#; '
joined = '#; '.join(it_companies)
print(f"Joined companies: {joined}")

# 14. Check if a certain company exists
print(f"Does Google exist? {'Google' in it_companies}")

# 15. Sort the list
it_companies.sort()
print(f"Sorted list: {it_companies}")

# 16. Reverse the list
it_companies.reverse()
print(f"Reversed list: {it_companies}")

# 17. Slice out the first 3 companies
print(f"First 3 companies: {it_companies[:3]}")

# 18. Slice out the last 3 companies
print(f"Last 3 companies: {it_companies[-3:]}")

# 19. Slice out the middle company/companies
mid = len(it_companies)//2
print(f"Middle company/companies: {it_companies[mid:mid+1]}")

# 20-24. Remove companies
it_companies.pop(0)
print(f"After removing first: {it_companies}")

it_companies.pop(len(it_companies)//2)
print(f"After removing middle: {it_companies}")

it_companies.pop(-1)
print(f"After removing last: {it_companies}")

it_companies.clear()
print(f"After removing all: {it_companies}")

del it_companies
# print(it_companies)  # would raise an error

# 25-26. Join two lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Full Stack:", full_stack)

# Insert Python and SQL after Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print("Full Stack after insert:", full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()
print(f"Sorted ages: {ages}")

# Find min and max age
min_age, max_age = min(ages), max(ages)
print(f"Min age: {min_age} | Max age: {max_age}")

# Add min and max again to the list
ages.extend([min_age, max_age])
print(f"After adding min and max again: {ages}")

# Find the median age
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print(f"Median age: {median}")

# Find average age
average = sum(ages) / len(ages)
print(f"Average age: {average}")

# Find range of ages
age_range = max_age - min_age
print(f"Range of ages: {age_range}")

# Compare (min - average) and (max - average)
print(f"abs(min - avg): {abs(min_age - average)}")
print(f"abs(max - avg): {abs(max_age - average)}")

# Middle country/countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = len(countries) // 2
print(f"Middle country/countries: {countries[mid:mid+1]}")

# Divide the list into two equal parts
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

# Unpack countries
china, russia, usa, *scandic_countries = countries
print(f"First 3: {china}, {russia}, {usa}")
print(f"Scandic countries: {scandic_countries}")
