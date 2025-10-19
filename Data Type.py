# 1. Numeric Data Types
print("----- Numeric Data Types -----")

# Integer
x_int = 100
print("Integer:", x_int, type(x_int))

# Float
x_float = 20.5
print("Float:", x_float, type(x_float))

# Complex
x_complex = 2 + 3j
print("Complex:", x_complex, type(x_complex))

print()

# 2. Sequence Data Types
print("----- Sequence Data Types -----")

# String
x_str = "Python"
print("String:", x_str, type(x_str))
print("First character:", x_str[0])
print("Last character:", x_str[-1])

# List
x_list = ["apple", "banana", "cherry"]
x_list.append("orange")
print("List:", x_list, type(x_list))

# Tuple
x_tuple = ("car", "bike", "bus")
print("Tuple:", x_tuple, type(x_tuple))

# Range
x_range = range(5)
print("Range:", list(x_range), type(x_range))

print()

# 3. Boolean Data Type
print("----- Boolean Data Type -----")

x_bool = True
y_bool = False
print("Boolean x:", x_bool, type(x_bool))
print("Boolean y:", y_bool, type(y_bool))
print("5 > 3:", 5 > 3)

print()

# 4. Set Data Types
print("----- Set Data Types -----")

# Set
x_set = {1, 2, 3, 4, 5}
y_set = {4, 5, 6, 7}
print("Set x:", x_set, type(x_set))
print("Set y:", y_set)

# Set operations
print("Union:", x_set | y_set)
print("Intersection:", x_set & y_set)
print("Difference (x - y):", x_set - y_set)
print("Symmetric Difference:", x_set ^ y_set)

# Frozenset
x_frozenset = frozenset([1, 2, 3])
print("Frozenset:", x_frozenset, type(x_frozenset))

print()

# 5. Dictionary Data Type
print("----- Dictionary Data Type -----")

x_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", x_dict, type(x_dict))
print("Access by key (name):", x_dict["name"])
print("Using get() method:", x_dict.get("age"))

print()

# 6. NoneType
print("----- NoneType -----")

x_none = None
print("NoneType variable:", x_none, type(x_none))
