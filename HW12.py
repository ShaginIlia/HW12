# Задание 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('шляпа', False)
print_params(b='кино', c='34')
print_params(c=False, a={'1': 'up', '2': 'down'})
print_params('число')
print_params(b=25)
print_params(c=[1, 2, 3])
print()
# Задание 2. Распаковка параметров
print()
values_list = [2, ['apple', 'orange', 'cherry'], True]
values_dict = {'a': 'Sony', 'b': 'Samsung', 'c': 'Apple'}
print_params(*values_list)
print_params(**values_dict)
print()
# Задание 3. Распаковка + отдельные параметры
print()
values_list_2 = ['QQ', 11]
print_params(*values_list_2, 42)

