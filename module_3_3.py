def print_params(a=1, b="строка", c=True):

        print(a, b, c)


print_params(a=1, b=25, c=[1, 2, 3])
print_params()
print_params()
values_list = [25, "string", [12]]
print_params = values_list
print(print_params)
values_dict = {"a":1, "строка": 0, True: 0}
print_params = values_dict
print(print_params)
values_list = [25, *"string", [12]]
print_params = values_list
print(print_params)
values_list_2 = [54.32, "Строка",]
print_params = values_list_2
print(print_params, 42)