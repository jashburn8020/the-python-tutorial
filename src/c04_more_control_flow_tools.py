#!/usr/bin/pytest-3
"""
More Control Flow Tools
https://docs.python.org/3/tutorial/controlflow.html
"""
import pytest


def positive_negative(number):
    """if-elif-else"""
    if number < 0:
        return -1
    elif number == 0:
        return 0
    else:
        return 1


def test_if():
    """if-elif-else"""
    assert positive_negative(100) == 1
    assert positive_negative(0) == 0
    assert positive_negative(-99) == -1

# for Statements
# Python’s for statement iterates over the items of any sequence (a list or a string)


def test_for_string():
    """for - iterate over a string"""
    alpha = "ababa"
    num_of_as = 0
    for letter in alpha:
        if letter == "a":
            num_of_as += 1

    assert num_of_as == 3


def test_for_list():
    """for - iterate over a list"""
    words = ['cat', 'window', 'defenestrate']
    char_count = []
    for word in words:
        char_count.append(len(word))

    assert char_count == [3, 6, 12]


def test_for_modify():
    """
    Modifying a list in a for loop
    If you need to modify the sequence you are iterating over while inside the loop (for example to
    duplicate selected items), it is recommended that you first make a copy.
    """
    words = ['cat', 'window', 'defenestrate']
    for word in words[:]:
        if len(word) > 5:
            words.insert(0, word)

    assert words == ['defenestrate', 'window', 'cat', 'window', 'defenestrate']


def test_range():
    """range() function"""
    numbers = []
    for i in range(5):
        numbers.append(i)

    assert numbers == [0, 1, 2, 3, 4]

    numbers = []
    for i in range(5, 10):
        numbers.append(i)

    assert numbers == [5, 6, 7, 8, 9]

    numbers = []
    for i in range(0, 10, 3):
        numbers.append(i)

    assert numbers == [0, 3, 6, 9]


def test_range_iterable():
    """range() returns an iterable. The for statement is an iterator, and so is list()"""
    numbers = list(range(10))
    assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# break and continue Statements, and else Clauses on Loops

def extract_primes(max_num):
    """break and else statements in a for loop"""
    primes = []
    for poss_prime in range(2, max_num):
        for poss_factor in range(2, poss_prime):
            if poss_prime % poss_factor == 0:
                break
        else:
            # loop fell through without finding a factor (without breaking)
            primes.append(poss_prime)
    return primes


def test_for_break_else():
    """Testing break and else statements in a for loop"""
    assert extract_primes(2) == []
    assert extract_primes(10) == [2, 3, 5, 7]


class MyEmptyClass:
    """The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action"""
    pass

# Defining Functions


def fibonacci(maxval):
    """Return a list containing the Fibonacci series up to maxval."""
    result = []
    current, nextval = 0, 1
    while current < maxval:
        result.append(current)
        current, nextval = nextval, current + nextval
    return result


def test_function():
    """Test for fibonacci; renaming a function locally"""
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
    fib = fibonacci
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8]


def default_args(value, multiplier=2):
    """Default arguments - if multiplier is not provided, the default value will be used.
    Throws ValueError is the value is same as the multiplier"""
    if value == multiplier:
        raise ValueError(f"Value {value} is the same as multiplier {multiplier}")

    return value * multiplier


def test_default_args():
    """Test default arguments"""
    assert default_args(5) == 10
    assert default_args(5, 3) == 15

    with pytest.raises(ValueError) as ex_info:
        default_args(5, 5)
    assert "Value 5 is the same as multiplier 5" in str(ex_info.value)


def mutable_default_value(value, container=[]):
    """container default value is a mutable object. Avoid!"""
    container.append(value)
    return container


def test_default_value_accumulation():
    """Default value is evaluated only once. With a mutable object, it accumulates arguments
    passed to it on subsequent calls"""
    assert mutable_default_value(1) == [1]
    assert mutable_default_value(2) == [1, 2]


def keyword_arguments(first, second=2, third=3):
    """Accepts 1 required argument (first) and 2 optional arguments (second, third)"""
    return [first, second, third]


def test_keyword_arguments():
    """Keyword arguments are arguments of the form kwarg=value"""
    # 1 positional argument
    assert keyword_arguments(10) == [10, 2, 3]
    # 1 keyword argument
    assert keyword_arguments(first=10) == [10, 2, 3]
    # 2 keyword arguments, order unimportant
    assert keyword_arguments(second=20, first=10) == [10, 20, 3]
    # 1 positional argument, 1 keyword argument
    assert keyword_arguments(10, third=30) == [10, 2, 30]
    # Positional argument cannot follow a keyword argument
    # keyword_arguments(second=20, 10)


def arbitrary_keyword_arguments(first, **seconds):
    """
    When a final parameter is of the form **name, it receives a dictionary containing all keyword
    arguments except those corresponding to a formal parameter
    """
    return seconds


def test_arbitrary_keyword_arguments():
    """kwargs"""
    args_dict = arbitrary_keyword_arguments(1, second=2, third=3)
    assert len(args_dict) == 2
    assert args_dict["second"] == 2
    assert args_dict["third"] == 3


def arbitary_argument_list(*args, sep=" "):
    """
    args accepts an arbitrary number of arguments. It is normally last in the list of formal
    parameters because it scoops up all remaining input arguments, wrapped up in a tuple. Formal
    parameters that occur after *args are keyword arguments only.
    """
    return sep.join(args)


def test_arbitrary_argument_list():
    """Arbitrary argument list"""
    assert arbitary_argument_list("1", "2", "3", sep=",") == "1,2,3"


def test_unpacking_arguments():
    """
    When the arguments are already in a list or tuple, they need to be unpacked for a function
    call requiring separate positional arguments
    """
    args = (10, 20, 30)
    # Without unpacking, the entire tuple is a single argument
    assert keyword_arguments(args) == [(10, 20, 30), 2, 3]
    # Unpack
    assert keyword_arguments(*args) == [10, 20, 30]

    # Similarly, dictionaries can deliver keyword arguments with the ** operator
    args_dict = {"second": 20, "third": 30}
    assert keyword_arguments(10, **args_dict) == [10, 20, 30]


def power(base):
    """Lambda expression"""
    return lambda exponent: base ** exponent


def test_lambda_expression():
    """
    Small anonymous functions can be created with the lambda keyword. Lambda functions can be used
    wherever function objects are required. They are syntactically restricted to a single
    expression. Like nested function definitions, lambda functions can reference variables from the
    containing scope.
    """
    two_raised_to_the_power_of = power(2)

    assert two_raised_to_the_power_of(3) == 8


def function_annotations(ham: str, eggs: str = "eggs") -> str:
    """Function annotations"""
    return ham + " and " + eggs


def test_function_annotations():
    """
    An annotation of a function parameter or return value. Usually used for type hints.
    Type hints are optional and are not enforced by Python but they are useful to static type
    analysis tools, and aid IDEs with code completion and refactoring.
    """
    assert function_annotations("sausage") == "sausage and eggs"
