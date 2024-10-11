"""
primitive data types
consist of: numbers, boolean, string
"""

# immutable
print("\nPrimitive Data Types are Immutable")
x = 1
print(id(x), " ", type(x))
x = "oke"
print(id(x), " ", type(x))

# numbers
print("\nPrimitive: Numbers")
x = 6
print(x, " ", type(x))
x = 6.0
print(x, " ", type(x))
x = 1+2j
print(x, " ", type(x))

# boolean
print("\nPrimitive: Boolean")
x = True
print(x, " ", type(x))
x = False
print(x, " ", type(x))

# string
print("\nPrimitive: String")
x = 'Dicoding'
print(x, " ", type(x))

"""
collection data types
consist of: list, tuple, set, dictionary
"""

# list
print("\nCollection: List")
x = [1, 'Dicoding', True, 1.0]
print(x)
print(type(x))

# tuple
print("\nCollection: Tuple")
x = (1, "Dicoding", 1+3j)
print(x)
print(type(x))

# set
print("\nCollection: Set")
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

# dictionary
print("\nCollection: Dictionary")
x = { 'name': 'Fatima Zza', 'age': 17, 'isMarried': False }
print(x)
print(type(x))
