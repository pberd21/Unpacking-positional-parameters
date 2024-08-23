def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=34)
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [21, 'Привет', True]
print_params(*value_list)

value_dict = {'a': 3, 'b': "Словарик", 'c': [6, 3, 9]}
print_params(**value_dict)

value_list2 = [54.32, 'Cтрока']
print_params(*value_list2, 42)
