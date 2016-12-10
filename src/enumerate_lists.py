cities = ['Dublin', 'Amsterdam', 'Helsinki', 'London']

# Bad way to to walk trough the list print them and their location on the list
i = 0
for city in cities:
    print(i, city)
    i += 1

# Good way is to use enumerate function.
# Enumerate documentation at: https://docs.python.org/3/library/functions.html#enumerate
for i, city in enumerate(cities):
    print(i, city)
