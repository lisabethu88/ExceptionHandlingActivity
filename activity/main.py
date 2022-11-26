def div_zero(num):
    x = num / 0

    # KeyError
def get_value(key):
    my_dict = {1:"Hello", 2:"World!"}
    result = my_dict[key]

# IndexError
def get_element(index):
    my_list = [2,4,6,7]
    element = my_list[index]

# TypeError
def calculate_sum(b):
    a=10
    sum = a+b

    # AttributeError
def append_to_num(num):
    num.append(7)

    # NameError
def add_names(first_name):
    full_name = first_name + last_name
    
    # ValueError
def convert_to_int(old_num):
    new_num = int(old_num)
    # UnboundLocalError
def print_full_name(last_name):
    print(first_name + '' + last_name)
    first_name = "Lisa"

    # OverflowError
def multiply_num(big_num):
    for i in range(1, 100):
        big_num = big_num ** i


