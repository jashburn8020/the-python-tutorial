#!/usr/bin/pytest-3
"""
Data Structures
https://docs.python.org/3/tutorial/datastructures.html
"""
from collections import deque
import math
import pytest

# More on Lists


def test_list_sort():
    """
    Sorting a list using a key function
    The value of the key parameter should be a function that takes a single argument and returns a
    key to use for sorting purposes. This technique is fast because the key function is called
    exactly once for each input record
    """
    students = [("john", "A", 15), ("jane", "B", 12), ("dave", "B", 10)]

    student_names = students.copy()
    student_names.sort()
    assert student_names[0][0] == "dave"

    student_ages = students.copy()
    student_ages.sort(key=lambda student: student[2])
    assert student_ages[0][2] == 10


def test_list_stack():
    """Using lists as stacks (LIFO) - append and pop"""
    stack = []
    stack.append(1)
    stack.append(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_list_queue_slow():
    """
    Using lists as queues (FIFO) - insert, pop
    Doing inserts or pops from the beginning of a list is slow because all of the other elements
    have to be shifted by one
    """
    slow_queue = []
    slow_queue.append(1)
    slow_queue.append(2)
    assert slow_queue.pop(0) == 1
    assert slow_queue.pop(0) == 2

    slow_queue.insert(0, 1)
    slow_queue.insert(0, 2)
    assert slow_queue.pop() == 1
    assert slow_queue.pop() == 2


def test_list_queue_fast():
    """Faster queue using a deque"""
    fast_queue = deque([])
    fast_queue.append(1)
    fast_queue.append(2)
    assert fast_queue.popleft() == 1
    assert fast_queue.popleft() == 2


# List Comprehensions

def test_listcomp():
    """
    List comprehension
    List comprehensions provide a concise way to create lists. Common applications are to make new
    lists where each element is the result of some operations applied to each member of another
    sequence or iterable, or to create a subsequence of those elements that satisfy a certain
    condition.
    """
    # 'Normal' for loop
    squares = []
    for num in range(5):
        squares.append(num ** 2)
    assert squares == [0, 1, 4, 9, 16]
    # Side-effect: num exists after the loop completes
    assert num == 4

    # List comprehension - no side-effects
    squares_listcomp = [num**2 for num in range(5)]
    assert squares_listcomp == squares


def test_listcomp_for_if():
    """
    A list comprehension consists of brackets containing an expression followed by a for clause,
    then zero or more for or if clauses. The result will be a new list resulting from evaluating
    the expression in the context of the for and if clauses which follow it.
    """
    # 'Normal' for loops
    combinations = []
    for first_loop_elem in [1, 2, 3]:
        for second_loop_elem in [3, 1, 4]:
            if first_loop_elem != second_loop_elem:
                combinations.append((first_loop_elem, second_loop_elem))
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # List comprehension
    combinations_listcomp = [(first_elem, second_elem) for first_elem in [1, 2, 3]
                             for second_elem in [3, 1, 4] if first_elem != second_elem]
    assert combinations_listcomp == combinations


def test_listcomp_applications():
    """Ways to use list comprehension"""
    vec = [-4, -2, 0, 2, 4]

    # Filter the list to exclude negative numbers
    assert [elem for elem in vec if elem >= 0] == [0, 2, 4]

    # Apply a function to all elements
    assert [abs(elem) for elem in vec] == [4, 2, 0, 2, 4]

    # Nested functions
    assert [str(round(math.pi, precision)) for precision in range(1, 4)] == ["3.1", "3.14", "3.142"]

    # Call a method on each element
    fruits = ["apple", "banana", "cherry"]
    assert [elem.upper() for elem in fruits] == ["APPLE", "BANANA", "CHERRY"]

    # Flatten a list
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert [num for elem in nested_list for num in elem] == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_nested_listcomp():
    """
    The initial expression in a list comprehension can be any arbitrary expression, including
    another list comprehension.
    """
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    transposed_matrix = [[row[elem] for row in matrix] for elem in range(4)]
    assert transposed_matrix == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


def test_del_list():
    """Remove element(s) from a list"""
    nums = [1, 2, 3, 4, 5]
    del nums[0]
    assert nums == [2, 3, 4, 5]

    del nums[1:3]
    assert nums == [2, 5]

    del nums[:]
    assert nums == []

    # Delete entire variable
    del nums

# Tuples and Sequences


def test_tuple_packing_sequence_unpacking():
    """
    Tuple packing - values are packed together in a tuple.
    Sequence unpacking - the reverse; request as many variables as there are elements in the
    sequence.
    """
    packed_tuple = 1, 2, "a"
    one, two, three = packed_tuple
    assert one == 1 and two == 2 and three == "a"


def test_tuple_features():
    """More about tuples"""
    first_tuple = 1, 2, 3
    nested_tuple = first_tuple, 4, (5, 6)
    assert nested_tuple[0] == (1, 2, 3)
    assert nested_tuple[2][0] == 5

    # Tuples are immutable
    with pytest.raises(TypeError):
        # pylint: disable=unsupported-assignment-operation
        first_tuple[0] = 0

    empty_tuple = ()
    # PEP 8: For sequences, (strings, lists, tuples), use the fact that empty sequences are false
    assert not empty_tuple

    single_elem_tuple = (1,)
    assert len(single_elem_tuple) == 1

# Sets


def test_set_features():
    """A set is an unordered collection with no duplicate elements"""
    empty_set = set()
    assert not empty_set

    set_one = {"a", "b", "c"}
    set_two = set("cde")

    assert "a" in set_one
    assert "e" in set_two
    assert set_one - set_two == {"a", "b"}
    assert set_one | set_two == set("abcde")
    assert set_one & set_two == {"c"}
    assert set_one ^ set_two == set("abde")

    # Set comprehension
    assert {elem for elem in set_one if elem not in set_two} == {"a", "b"}


# Dictionaries


def test_dictionary_features():
    """
    Dictionaries are indexed by keys, which can be any immutable type - strings, numbers. Tuples
    can be used as keys if they contain only strings, numbers, or tuples.
    """
    fruits = {"apple": 3, "banana": 5, "cherry": 4}
    assert fruits["banana"] == 5

    del fruits["cherry"]
    fruits["durian"] = 2

    # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in
    # insertion order (if you want it sorted, just use sorted(d) instead).
    assert list(fruits) == ["apple", "banana", "durian"]
    assert sorted(fruits, reverse=True) == ["durian", "banana", "apple"]

    assert "apple" in fruits
    assert "elderberry" not in fruits


def test_dictionary_constructor_comprehension():
    """Dictionaries can be created using the dict() constructor and dict comprehension"""
    fruits = dict([("banana", 5), ("cherry", 4), ("durian", 2)])
    also_fruits = dict((("banana", 5), ("cherry", 4), ("durian", 2)))
    assert fruits == also_fruits

    more_fruits = dict(banana=5, cherry=4, durian=2)
    assert fruits == more_fruits

    even_power_twos = {even: even**2 for even in range(10) if even % 2 == 0}
    assert even_power_twos == {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


def test_looping_data_structures():
    """Looping techniques"""
    # items() method to retrieve a dict's key and value at the same time
    flat_list = []
    for key, value in {"gallahad": "the pure", "robin": "the brave"}.items():
        flat_list.append(key)
        flat_list.append(value)
    assert flat_list == ["gallahad", "the pure", "robin", "the brave"]

    # enumerate() function to retrieve a sequence's position index and value at the same time
    flat_list.clear()
    for index, value in enumerate(["tic", "tac", "toe"]):
        flat_list.append(index)
        flat_list.append(value)
    assert flat_list == [0, "tic", 1, "tac", 2, "toe"]

    # zip() function to pair entries from two or more sequences
    flat_list.clear()
    questions = ["name", "quest"]
    answers = ["lancelot", "the holy grail"]
    for question, answer in zip(questions, answers):
        flat_list.append((question, answer))
    assert flat_list == [("name", "lancelot"), ("quest", "the holy grail")]

    # Changing a list: it is often simpler and safer to create a new list
    raw_data = [56.2, float('NaN'), 51.7, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    assert filtered_data == [56.2, 51.7, 47.8]

    filtered_data_listcomp = [data for data in raw_data if not math.isnan(data)]
    assert filtered_data == filtered_data_listcomp
