#identity operator 
#is operator  compare according to the address of the object 
# 1. INTEGER
a = 5
b = 5
print("int:", a == b, a is b)


# 2. FLOAT
a = 5.5
b = 5.5
print("float:", a == b, a is b)


# 3. COMPLEX
a = 2 + 3j
b = 2 + 3j
print("complex:", a == b, a is b)


# 4. BOOLEAN
a = True
b = True
print("bool:", a == b, a is b)


# 5. STRING
a = "hello"
b = "hello"
print("string:", a == b, a is b)


# 6. LIST
a = [1, 2, 3]
b = [1, 2, 3]
print("list:", a == b, a is b)


# 7. TUPLE
a = (1, 2, 3)
b = (1, 2, 3)
print("tuple:", a == b, a is b)


# 8. SET
a = {1, 2, 3}
b = {1, 2, 3}
print("set:", a == b, a is b)


# 9. DICTIONARY
a = {"name": "Aniket"}
b = {"name": "Aniket"}
print("dict:", a == b, a is b)


# 10. NONE
a = None
b = None
print("None:", a == b, a is b)
