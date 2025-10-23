

# 1. Concatenate strings
part1, part2, part3, part4 = 'Thirty', 'Days', 'Of', 'Python'
full_sentence = part1 + ' ' + part2 + ' ' + part3 + ' ' + part4
print(full_sentence)

# 2. Concatenate other strings
text = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(text)

# 3. Declare variable
company = "Coding For All"

# 4. Print variable
print(company)

# 5. Length of string
print(len(company))

# 6. Uppercase
print(company.upper())

# 7. Lowercase
print(company.lower())

# 8. capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Slice out the first word
print(company[7:])  # removes 'Coding '

# 10. Check if contains 'Coding'
print('Coding' in company)

# 11. Replace 'Coding' with 'Python'
print(company.replace('Coding', 'Python'))

# 12. Change 'Python for Everyone' to 'Python for All'
print('Python for Everyone'.replace('Everyone', 'All'))

# 13. Split the string
print(company.split())

# 14. Split by commas
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# 15. Character at index 0
print(company[0])

# 16. Last index
print(len(company) - 1)

# 17. Character at index 10
print(company[10])

# 18. Acronym of 'Python For Everyone'
phrase = 'Python For Everyone'
acronym = ''.join(word[0].upper() for word in phrase.split())
print(acronym)

# 19. Acronym of 'Coding For All'
phrase2 = 'Coding For All'
acronym2 = ''.join(word[0].upper() for word in phrase2.split())
print(acronym2)

# 20. First occurrence of 'C'
print(company.index('C'))

# 21. First occurrence of 'F'
print(company.index('F'))

# 22. Last occurrence of 'l'
print('Coding For All People'.rfind('l'))

# 23–25. Sentences with 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rindex('because'))
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])  # prints 'because because because'

# 26. Starts with 'Coding'
print(company.startswith('Coding'))

# 27. Ends with 'coding'
print(company.endswith('coding'))

# 28. Remove spaces
text_with_spaces = '   Coding For All      '
print(text_with_spaces.strip())

# 29. Check valid identifiers
print('30DaysOfPython'.isidentifier())  # False
print('thirty_days_of_python'.isidentifier())  # True

# 30. Join list with '# '
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libs))

# 31. New line
print("I am enjoying this challenge.\nI just wonder what is next.")

# 32. Tabs
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 33. String formatting: area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# 34. Operations with string formatting
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

