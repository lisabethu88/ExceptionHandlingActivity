import pytest

from activity.main import *

def test_exception():
    num = 5
    with pytest.raises(ZeroDivisionError):
        div_zero(num)

 # KeyError
def test_get_value_key_error():
    key = 4
    with pytest.raises(KeyError):
        get_value(key)

  # IndexError
def test_get_element_index_error():
    index = 10
    with pytest.raises(IndexError):
        get_element(index)
  
    # TypeError
def test_calculate_sum_type_error():
    b="Hello World!"
    with pytest.raises(TypeError):
        calculate_sum(b)

    # AttributeError
def test_append_to_num_attribute_error():
    num = 5
    with pytest.raises(AttributeError):
        append_to_num(num)

    # NameError
def test_add_names_name_error():
    first_name = "Lisa"
    with pytest.raises(NameError):
        add_names(first_name)

    # ValueError
def test_convert_to_int_value_error():
    num = "whoops"
    with pytest.raises(ValueError):
        convert_to_int(num)

    # UnboundLocalError
def test_print_full_name_unbound_local_error():
    last_name = "Utsett"
    with pytest.raises(UnboundLocalError):
        print_full_name(last_name)

    # OverflowError
def test_multiply_num_overflow_error():
    big_num = 7.0
    with pytest.raises(OverflowError):
        multiply_num(big_num)
