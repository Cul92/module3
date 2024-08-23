def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
# print_params(a, b) для вывода отдельных параметров функции необходимо указать print (a,b)- параметры, необходимые для печати
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [2.3, 'слово', 9]
values_dict = {'a': [1, 2, 3], 'b': 7, 'c': 'красотка'}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [8, 'шмекси']
print_params(*values_list_2, 42)
