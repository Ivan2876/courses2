from dataclasses import dataclass

from homework1_utils import calculate_discount, is_even, get_full_name


def test_calculate_discount1():
    price = 100
    discount = 20
    expected = 80
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount2():
    price = 100
    discount = 50
    expected = 50
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount3():
    price = 100
    discount = 0
    expected = 100
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount4():
    price = 0
    discount = 20
    expected = 0
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount5():
    price = 200
    discount = 25
    expected = 150
    actual = calculate_discount(price, discount)
    assert expected == actual



def test_is_even1():
    number = 4
    expected = True
    actual = is_even(number)
    assert expected is actual

def test_is_even2():
    number = 7
    expected = False
    actual = is_even(number)
    assert expected is actual

def test_is_even3():
    number = -4
    expected = True
    actual = is_even(number)
    assert expected is actual

def test_is_even4():
    number = -7
    expected = False
    actual = is_even(number)
    assert expected is actual

def test_is_even5():
    number = 0
    expected =True
    actual = is_even(number)
    assert expected is actual


def test_get_full_name1():
    first_name = "John"
    last_name = "Smith"
    expected = "John Smith"
    actual = get_full_name(first_name, last_name)
    assert actual == expected, "what happened?"

def test_get_full_name2():
    first_name = "bob"
    last_name = "Doe"
    expected = "Bob Doe"
    actual = get_full_name(first_name, last_name)
    assert actual == expected, "what happened?"

def test_get_full_name3():
    first_name = "Christopher"
    last_name = "Maximilian"
    expected = "Christopher Maximilian"
    actual = get_full_name(first_name, last_name)
    assert actual == expected, "what happened?"

def test_get_full_name4():
    first_name = "J"
    last_name = "D"
    expected = "J D"
    actual = get_full_name(first_name, last_name)
    assert actual == expected, "what happened?"

def test_get_full_name5():
    first_name = "max"
    last_name = "doe"
    expected = "Max Doe"
    actual = get_full_name(first_name, last_name)
    assert actual == expected, "what happened?"