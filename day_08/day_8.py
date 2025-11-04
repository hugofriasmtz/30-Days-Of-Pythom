# Creating a Directory
person = {
    'first_name':'Hugo',
    'last_name':'Frias',
    'age':22,
    'country':'México',
    'is_married':False,
    'skills':['PHP', 'BASH', 'Node', 'MariaDB', 'Python'],
    'address':{
        'street':'15 de Mayo',
        'zipcode':'101010'
    }
}
print(person)

# Dictionary Length
print(len(person))

# Accessing Dictionary Items
print(person['first_name'])         # Hugo
print(person['last_name'])          # Frias
print(person['age'])                # 22
print(person['country'])            # México
print(person['is_married'])        # False
print(person['skills'])             # ['PHP', 'BASH', 'Node', 'MariaDB', 'Python']
print(person['address'])            # {'street': '15 de Mayo', 'zipcode': '101010'}
print(person['address']['street'])  # 15 de Mayo
print(person['address']['zipcode']) # 101010
print(person.get('city'))           # The get method returns None, which is a NoneType object data type, if the key does not exist.

# Adding Items to a Dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

# Modifying Items in a Dictionary
person['first_name'] = 'Jesús'
person['age'] = 23
print(person)

# Checking Keys in a Dictionary
print('last_name' in person)    # True
print('hobby' in person)        # False

# Removing Key and Value Pairs from a Dictionary
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the job_title
del person['is_married']        # Removes the is_married item
print(person)

# Copy a Dictionary
person_copy = person.copy()

# Getting Dictionary Keys as a List
person_keys = person.keys()
print(person_keys)

# Getting Dictionary Values as a List
person_values = person.values()
print(person_values)