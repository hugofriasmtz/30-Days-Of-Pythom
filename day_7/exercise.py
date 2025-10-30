# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once into it_companies
it_companies.update(['Tesla', 'Intel', 'HP'])
print(it_companies)

# 4. Remove one company from it_companies
it_companies.remove('IBM')
print(it_companies)

# 5. What is the difference between remove and discard?
# remove() raises an error if the item is not found.
# discard() does not raise an error if the item is not found.


# 1. Join A and B
C = A.union(B)
print(C)

# 2. Find intersection of A and B
print(A.intersection(B))

# 3. Is A subset of B
print(A.issubset(B))

# 4. Are A and B disjoint sets
print(A.isdisjoint(B))

# 5. Join A with B and B with A
print(A.union(B))
print(B.union(A))

# 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B



# 1. Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print("List length:", len(age))
print("Set length:", len(age_set))
# The list is longer because it contains duplicate values.


# “I am a teacher and I love to inspire and teach people.”
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
