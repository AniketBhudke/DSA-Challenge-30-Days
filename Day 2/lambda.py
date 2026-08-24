add = lambda a, b: a + b
square = lambda x: x ** 2
check_even = lambda n: "Even" if n % 2 == 0 else "Odd"
max_val = lambda x, y: x if x > y else y

print(add(3, 5))
print(square(4))
print(check_even(7))
print(max_val(10, 20))

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, numbers)))