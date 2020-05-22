"""More Control Flow Tools.

https://docs.python.org/3/tutorial/controlflow.html"""
import pytest


class TestIf:
    """Demonstrate `if`."""

    @staticmethod
    def test_if():
        """if-elif-else."""

        def positive_negative(number):
            """Returns -1 for negative numbers, 1 for positive numbers, and 0 for 0."""
            if number < 0:
                result = -1
            elif number == 0:
                result = 0
            else:
                result = 1
            return result

        assert positive_negative(100) == 1
        assert positive_negative(0) == 0
        assert positive_negative(-99) == -1


class TestFor:
    """Demonstrate `for`."""

    @staticmethod
    def test_for_string():
        """Iterate over a string."""
        alpha = "ababa"
        num_of_as = 0

        for letter in alpha:
            if letter == "a":
                num_of_as += 1

        assert num_of_as == 3

    @staticmethod
    def test_for_list():
        """Iterate over a list."""
        words = ["cat", "window", "defenestrate"]
        char_count = []
        for word in words:
            char_count.append(len(word))

        assert char_count == [3, 6, 12]

    @staticmethod
    def test_for_modify():
        """Modifying a list in a for loop.

        If you need to modify the sequence you are iterating over while inside the loop
        (for example to duplicate selected items), it is recommended that you first
        make a copy."""
        words = ["cat", "window", "defenestrate"]
        for word in words[:]:  # copy of words
            if len(word) > 5:
                words.insert(0, word)

        assert words == ["defenestrate", "window", "cat", "window", "defenestrate"]

    @staticmethod
    def test_for_modify_no_copy():
        """Modifying a list in a `for` loop without first making a copy of the list -
        not a good idea."""
        words = ["cat", "window", "defenestrate"]
        for word in words:
            if len(word) > 5 and len(words) < 7:
                words.insert(0, word)

        assert words == [
            "window",
            "window",
            "window",
            "window",
            "cat",
            "window",
            "defenestrate",
        ]


class TestRange:
    """Demonstrate `range()`."""

    @staticmethod
    def test_range():
        """`range()` function."""
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

    @staticmethod
    def test_range_iterate_over_indices():
        """Iterate over the indices of a sequence."""
        rhyme = ["Mary", "had", "a", "little", "lamb"]
        odd_rhyme = []
        for i in range(1, len(rhyme), 2):
            odd_rhyme.append((i, rhyme[i]))

        assert odd_rhyme == [(1, "had"), (3, "little")]

    @staticmethod
    def test_range_iterable():
        """range() returns an iterable. The `for` statement is an iterator, and so is
        `list()`."""
        numbers = list(range(10))
        assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestBreakElse:
    """Demonstrate the `break` and `else` statements on loops."""

    @staticmethod
    def test_for_break_else():
        """Testing `break` and `else` statements in a `for` loop."""

        def extract_primes(max_num):
            """Extract prime numbers for numbers from 2 to `max_num`"""
            primes = []
            for poss_prime in range(2, max_num + 1):
                for poss_factor in range(2, poss_prime):
                    if poss_prime % poss_factor == 0:
                        break
                else:
                    # loop fell through without finding a factor (without breaking)
                    primes.append(poss_prime)
            return primes

        assert extract_primes(2) == [2]
        assert extract_primes(10) == [2, 3, 5, 7]


class MyEmptyClass:
    """The `pass` statement does nothing."""

    pass


GLOBAL_VAR = 1


def test_var_assign():
    """Test assigning value to global variables and variables of enclosing functions."""
    enclosing_function_var = 2

    def reference_enclosing_var():
        """Variables in the enclosing function can be referenced."""
        assert enclosing_function_var == 2

    def assign_enclosing_var():
        """Variables in the enclosing function cannot be assigned."""
        # By assigning a value to enclosing_function_var below, enclosing_function_var
        # becomes a local variable. The assert statement thus causes calling this
        # function to fail with UnboundLocalError.
        assert enclosing_function_var == 200
        enclosing_function_var = 3

    def reference_global_var():
        """Global variables can be referenced."""
        assert GLOBAL_VAR == 1

    def assign_global_var():
        """Global variables cannot be assigned."""
        assert GLOBAL_VAR == 100
        GLOBAL_VAR = 3

    reference_enclosing_var()
    reference_global_var()

    with pytest.raises(UnboundLocalError):
        assign_enclosing_var()
    with pytest.raises(UnboundLocalError):
        assign_global_var()


class TestFunctions:
    """Demonstrate renaming functions and functions without a `return` statement."""

    @staticmethod
    def test_function_rename():
        """Renaming a function locally"""

        def fibonacci(maxval):
            """Return a list containing the Fibonacci series up to `maxval`."""
            result = []
            current, nextval = 0, 1
            while current < maxval:
                result.append(current)
                current, nextval = nextval, current + nextval
            return result

        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
        fib = fibonacci
        assert fib(10) == [0, 1, 1, 2, 3, 5, 8]

    @staticmethod
    def test_function_no_return():
        """Functions without a `return` statement do return a value - `None`."""

        def function_no_return():
            pass

        assert function_no_return() is None


class TestFunctionArguments:
    """Demonstrate default arguments and keyword arguments."""

    @staticmethod
    def test_default_args():
        """Default arguments"""

        def default_args(value, multiplier=2):
            """If `multiplier` is not provided, the default value will be used.
            Throws `ValueError` if `value` is same as `multiplier`."""
            if value == multiplier:
                raise ValueError(
                    f"Value {value} is the same as multiplier {multiplier}"
                )

            return value * multiplier

        assert default_args(5) == 10
        assert default_args("a", 3) == "aaa"

        with pytest.raises(ValueError) as ex_info:
            default_args(5, 5)
        assert "Value 5 is the same as multiplier 5" in str(ex_info.value)

    @staticmethod
    def test_default_value_accumulation():
        """Default value is evaluated only once. With a mutable object, it accumulates
        arguments passed to it on subsequent calls."""

        def mutable_default_value_shared(value, container=[]):
            """`container` default value is a mutable object. Avoid!"""
            container.append(value)
            return container

        def mutable_default_value_not_shared(value, container=None):
            """Avoids the default mutable object problem."""
            if container is None:
                container = []
            container.append(value)
            return container

        assert mutable_default_value_shared(1) == [1]
        assert mutable_default_value_shared(2) == [1, 2]

        assert mutable_default_value_not_shared(1) == [1]
        assert mutable_default_value_not_shared(2) == [2]

    @staticmethod
    def test_keyword_arguments():
        """Keyword arguments are arguments of the form `kwarg=value`."""

        def keyword_arguments(first, second=2, third=3):
            """Accepts 1 required argument (`first`) and 2 optional arguments (`second`,
            `third`)."""
            return (first, second, third)

        # 1 positional argument
        assert keyword_arguments(10) == (10, 2, 3)
        # 1 keyword argument
        assert keyword_arguments(first=10) == (10, 2, 3)
        # 2 keyword arguments, order unimportant
        assert keyword_arguments(second=20, first=10) == (10, 20, 3)
        # 1 positional argument, 1 keyword argument
        assert keyword_arguments(10, third=30) == (10, 2, 30)
        # Positional argument cannot follow a keyword argument
        # keyword_arguments(second=20, 10)


class TestArbitraryArguments:
    """Demonstrate arbitrary argument lists."""

    @staticmethod
    def test_arbitrary_keyword_arguments():
        """Arbitrary number of keyword arguments, parameter of the form `**name`."""

        def arbitrary_keyword_arguments(first, **seconds):
            """When a final parameter is of the form `**name`, it receives a dictionary
            containing all keyword arguments except those corresponding to a formal
            parameter."""
            return (first, seconds.copy())

        first_arg, args_dict = arbitrary_keyword_arguments(1, second=2, third=3)
        assert first_arg == 1

        assert isinstance(args_dict, dict)
        assert len(args_dict) == 2
        assert args_dict["second"] == 2
        assert args_dict["third"] == 3

    @staticmethod
    def test_arbitrary_argument_list():
        """Arbitrary argument list, parameter of the form `*name`."""

        def arbitrary_argument_list(*args, sep=" "):
            """`args` accepts an arbitrary number of arguments.
            
            It is normally last in the list of formal parameters because it scoops up
            all remaining input arguments, wrapped up in a tuple. Formal parameters
            that occur after `*args` are keyword arguments only."""
            return sep.join(args)

        assert arbitrary_argument_list("1", "2", "3", sep=",") == "1,2,3"

    @staticmethod
    def test_combined_arbitrary_arguments(capsys):
        """Combining parameters of the form `*name` and `**name`."""

        def print_nvp(title, *separator_line_chars, **name_value_pair):
            """Print name-value pairs to stdout."""
            print(title)
            print("".join(separator_line_chars) * 3)
            for name in name_value_pair:
                print(name, ":", name_value_pair[name])

        print_nvp("Name-Value Pairs", "-", "=", one=1, two=2)
        out, err = capsys.readouterr()
        assert out == "Name-Value Pairs\n-=-=-=\none : 1\ntwo : 2\n"


class TestUnpackArgumentLists:
    """Demonstrate unpacking arguments."""

    @staticmethod
    def keyword_arguments(first, second=2, third=3):
        """Accepts 1 required argument (`first`) and 2 optional arguments (`second`,
        `third`)."""
        return (first, second, third)

    @staticmethod
    def test_unpacking_arguments():
        """When the arguments are already in a list or tuple, they need to be unpacked
        using the `*`-operator for a function call requiring separate positional
        arguments."""

        args = (10, 20, 30)
        # Without unpacking, the entire tuple is a single argument
        assert TestUnpackArgumentLists.keyword_arguments(args) == ((10, 20, 30), 2, 3,)
        # Unpack
        assert TestUnpackArgumentLists.keyword_arguments(*args) == (10, 20, 30)

    @staticmethod
    def test_unpack_dictionary():
        """Use the `**`-operator to unpack a dictionary."""

        args_dict = {"third": 30, "second": 20}
        assert TestUnpackArgumentLists.keyword_arguments(**args_dict, first=10) == (
            10,
            20,
            30,
        )


class TestLambda:
    """Demonstrate lambda expressions."""

    @staticmethod
    def test_lambda_function_object():
        """Lambda returned by a function."""

        def power(base):
            """Lambda expression to calculate power."""
            return lambda exponent: base ** exponent

        two_raised_to_the_power_of = power(2)
        assert two_raised_to_the_power_of(3) == 8

    @staticmethod
    def test_lambda_inline():
        """Lambda, inlined."""
        doubler = lambda value: value * 2
        assert doubler(5) == 10
        assert doubler("a") == "aa"
