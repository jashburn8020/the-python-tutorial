# The Python Tutorial

Examples from [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

## 3. An Informal Introduction to Python

- See examples in [`c03_an_informal_introduction_to_python.py`](src/c03_an_informal_introduction_to_python.py)

### Numbers

- Integer numbers (e.g. 2, 4, 20) have type [`int`](https://docs.python.org/3/library/functions.html#int)
- The ones with a fractional part (e.g. 5.0, 1.6) have type [`float`](https://docs.python.org/3/library/functions.html#float)
- Division (`/`) always returns a `float`
- To do floor division and get an integer result (discarding any fractional result) you can use the `//` operator
  - to calculate the remainder you can use `%`
- Use the `**` operator to calculate powers
  - since `**` has higher precedence than `-`, `-3**2` will be interpreted as `-(3**2)` and thus result in `-9`.
  - to avoid this and get `9`, you can use `(-3)**2`
- Python supports other types of numbers, such as [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal) and [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction)
- Python also has built-in support for [complex numbers](https://docs.python.org/3/library/stdtypes.html#typesnumeric)
  - use the `j` or `J` suffix to indicate the imaginary part (e.g. `3+5j`)

### Strings

- Strings can be enclosed in single quotes (`'...'`) or double quotes (`"..."`)
  - `\` can be used to escape quotes
- If you don't want characters prefaced by `\` to be interpreted as special characters, you can use **raw strings** by adding an `r` before the first quote
  - see `test_raw_strings()`
- String literals can span **multiple lines**
  - one way is using triple-quotes: `"""..."""` or `'''...'''`
  - end of lines are automatically included in the string
    - possible to prevent this by adding a `\` at the end of the line
  - see `test_multiline()`
- Strings can be **concatenated** with the `+` operator, and **repeated** with `*`
  - repeated concatenation will have a quadratic runtime cost in the total sequence length
  - to get a linear runtime cost, you must switch to one of the alternatives below:
    - build a list and use [`str.join()`](https://docs.python.org/3/library/stdtypes.html#str.join) at the end
    - write to an [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO) instance and retrieve its value when complete
  - see `test_concat_repeat()`
- Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated
  - see `test_concat_string_literal()`
- Strings can be **indexed** (subscripted), with the first character having index 0
  - there is no separate character type; a character is simply a string of size one
  - indices may also be negative numbers, to start counting from the right
  - see `test_string_index()`
- **Slicing** is also supported
  - allows you to obtain substring
  - see `test_string_slice()`
- Python strings cannot be changed - they are **immutable**
  - assigning to an indexed position in the string results in an error
  - see `test_immutable_string()`
- The built-in function **`len()`** returns the length of a string
  - `test_string_len()`
- See also:
  - [Text Sequence Type - str](https://docs.python.org/3/library/stdtypes.html#textseq)
    - strings are examples of sequence types, and support the common operations supported by such types
    - see `test_text_sequence_type()`
  - [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
    - strings support a large number of methods for basic transformations and searching
    - see `test_string_methods()`
  - [Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    - string literals that have embedded expressions
    - see `test_formatted_string_literals()`
  - [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
    - information about string formatting with `str.format()`
    - see `test_format_string_syntax()`
  - [printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)
    - the old formatting operations invoked when strings are the left operand of the `%` operator are described in more detail here

### Lists

- A list can be written as a list of comma-separated values (items) between square brackets
- Lists might contain items of different types, but usually the items all have the same type
- Lists can be **indexed** and **sliced**
  - all slice operations return a new list containing the requested elements
  - slice returns a shallow copy of the list
  - see `test_list_index_slice()`
- Lists also support operations like **concatenation** (`+`)
  - see `test_list_concat()`
- Lists are a **mutable** type, i.e. it is possible to change their content
  - see `test_list_mutable()`
- You can also add new items at the end of the list, by using the **`append()`** method
  - see `test_list_append()`
- **Assignment to slices** is also possible, and this can even change the size of the list or clear it entirely
  - see `test_list_assign_to_slice()`
- The built-in function **`len()`** also applies to lists
  - see `test_list_len()`
- It is possible to **nest** lists
  - see `test_list_nest()`

## 4. More Control Flow Tools

- Based on <https://docs.python.org/3/tutorial/controlflow.html>

### `if` Statements

- See [`if_elif_else_test.py`](src/ch04/if_elif_else_test.py)
- An `if ... elif ... elif ...` sequence is a substitute for the `switch` or `case` statements found in other languages

```python
if number < 0:
    ...
elif number == 0:
    ...
else:
    ...
```

### `for` Statements

- See [`for_test.py`](src/ch04/for_test.py)
- Python's `for` statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence, rather than
  - always iterating over an arithmetic progression of numbers (like in Pascal), or
  - giving the user the ability to define both the iteration step and halting condition (as C)
  - `for letter in alpha:`
- Code that modifies a collection while iterating over that same collection should loop over a copy of the collection or to create a new collection
  - `for word in words[:]:`

### The `range()` Function

- See [`range_test.py`](src/ch04/range_test.py)
- If you do need to iterate over a sequence of numbers, the built-in function [`range()`](https://docs.python.org/3/library/stdtypes.html#range) comes in handy
- The object returned by `range()` is an **iterable**, implements the [collections.abc.**Sequence**](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence) ABC
- `for i in range(0, 12, 3):`

### `break` and `continue` Statements, and `else` Clauses on Loops

- See [`break_else_test.py`](src/ch04/break_else_test.py)
- The `break` statement breaks out of the innermost enclosing `for` or `while` loop
- The `continue` statement continues with the next iteration of the loop
- Loop statements may have an `else` clause
  - executed when
    - the loop terminates through exhaustion of the iterable (with `for`)
    - the condition becomes false (with `while`)
  - but not when the loop is terminated by a `break` statement

### `pass` Statements

- The `pass` statement does nothing
- It can be used when a statement is required syntactically but the program requires no action
- Another place is as a placeholder for a function or conditional body when you are working on new code

### Defining Functions

- The execution of a function introduces a new symbol table used for the local variables of the function
- All variable assignments in a function store the value in the _local symbol table_
- Variable references
  - first look in the local symbol table
  - then in the local symbol tables of enclosing functions
  - then in the global symbol table
  - finally in the table of built-in names
- Global variables and variables of enclosing functions
  - cannot be directly assigned a value within a function
  - unless, for global variables, named in a `global` statement, or, for variables of enclosing functions, named in a `nonlocal` statement
    - `nonlocal enclosing_var_assign`
    - `global GLOBAL_VAR_2`
  - although they may be referenced
  - see [`nonlocal_global_test.py`](src/ch04/nonlocal_global_test.py)
- The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called
  - arguments are passed using _call by value_ (where the value is always an _object reference_, not the value of the object)
- When a function calls another function, a new local symbol table is created for that call
- A function definition introduces the function name in the current symbol table
  - the value of the function name can be assigned to another name which can then also be used as a function
    - serves as a general renaming mechanism
  - `fib = fibonacci`
- Functions without a `return` statement do return a value - `None`
- See [`function_rename_no_return_test.py`](src/ch04/function_rename_no_return_test.py)

### More on Defining Functions

- It is possible to define functions with a variable number of arguments

#### Default Argument Values

- See [`function_arguments_test.py`](src/ch04/function_arguments_test.py)
- The most useful form is to specify a default value for one or more arguments
  - creates a function that can be called with fewer arguments than it is defined to allow
  - `def default_args(..., multiplier: int = 2) -> ...:`
- **Important warning**
  - the default value is evaluated only once
  - this makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes
    - can result in the default mutable object accumulating arguments passed to it on subsequent calls
  - `def mutable_default_value_shared(..., container: List[int] = []) -> ...:`

#### Keyword Arguments

- See [`function_arguments_test.py`](src/ch04/function_arguments_test.py)
- Functions can also be called using keyword arguments of the form `kwarg=value`
  - keyword parameters are also referred to as named parameters
- In a function call
  - keyword arguments must follow positional arguments
  - all the keyword arguments passed must match one of the arguments accepted by the function
  - keyword arguments' order is not important
  - no argument may receive a value more than once
  - `def keyword_arguments(first: int, second: int = 2, third: int = 3) -> ...:`
  - `keyword_arguments(10, third=30)`

#### Special parameters

- _Note: This works with Python 3.8+ only_
- See [`special_parameters_test.py`](src/ch04/special_parameters_test.py)
- By default, arguments may be passed to a Python function either by position or explicitly by keyword
- For readability and performance, it makes sense to restrict the way arguments can be passed
  - a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword
- A function definition may look like:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```

- where
  - `pos1` and `pos2`: positional only
  - `/`: optional
  - `pos_or_kwd`: positional or keyword
  - `*`: optional
  - `kwd1`, `kwd2`: keyword only

##### Positional-or-Keyword Arguments

- If `/` and `*` are not present in the function definition, arguments may be passed to a function by position or by keyword

##### Positional-Only Parameters

- It is possible to mark certain parameters as positional-only
- The parameters' order matters, and the parameters cannot be passed by keyword
- Positional-only parameters are placed before a `/`
  - used to logically separate the positional-only parameters from the rest of the parameters
- If there is no `/` in the function definition, there are no positional-only parameters
- `def pos_only_args(arg1: int, arg2: int, /) -> ...:`

##### Keyword-Only Arguments

- Placing an `*` in the arguments list just before the first keyword-only parameter
  - mark parameters as keyword-only
  - indicating the parameters must be passed by keyword argument
- `def kwd_only_args(*, arg1: int, arg2: int) -> ...:`
- `def combined_args(pos1: int, /, pos_or_kwd2: int, *, kwd3: int) -> ...:`

#### Arbitrary Argument Lists

- See [`arbitrary_arguments_test.py`](src/ch04/arbitrary_arguments_test.py)
- When a final formal parameter of the form `**name` is present
  - it receives a **dictionary** containing all keyword arguments except for those corresponding to a formal parameter
  - `def arbitrary_keyword_arguments(first: int, **seconds: int) -> ...:`
- May be combined with a formal parameter of the form `*name`
  - receives a **tuple** containing the positional arguments beyond the formal parameter list
  - `*name` must occur before `**name`
  - `def print_nvp(title: str, *separator_line_chars: str, **name_value_pair: int) -> ...:`
- Before the variable number of arguments, zero or more normal arguments may occur
- Any formal parameters which occur after the `*name` parameter are 'keyword-only' arguments
  - `def arbitrary_argument_list(*args: str, sep: str = " ") -> ...:`

#### Unpacking Argument Lists

- See [`unpack_arguments_test.py`](src/ch04/unpack_arguments_test.py)
- The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments
  - write the function call with the `*`-operator to unpack the arguments out of a list or tuple
  - `keyword_arguments(*args)`
- In the same fashion, dictionaries can deliver keyword arguments with the `**`-operator
  - `keyword_arguments(first=10, **args_dict)`

#### Lambda Expressions

- See [`lambda_test.py`](src/ch04/lambda_test.py)
- Small anonymous functions can be created with the [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda) keyword
- Lambda functions can be used wherever function objects are required
- They are syntactically restricted to a single expression
- Like nested function definitions, lambda functions can reference variables from the containing scope
- `lambda value: value * 2`

#### Function Annotations

- Function annotations are completely optional metadata information about the types used by user-defined functions
  - see [PEP 3107](https://www.python.org/dev/peps/pep-3107) and [PEP 484](https://www.python.org/dev/peps/pep-0484) for more information
- Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation
- Return annotations are defined by a literal `->`, followed by an expression, between the parameter list and the colon denoting the end of the `def` statement
- Example: `def function_annotations(ham: str, eggs: str = "eggs") -> str`

## Source

- "The Python Tutorial." _The Python Tutorial - Python 3.8.3 Documentation_, 19 May 2020, docs.python.org/3/tutorial/index.html.
