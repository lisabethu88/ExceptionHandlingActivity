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
  
    # AttributeError
    # TypeError
    # NameError
    # ValueError
    # UnboundLocalError
    # OverflowError
