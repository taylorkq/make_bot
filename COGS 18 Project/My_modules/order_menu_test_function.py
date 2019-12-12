""" Test for order_menu. Used to test the majority of functions in the
program.
"""
from order_menu import *
first_menu = Menu("menu.json")

def test_print_categories():
    assert callable(first_menu.print_categories)
    assert isinstance(first_menu.print_categories(), bool)
    
def test_order_food():
    assert callable(first_menu.order_food)
    assert isinstance(first_menu.order_food("Juicy Steamed Chicken in Chili Sauce"), bool)