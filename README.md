# The Python Tutorial

Examples from [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (mostly).

- [The Python Tutorial](#the-python-tutorial)
  - [3. An Informal Introduction to Python](#3-an-informal-introduction-to-python)
    - [Numbers](#numbers)
    - [Strings](#strings)
    - [Lists](#lists)
  - [4. More Control Flow Tools](#4-more-control-flow-tools)
    - [`if` Statements](#if-statements)
    - [`for` Statements](#for-statements)
    - [The `range()` Function](#the-range-function)
    - [`break` and `continue` Statements, and `else` Clauses on Loops](#break-and-continue-statements-and-else-clauses-on-loops)
    - [`pass` Statements](#pass-statements)
    - [Defining Functions](#defining-functions)
    - [More on Defining Functions](#more-on-defining-functions)
      - [Default Argument Values](#default-argument-values)
      - [Keyword Arguments](#keyword-arguments)
      - [Special parameters](#special-parameters)
        - [Positional-or-Keyword Arguments](#positional-or-keyword-arguments)
        - [Positional-Only Parameters](#positional-only-parameters)
        - [Keyword-Only Arguments](#keyword-only-arguments)
      - [Arbitrary Argument Lists](#arbitrary-argument-lists)
      - [Unpacking Argument Lists](#unpacking-argument-lists)
      - [Lambda Expressions](#lambda-expressions)
      - [Function Annotations](#function-annotations)
  - [5. Data Structures](#5-data-structures)
    - [More on Lists](#more-on-lists)
      - [Using Lists as Stacks](#using-lists-as-stacks)
      - [Using Lists as Queues](#using-lists-as-queues)
      - [List Comprehensions](#list-comprehensions)
      - [Nested List Comprehensions](#nested-list-comprehensions)
    - [The `del` Statement](#the-del-statement)
    - [Tuples and Sequences](#tuples-and-sequences)
    - [Sets](#sets)
    - [Dictionaries](#dictionaries)
    - [Looping Techniques](#looping-techniques)
    - [More on Conditions](#more-on-conditions)
  - [6. Modules](#6-modules)
    - [More on Modules](#more-on-modules)
      - [Executing modules as scripts](#executing-modules-as-scripts)
      - [The Module Search Path](#the-module-search-path)
      - ["Compiled" Python files](#compiled-python-files)
    - [Standard Modules](#standard-modules)
    - [The `dir()` Function](#the-dir-function)
    - [Packages](#packages)
      - [Importing `*` From a Package](#importing--from-a-package)
      - [Intra-package References](#intra-package-references)
      - [Packages in Multiple Directories](#packages-in-multiple-directories)
      - [Namespace packages](#namespace-packages)
  - [7. Input and Output](#7-input-and-output)
    - [Fancier Output Formatting](#fancier-output-formatting)
      - [Formatted String Literals](#formatted-string-literals)
      - [The String `format()` Method](#the-string-format-method)
      - [Manual String Formatting](#manual-string-formatting)
      - [Old String Formatting](#old-string-formatting)
    - [Reading and Writing Files](#reading-and-writing-files)
      - [Methods of File Objects](#methods-of-file-objects)
      - [Saving structured data with json](#saving-structured-data-with-json)
  - [8. Errors and Exceptions](#8-errors-and-exceptions)
    - [Exceptions](#exceptions)
    - [Handling Exceptions](#handling-exceptions)
    - [Raising Exceptions](#raising-exceptions)
    - [User-defined Exceptions](#user-defined-exceptions)
    - [Defining Clean-up Actions](#defining-clean-up-actions)
  - [9. Classes](#9-classes)
    - [A Word About Names and Objects](#a-word-about-names-and-objects)
    - [Python Scopes and Namespaces](#python-scopes-and-namespaces)
    - [A First Look at Classes](#a-first-look-at-classes)
      - [Class Definition Syntax](#class-definition-syntax)
      - [Class Objects](#class-objects)
      - [Instance Objects](#instance-objects)
      - [Method Objects](#method-objects)
      - [Class and Instance Variables](#class-and-instance-variables)
    - [Random Remarks](#random-remarks)
    - [Inheritance](#inheritance)
      - [Multiple Inheritance](#multiple-inheritance)
      - [Mixins](#mixins)
    - [Private Variables](#private-variables)
    - [Odds and Ends](#odds-and-ends)
    - [Iterators](#iterators)
    - [Generators](#generators)
    - [Generator Expressions](#generator-expressions)
  - [10. Brief Tour of the Standard Library](#10-brief-tour-of-the-standard-library)
    - [Operating System Interface](#operating-system-interface)
    - [File Wildcards](#file-wildcards)
    - [Command Line Arguments](#command-line-arguments)
    - [Error Output Redirection and Program Termination](#error-output-redirection-and-program-termination)
    - [String Pattern Matching](#string-pattern-matching)
    - [Mathematics](#mathematics)
    - [Internet Access](#internet-access)
    - [Dates and Times](#dates-and-times)
      - [Aware and Naive Objects](#aware-and-naive-objects)
      - [Determining if an Object is Aware or Naive](#determining-if-an-object-is-aware-or-naive)
      - [Common Properties](#common-properties)
      - [`timedelta` Objects](#timedelta-objects)
      - [`date` Objects](#date-objects)
      - [`datetime` Objects](#datetime-objects)
      - [`strftime()` and `strptime()` Behavior](#strftime-and-strptime-behavior)
    - [Data Compression](#data-compression)
      - [`zipfile`](#zipfile)
    - [Performance Measurement](#performance-measurement)
    - [Quality Control](#quality-control)
    - [Batteries Included](#batteries-included)
      - [`csv`](#csv)
      - [`xml.etree.ElementTree`](#xmletreeelementtree)
      - [`sqlite3`](#sqlite3)
      - [`gettext`](#gettext)
  - [11. Brief Tour of the Standard Library - Part II](#11-brief-tour-of-the-standard-library---part-ii)
    - [Output Formatting](#output-formatting)
      - [`reprlib`](#reprlib)
      - [`pprint`](#pprint)
      - [`locale`](#locale)
    - [Templating](#templating)
    - [Multi-threading](#multi-threading)
    - [Logging](#logging)
    - [Weak References](#weak-references)
    - [Tools for Working with Lists](#tools-for-working-with-lists)
      - [`array`](#array)
      - [`collections` and `deque`](#collections-and-deque)
      - [`bisect`](#bisect)
      - [`heapq`](#heapq)
    - [Decimal Floating Point Arithmetic](#decimal-floating-point-arithmetic)
  - [12. `enum` - Enumerations](#12-enum---enumerations)
  - [13. Hashable Objects in Sets and Dictionaries](#13-hashable-objects-in-sets-and-dictionaries)
  - [Main Source](#main-source)

## 3. An Informal Introduction to Python

- Based on <https://docs.python.org/3/tutorial/introduction.html>

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

- See [`strings_test.py`](src/ch03/strings_test.py)
- Strings can be enclosed in single quotes (`'...'`) or double quotes (`"..."`)
  - `\` can be used to escape quotes
- If you don't want characters prefaced by `\` to be interpreted as special characters, you can use **raw strings** by adding an `r` before the first quote
  - `r"c:\some\name"`
  - see `test_raw_strings()`
- String literals can span **multiple lines**
  - one way is using triple-quotes: `"""..."""` or `'''...'''`
  - end of lines are automatically included in the string
    - possible to prevent this by adding a `\` at the end of the line
  - see `test_multiline()`
- Strings can be **concatenated** with the `+` operator, and **repeated** with `*`
  - `some_str = 2 * "pa" + "dum"`
  - repeated concatenation will have a quadratic runtime cost in the total sequence length
  - to get a linear runtime cost, you must switch to one of the alternatives below:
    - build a list and use [`str.join()`](https://docs.python.org/3/library/stdtypes.html#str.join) at the end
      - `strings = ["some", "strings"]`
      - `" ".join(strings)`
    - write to an [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO) instance and retrieve its value when complete
      - `buffer = io.StringIO()`
      - `buffer.write("some")`
      - `stringio_content = buffer.getvalue()`
  - see `test_concat_repeat()`
- Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated
  - `some_str = "Breaking a long " "string"`
  - see `test_concat_string_literal()`
- Strings can be **indexed** (subscripted), with the first character having index 0
  - there is no separate character type; a character is simply a string of size one
  - indices may also be negative numbers, to start counting from the right
  - `some_str[0]`
  - see `test_string_index()`
- **Slicing** is also supported
  - allows you to obtain substring
  - `some_str[2:4]`
  - see `test_string_slice()`
- Python strings cannot be changed - they are **immutable**
  - assigning to an indexed position in the string results in an error
  - see `test_immutable_string()`
- The built-in function **`len()`** returns the length of a string
  - `len(some_str)`
  - see `test_string_len()`
- See also:
  - [Text Sequence Type - str](https://docs.python.org/3/library/stdtypes.html#textseq)
    - strings are examples of sequence types, and support the [common operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) supported by such types
    - see `test_text_sequence_type()`
  - [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
    - strings support a large number of methods for basic transformations and searching
    - see `test_string_methods()`
  - [Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    - string literals that have embedded expressions
      - `name = "Fred"`
      - `f"He said his name is {name!r}"`
    - see `test_formatted_string_literals()`
  - [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
    - information about string formatting with `str.format()`
    - `"{1}, {0}, {2}".format("a", "b", "c")`
    - see `test_format_string_syntax()`
  - [printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)
    - the old formatting operations invoked when strings are the left operand of the `%` operator are described in more detail here

### Lists

- See [`lists_test.py`](src/ch03/lists_test.py)
- A list can be written as a list of comma-separated values (items) between square brackets
  - `[1, 4, 9, 16, 25]`
- Lists might contain items of different types, but usually the items all have the same type
- Lists can be **indexed** and **sliced**
  - all slice operations return a new list containing the requested elements
  - slice returns a shallow copy of the list
  - `squares[2]`
  - `squares[2:]`
  - see `test_list_index_slice()`
- Lists also support operations like **concatenation** (`+`)
  - `squares += [16, 25]`
  - see `test_list_concat()`
- Lists are a **mutable** type, i.e. it is possible to change their content
  - `cubes[3] = 64`
  - see `test_list_mutable()`
- You can also add new items at the end of the list, by using the **`append()`** method
  - `squares.append(4 ** 2)`
  - see `test_list_append()`
- **Assignment to slices** is also possible, and this can even change the size of the list or clear it entirely
  - `letters[1:3] = ["B", "C"]`
  - `letters[:] = []`
  - see `test_list_assign_to_slice()`
- The built-in function **`len()`** also applies to lists
  - `len(["a", "b", "c", "d", "e"])`
  - see `test_list_len()`
- It is possible to **nest** lists
  - `[["a", "b", "c"], [1, 2]]`
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

## 5. Data Structures

- Based on <https://docs.python.org/3/tutorial/datastructures.html>

### More on Lists

- See [`more_lists_test.py`](src/ch05/more_lists_test.py)
- **`list.append(x)`**
  - add an item to the end of the list
  - equivalent to `a[len(a):] = [x]`
  - see `test_append()`
- **`list.extend(iterable)`**
  - extend the list by appending all the items from the iterable
  - equivalent to `a[len(a):] = iterable`
  - see `test_extend()`
- **`list.insert(i, x)`**
  - insert an item at a given position
  - see `test_insert()`
- **`list.remove(x)`**
  - remove the first item from the list whose value is equal to `x`
  - raises a `ValueError` if there is no such item
  - see `test_remove()`
- **`list.pop([i])`**
  - remove the item at the given position in the list, and return it
  - if no index is specified, `a.pop()` removes and returns the last item in the list
  - (the square brackets around the `i` denote that the parameter is optional)
  - see `test_pop()`
- **`list.clear()`**
  - remove all items from the list
  - equivalent to `del a[:]`
  - see `test_clear()`
- **`list.index(x[, start[, end]])`**
  - return zero-based index in the list of the first item whose value is equal to `x`
  - raises a `ValueError` if there is no such item
  - the optional arguments `start` and `end` are interpreted as in the slice notation
    - used to limit the search to a particular subsequence of the list
    - the returned index is computed relative to the beginning of the full sequence rather than the `start` argument
  - see `test_index()`
- **`list.count(x)`**
  - return the number of times `x` appears in the list
  - see `test_count()`
- **`list.sort(key=None, reverse=False)`**
  - sort the items of the list in place
    - the arguments can be used for sort customization, see [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) for their explanation
  - see `test_sort()`
- **`list.reverse()`**
  - reverse the elements of the list in place
  - see `test_reverse()`
- **`list.copy()`**
  - return a shallow copy of the list
  - equivalent to `a[:]`
  - see `test_sort()`
- Methods like `insert`, `remove` or `sort` that only modify the list have no return value
  - this is a design principle for all mutable data structures in Python

#### Using Lists as Stacks

- See [`stacks_queues_test.py`](src/ch05/stacks_queues_test.py)
- Stack, where the last element added is the first element retrieved (LIFO)
  - to add an item to the top of the stack, use **`append()`**
  - to retrieve an item from the top of the stack, use **`pop()`** without an explicit index
- See `test_list_stack()`

#### Using Lists as Queues

- See [`stacks_queues_test.py`](src/ch05/stacks_queues_test.py)
- Queue, where the first element added is the first element retrieved (FIFO)
- Lists are not efficient for this purpose
  - while `append`s and `pop`s from the end of list are fast, doing `insert`s or `pop`s from the beginning of a list is slow
    - all of the other elements have to be shifted by one
    - O(n) memory movement costs
  - see `test_list_queue_slow()`
- To implement a queue, use [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque) which was designed to have fast `append`s and `pop`s from both ends
  - approximately O(1) performance
  - `deque([iterable[, maxlen]])`
  - see `test_list_queue_fast()`

#### List Comprehensions

- See [`list_comprehensions_test.py`](src/ch05/list_comprehensions_test.py)
- A concise way to create lists
  - each element is the result of some operations applied to each member of another sequence or iterable
  - a subsequence of those elements that satisfy a certain condition
- Consists of brackets containing
  - an expression,
  - followed by a `for` clause,
  - then zero or more `for` or `if` clauses
- The result will be a new list
- Some examples
  - `[num ** 2 for num in range(5)]`
  - `[(i, j) for i in [1, 2, 3] for j in [3, 1, 4] if i != j]`
  - `[elem for elem in [-4, -2, 0, 2, 4] if elem >= 0]`
  - `[str(round(math.pi, precision)) for precision in range(1, 4)]`
  - `[letter.upper() for letter in "abcde"]`

#### Nested List Comprehensions

- See [`list_comprehensions_test.py`](src/ch05/list_comprehensions_test.py)
- The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension
- `[[row[elem] for row in matrix] for elem in range(4)]`
- See `test_nested_listcomp()`

### The `del` Statement

- See [`del_test.py`](src/ch05/del_test.py)
- Remove an item from a list given its index instead of its value
- Can also be used to remove slices from a list or clear the entire list

### Tuples and Sequences

- See [`tuples_sequences_test.py`](src/ch05/tuples_sequences_test.py)
- There are 3 basic sequence types: lists, tuples, and range objects
  - additional sequence types tailored for processing of [binary data](https://docs.python.org/3/library/stdtypes.html#binaryseq) and [text strings](https://docs.python.org/3/library/stdtypes.html#textseq)
- Empty [tuple](https://docs.python.org/3/library/stdtypes.html#tuples)s are constructed by an empty pair of parentheses
- A tuple with one item (singleton) is constructed by following a value with a comma
  - not sufficient to enclose a single value in parentheses
  - `single_elem_tuple = (1,)`
- A tuple consists of a number of values separated by commas
  - may be constructed with or without surrounding parentheses
  - may be constructed using the [`tuple()`](https://docs.python.org/3/library/stdtypes.html#tuple) built-in
  - usually contain a heterogeneous sequence of elements
  - `packed_tuple: Tuple[int, int, str] = 1, 2, "c"`
- Tuple packing - multiple values can be packed together in a tuple
- Sequence unpacking
  - works for any sequence (but not `str`) on the right-hand side
  - requires that there are as many variables on the left side of the equals sign as there are elements in the sequence
  - `one, two, three = packed_tuple`
  - multiple assignment is really just a combination of tuple packing and sequence unpacking
- Tuples
  - elements are accessed via unpacking or indexing (or even by attribute in the case of `namedtuples`)
  - may be nested
  - are immutable
  - implement all of the [common sequence operations](https://docs.python.org/3/library/stdtypes.html#typesseq-common)
- For heterogeneous collections of data where access by name is clearer than access by index, [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple) may be a more appropriate choice than a simple tuple object
  - see also <https://github.com/jashburn8020/python-type-hints-mypy#named-tuples>

### Sets

- See [`sets_test.py`](src/ch05/sets_test.py)
- A [set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) object is an unordered collection of distinct _hashable_ objects
  - basic uses include membership testing and eliminating duplicate entries
- Curly braces or the `set([iterable])` function can be used to create sets
  - to create an empty set you have to use `set()`, not `{}`; the latter creates an empty dictionary
- Being an _unordered collection_, sets
  - do not record element position or order of insertion
  - do not support indexing, slicing, or other sequence-like behavior
- The set type is _mutable_
  - contents can be changed using methods like `add()` and `remove()`
  - since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set
  - the `frozenset` type is immutable
- Similarly to list comprehensions, set comprehensions are also supported
- Set objects support mathematical operations like
  - difference:
    - `difference(*others)`
    - `set - other - ...`
    - return a new set with elements in the set that are not in the others
  - symmetric difference:
    - `symmetric_difference(other)`
    - `set ^ other`
    - return a new set with elements in either the set or other but not both
  - union
    - `union(*others)`
    - `set | other | ...`
    - return a new set with elements from the set and all others
  - intersection
    - `intersection(*others)`
    - `set & other & ...`
    - return a new set with elements common to the set and all others
  - subset
    - `issubset(other)`
    - `set <= other`
    - test whether every element in the set is in other
  - proper subset
    - `set < other`
    - test whether the set is a proper subset of other, that is, `set <= other and set != other`
  - superset
    - `issuperset(other)`
    - `set >= other`
    - test whether every element in other is in the set
  - proper superset
    - `set > other`
    - test whether the set is a proper superset of other, that is, `set >= other and set != other`
  - disjoint
    - `isdisjoint(other)`
    - return `True` if the set has no elements in common with other
    - sets are disjoint if and only if their intersection is the empty set
- The method versions of the operations will accept any iterable as an argument
  - in contrast, their operator based counterparts require their arguments to be sets

### Dictionaries

- See [`dictionaries_test.py`](src/ch05/dictionaries_test.py)
- [Dictionaries](https://docs.python.org/3/library/stdtypes.html#typesmapping) are indexed by keys, which can be any _immutable_ type
- It is best to think of a dictionary as a set of key:value pairs, with the requirement that the keys are unique (within one dictionary)
- Constructing a dictionary:
  - a pair of braces creates an empty dictionary: `{}`
  - placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary
    - `{"banana": 5, "cherry": 4, "durian": 2}`
  - the `dict()` constructor builds dictionaries directly from sequences of key-value pairs
    - `dict([("banana", 5), ("cherry", 4), ("durian", 2)])`
  - when the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
    - `dict(banana=5, cherry=4, durian=2)`
  - see `test_construct_dictionary()`
  - dict comprehensions can be used to create dictionaries from arbitrary key and value expressions
    - `{even: even ** 2 for even in range(10) if even % 2 == 0}`
    - see `test_dict_comprehension()`
- The main operations on a dictionary are storing a value with some key and extracting the value given the key
  - `fruits["banana"] = 5`
  - if you store using a key that is already in use, the old value associated with that key is forgotten
- It is also possible to delete a key:value pair with `del`
  - `del fruits["banana"]`
- See `test_store_extract_del()`
- Dictionaries compare equal if and only if they have the same (key, value) pairs (regardless of ordering)
- Dictionaries preserve _insertion order_
- Some other [operations](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) that dictionaries support:
  - **`list(d)`**
    - return a list of all the keys used in the dictionary `d` in insertion order
    - use **`sorted(d)`** to get a sorted list of keys
  - **`len(d)`**
    - return the number of items in the dictionary `d`
  - **`key in d`**
    - return `True` if `d` has a key `key`
    - see `test_list_len_key_in()`
  - **`clear()`**
    - remove all items from the dictionary
  - **`copy()`**
    - return a shallow copy of the dictionary
  - **`setdefault(key[, default])`**
    - if `key` is in the dictionary, return its value
    - if not, insert key with a value of `default` and return `default`
    - `default` defaults to `None`
  - **`update([other])`**
    - update the dictionary with the key/value pairs from `other`, overwriting existing keys
    - accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two)
    - if keyword arguments are specified, the dictionary is then updated with those key/value pairs
  - **`get(key[, default])`**
    - return the value for `key` if `key` is in the dictionary, else `default`
    - if `default` is not given, it defaults to `None`, so that this method never raises a `KeyError`
  - **`pop(key[, default])`**
    - if `key` is in the dictionary, remove it and return its value, else return `default`
    - if `default` is not given and `key` is not in the dictionary, a `KeyError` is raised
  - **`popitem()`**
    - remove and return a `(key, value)` pair from the dictionary
    - pairs are returned in LIFO order
    - see `test_more_set_get()`
- **View objects**
  - the following operations return view objects:
    - **`items()`**
      - return a new view of the dictionary's items (`(key, value)` pairs): [`ItemsView`](https://docs.python.org/3/library/collections.abc.html?highlight=itemsview#collections.abc.ItemsView)
    - **`keys()`**
      - return a new view of the dictionary's keys: [`KeysView`](https://docs.python.org/3/library/collections.abc.html?highlight=itemsview#collections.abc.KeysView)
    - **`values()`**
      - return a new view of the dictionary's values: [`ValuesView`](https://docs.python.org/3/library/collections.abc.html?highlight=itemsview#collections.abc.ValuesView)
      - equality comparison between one `dict.values()` view and another will always return `False`
  - provide a dynamic view on the dictionary's entries
  - when the dictionary changes, the view reflects these changes
  - keys views are set-like since their entries are unique and hashable
  - if all values are hashable, so that (key, value) pairs are unique and hashable, then the items view is also set-like
  - values views are not treated as set-like since the entries are generally not unique
  - for set-like views, all of the operations defined for the abstract base class `collections.abc.Set` are available (for example, `==`, `<`, and `^`)
  - see `test_view_objects()`
  - `types.MappingProxyType` can be used to create a read-only view of a `dict`
    - see `test_mappingproxytype()`

### Looping Techniques

- See [`looping_techniques_test.py`](src/ch05/looping_techniques_test.py)
- When looping through _dictionaries_, the key and corresponding value can be retrieved at the same time using the **`items()`** method
  - `for name, value in knights_dict.items()`
  - see `test_dict_items()`
- When looping through a _sequence_, the position index and corresponding value can be retrieved at the same time using the **`enumerate(iterable, start=0)`** function
  - `for index, value in enumerate(["tic", "tac", "toe"], start=1)`
  - see `test_seq_enumerate()`
- To loop over _two or more sequences_ at the same time, the entries can be paired with the **`zip(*iterables)`** function
  - returns an iterator of tuples; the iterator stops when the shortest input iterable is exhausted
  - `for attr, value in zip(attrs, values)`
  - see `test_seqs_zip()`
- To loop over a _sequence in reverse_, first specify the sequence in a forward direction and then call the **`reversed(seq)`** function
  - returns a reverse iterator
  - `for fruit in reversed(["banana", "cherry", "durian"])`
  - see `test_seq_reversed()`
- To loop over a _sequence in sorted order_, use the **`sorted(iterable, *, key=None, reverse=False)`** function
  - `key` specifies a one-argument function to be called on each list element prior to making comparisons
  - returns a new sorted list from the items in iterable
  - `for fruit_name in sorted(fruits_amount, key=lambda fruit: fruit[1])`
  - see `test_seq_sorted()`
- It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead
  - see `test_changing_list()`

### More on Conditions

- The conditions used in `while` and `if` statements can contain any operators, not just comparisons
- The comparison operators `in` and `not in`
  - check whether a value occurs (does not occur) in a sequence
- The operators `is` and `is not` compare whether two objects are really the same object
  - this only matters for mutable objects like lists
- All comparison operators have the same priority
  - lower than that of all numerical operators
- Comparisons can be chained
  - e.g., `a < b == c` tests whether `a` is less than `b` and moreover `b` equals `c`
- Comparisons may be combined using the Boolean operators `and` and `or`
  - short-circuit operators
- The outcome of a comparison (or of any other Boolean expression) may be negated with `not`
- Boolean operators have lower priorities than comparison operators
  - between them, `not` has the highest priority and `or` the lowest
  - `A and not B or C` is equivalent to `(A and (not B)) or C`
- Assignment inside expressions must be done explicitly with the **walrus operator** `:=` (Python 3.8)
  - see [PEP 572 -- Assignment Expressions](https://www.python.org/dev/peps/pep-0572/)

```python
# Handle a matched regex
if (match := pattern.search(data)) is not None:
    # Do something with match

# A loop that can't be trivially rewritten using 2-arg iter()
while chunk := file.read(8192):
    process(chunk)

# Reuse a value that's expensive to compute
[y := f(x), y**2, y**3]

# Share a subexpression between a comprehension filter clause and its output
filtered_data = [y for x in data if (y := f(x)) is not None]
```

## 6. Modules

- A module is a file containing Python definitions and statements
- The file name is the module name with the suffix `.py` appended
- Within a module, the module's name (as a string) is available as the value of the global variable `__name__`
- Consider a file called `fibo.py` containing a function, `fib(n)`, created in the current directory
  - **`import fibo`**
    - this does not enter the names of the function defined in `fibo` directly in the current symbol table
    - it only enters the module name `fibo` there
  - using the module name you can access its function
    `fibo.fib(1000)`

### More on Modules

- A module can contain executable statements as well as function definitions
  - these statements are intended to initialize the module
    - they are executed only the _first_ time the module name is encountered in an `import` statement
    - they are also run if the file is executed as a script
  - function definitions in a module are also 'statements' that are 'executed'
    - execution of a module-level function definition enters the function name in the module's global symbol table
  - see [`demo_import.py`](src/ch06/demo_import.py) and [`fibo.py`](src/ch06/fibo.py)

```console
$ python ch06/demo_import.py
Initialise fibo
Initialise demo_import
0 1 1 2 3
```

- Each module has its own private symbol table
  - used as the global symbol table by all functions defined in the module
- Imported module names are placed in the importing module's global symbol table
- There is a variant of the `import` statement that imports names from a module directly into the importing module's symbol table
  - **`from fibo import fib`**
  - this does not introduce the module name from which the imports are taken in the local symbol table
    - in the example, `fibo` is not defined
- There is even a variant to import all names that a module defines
  - `from fibo import *`
  - this imports all names except those beginning with an underscore (`_`)
  - not recommended because it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined
- If the module name is followed by `as`, then the name following `as` is bound directly to the imported module
  - **`import fibo as fib`**
  - `fib.fib(500)`
  - this is effectively importing the module in the same way that `import fibo` will do, with the only difference of it being available as `fib`
  - it can also be used when utilising `from` with similar effects
    - **`from fibo import fib as fibonacci`**
    - `fibonacci(500)`

#### Executing modules as scripts

- When you run a Python module with `python fibo.py <arguments>`
  - the code in the module will be executed, just as if you imported it
  - but with `__name__` set to `"__main__"`
- By adding the following code at the end of your module, you can make the file usable as a script as well as an importable module
  - see [`demo_import.py`](src/ch06/demo_import.py)

```python
if __name__ == "__main__":
    import sys

    fibo.fib(int(sys.argv[1]))
```

```console
$ python ch06/demo_import.py 10
Initialise fibo
Initialise demo_import
0 1 1 2 3
0 1 1 2 3 5 8
```

#### The Module Search Path

- When a module named `spam` is imported
  - the interpreter first searches for a built-in module with that name
  - if not found, it then searches for a file named `spam.py` in a list of directories given by the variable `sys.path`
- **`sys.path`** is initialized from these locations:
  - the directory containing the input script (or the current directory when no file is specified)
  - `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable `PATH`)
  - the installation-dependent default
- Note: On file systems which support **symlinks**, the directory containing the input script is calculated after the symlink is followed
  - in other words the directory containing the symlink is _not_ added to the module search path
- After initialization, Python programs can modify `sys.path`
  - the directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path
    - scripts in that directory will be loaded instead of modules of the same name in the library directory
- See [`syspath.py`](src/ch06/syspath.py)
- `sys.path` from a script outside a virtual environment:

```console
$ python ch06/syspath.py
['/path/to/directory/containing/script', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages']
```

- `sys.path` from a script in a virtual environment:

```console
$ python ch06/syspath.py
['/path/to/directory/containing/script', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/path/to/venv/lib/python3.8/site-packages']
```

#### "Compiled" Python files

- To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name `module.version.pyc`, where the version encodes the format of the compiled file; it generally contains the Python version number
  - e.g., `fibo.cpython-38.pyc`
- Python does not check the cache in two circumstances
  - it always recompiles and does not store the result for the module that's loaded directly from the command line
  - it does not check the cache if there is no source module
    - to support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module
- A program doesn't run any faster when it is read from a `.pyc` file than when it is read from a `.py` file
  - the only thing that's faster about `.pyc` files is the speed with which they are loaded
- See [PEP 3147 -- PYC Repository Directories](https://www.python.org/dev/peps/pep-3147/)

### Standard Modules

- Python comes with a library of standard modules, described in a separate document, the Python Library Reference
- Some modules are built into the interpreter
  - provide access to operations that are not part of the core of the language
  - built in either for efficiency or to provide access to operating system primitives such as system calls
  - the set of such modules is a configuration option which also depends on the underlying platform
    - e.g., the `winreg` module is only provided on Windows systems
  - one particular module deserves some attention: `sys`, which is built into every Python interpreter

### The `dir()` Function

- The built-in function [`dir()`](https://docs.python.org/3/library/functions.html#dir) is used to find out which names a module defines
  - variables, modules, functions, etc.
  - returns a sorted list of strings
- Does not list the names of built-in functions and variables
  - defined in the standard module `builtins`
    - [built-in functions](https://docs.python.org/3/library/functions.html#built-in-funcs)
    - [built-in constants](https://docs.python.org/3/library/constants.html#built-in-consts)

### Packages

- Packages are a way of structuring Python's module namespace by using "dotted module names"
  - e.g., the module name `A.B` designates a submodule named `B` in a package named `A`
- Just like the use of modules saves the authors of different modules from having to worry about each other's global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other's module names
- Suppose you want to design a collection of modules (a "package") for the uniform handling of sound files and sound data

```text
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              ...
```

- When importing the package, Python searches through the directories on `sys.path` looking for the package subdirectory
- The **`__init__.py`** files are required to make Python treat directories containing the file as (regular) packages
  - (see also [namespace packages](#namespace-packages))
  - prevents directories with a common name, such as `string`, unintentionally hiding valid modules that occur later on the module search path
  - in the simplest case, can just be an empty file
  - can also execute initialization code for the package or set the `__all__` variable (described later)
- Users of the package can import individual modules from the package
  - `import sound.effects.echo`
    - loads the submodule `sound.effects.echo`
    - referenced with its full name
    - `sound.effects.echo.echofilter(...)`
  - `from sound.effects import echo`
    - also loads the submodule `echo`, and makes it available without its package prefix
    - `echo.echofilter(...)`
  - `from sound.effects.echo import echofilter`
    - loads the submodule `echo`, but this makes its function `echofilter()` directly available
    - `echofilter(...)`
- When using syntax like **`import item.subitem.subsubitem`**
  - each item except for the last must be a package
  - the last item can be a module or a package but can't be a class or function or variable defined in the previous item
- When using **`from package import item`**
  - `item` can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable
  - the `import` statement first tests whether the item is defined in the package
    - if not, it assumes it is a module and attempts to load it
    - if it fails to find it, an `ImportError` exception is raised

#### Importing `*` From a Package

- What happens when the user writes `from sound.effects import *`?
- If a package's `__init__.py` code defines a list named **`__all__`**
  - it is taken to be the list of module names that should be imported
  - e.g., the file `sound/effects/__init__.py` could contain the following code:
    - `__all__ = ["echo", "surround", "reverse"]`
- If `__all__` is not defined
  - does _not_ import all submodules from the package `sound.effects` into the current namespace
  - only ensures that the package `sound.effects` has been imported (possibly running any initialization code in `__init__.py`) and then imports whatever names are defined in the package
    - includes any names defined (and submodules explicitly loaded) by `**init**.py
    - also includes any submodules of the package that were explicitly loaded by previous `import` statements

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

- In this example, the `echo` and `surround` modules are imported in the current namespace because they are defined in the `sound.effects` package when the `from...import statement` is executed
  - this also works when `__all__` is defined
- `import *` is considered bad practice in production code
- `from package import specific_submodule` is the recommended notation unless the importing module needs to use submodules with the same name from different packages

#### Intra-package References

```text
sound/
      __init__.py
      formats/
              __init__.py
              ...
      effects/
              __init__.py
              echo.py
              surround.py
              ...
      filters/
              __init__.py
              equalizer.py
              vocoder.py
              ...
```

- When packages are structured into subpackages, you can use **absolute imports** to refer to submodules of siblings packages
  - e.g., if the module `sound.filters.vocoder` needs to use the `echo` module in the `sound.effects` package, it can use `from sound.effects import echo`
- You can also write **relative imports**, with the `from module import name` form
  - use leading dots to indicate the current and parent packages involved in the relative import
  - 1 leading dot means the current package where the module making the import exists
  - 2 dots means up one package level, and 3 dots is up two levels
  - e.g., from the `surround` module, you might use:

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

#### Packages in Multiple Directories

- Packages support one more special attribute, **`__path__`**
  - initialized to be a list containing the name of the directory holding the package's `__init__.py` before the code in that file is executed
  - can be modified; doing so affects future searches for modules and subpackages contained in the package
- While this feature is not often needed, it can be used to extend the set of modules found in a package

#### Namespace packages

- A [PEP 420](https://www.python.org/dev/peps/pep-0420/) package which serves only as a container for subpackages
- A mechanism for splitting a single Python package across multiple directories on disk
- Have no `__init__.py` file
- Multiple portions of a namespace package can be installed into the same directory, or into separate directories
- Suppose there are two portions which define `foo.bar` and `foo.baz`
  - `foo` is a namespace package
  - if these are installed in the same location
    - a single directory `foo` would be in a directory that is on `sys.path`
    - inside `foo` would be two directories, `bar` and `baz`
  - if the portions are installed in different locations
    - two different `foo` directories would be in directories that are on `sys.path`
      - `foo/bar` would be in one of these `sys.path` entries, and `foo/baz` would be in the other
    - it is also possible to have the `foo.bar` portion installed in a directory on `sys.path`, and have the `foo.baz` portion provided in a zip file, also on `sys.path`
- Further example:

```text
Lib/test/namespace_pkgs
    project1
        parent
            child
                one.py
    project2
        parent
            child
                two.py
```

- Both `parent` and `child` are namespace packages
  - portions of them exist in different directories, and they do not have `__init__.py` files

```text
>>> import sys
>>> sys.path += ['Lib/test/namespace_pkgs/project1', 'Lib/test/namespace_pkgs/project2']
>>> import parent.child.one
>>> parent.__path__
_NamespacePath(['Lib/test/namespace_pkgs/project1/parent', 'Lib/test/namespace_pkgs/project2/parent'])
>>> parent.child.__path__
_NamespacePath(['Lib/test/namespace_pkgs/project1/parent/child', 'Lib/test/namespace_pkgs/project2/parent/child'])
>>> import parent.child.two
>>>
```

## 7. Input and Output

### Fancier Output Formatting

- See [`str_repr_test.py`](src/ch07/str_repr_test.py)
- When you don't need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the `repr()` or `str()` functions
- [**`class str(object='')`**](https://docs.python.org/3/library/stdtypes.html#str)
  - returns `object.__str__()`, which is the **"informal" or nicely printable** string representation of object
    - also called by the built-in functions `format()` and `print()`
    - differs from `object.__repr__()` in that there is no expectation that `__str__()` return a valid Python expression
  - if `object` does not have a `__str__()` method, then `str()` falls back to returning `repr(object)`
- [**`repr()`**](https://docs.python.org/3/library/functions.html#repr)
  - returns a string containing a printable representation of an object
  - for many types, this function makes an attempt to return a string that would yield an object with the same value when passed to `eval()`
    - otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information, often including the name and address of the object
  - typically used for **debugging**
  - a class can control what this function returns for its instances by defining a `__repr__()` method
- For objects which don't have a particular representation for human consumption, `str()` will return the same value as `repr()`
  - many values, such as numbers or structures like lists and dictionaries, have the same representation using either function
  - strings, in particular, have two distinct representations
- See also [`Templating`](#templating)

#### Formatted String Literals

- See [`f_string_test.py`](src/ch07/f_string_test.py)
- A [formatted string literal](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) (also called f-string for short) is a string literal that is prefixed with `f` or `F`
  - may contain **replacement fields**, which are expressions delimited by curly braces **`{}`**
    - the grammar for a replacement field:
      - `replacement_field ::= "{" f_expression ["!" conversion] [":" format_spec] "}"`
  - the parts of the string outside curly braces are treated literally
    - except that any doubled curly braces `{{` or `}}` are replaced with the corresponding single curly brace
  - a single opening curly bracket `{` marks a replacement field, which starts with a Python expression
  - after the expression, there may be a **conversion field**, introduced by an exclamation point **`!`**
  - a **format specifier** may also be appended, introduced by a colon **`:`**
  - a replacement field ends with a closing curly bracket `}`
- **Expressions** in formatted string literals are treated like regular Python expressions surrounded by parentheses, with a few exceptions
  - an empty expression is not allowed
  - both lambda and assignment expressions `:=` must be surrounded by explicit parentheses
  - can contain line breaks (e.g. in triple-quoted strings), but they cannot contain comments
  - each expression is evaluated in the context where the formatted string literal appears, in order from left to right
- If a **conversion** is specified (`!`)
  - the result of evaluating the expression is converted before formatting
  - **`!s`** calls `str()` on the result
  - **`!r`** calls `repr()`
  - **`!a`** calls `ascii()`
  - `f"The {animal!s}'s name is {name!r}"`
  - see `test_conversion_modifiers()`
- The result is then **formatted** using the `format()` protocol (`:`)
  - top-level format specifiers may include nested replacement fields
    - `"result: {value:{width}.{precision}}"`
    - see `test_format_nested_fields()`
  - nested fields may include their own conversion fields and format specifiers
    - may not include more deeply-nested replacement fields
  - the [format specifier mini-language](https://docs.python.org/3/library/string.html#formatspec) is the same as that used by the string `.format()` method
    - `f"pi is approximately {math.pi:.3f}"`
    - `f"{'Sjoerd':10} ==> {table['Sjoerd']:10d}"`
    - `f"{name + ' ':.<10}{' ' + str(phone):.>10}"`
    - `f"{timestamp:%d %B %Y %H:%M:%S}"`
- Formatted string literals may be concatenated, but replacement fields cannot be split across literals

#### The String `format()` Method

- See [`string_format_test.py`](src/ch07/string_format_test.py)
- `str.format(*args, **kwargs)` perform a string formatting operation
  - the string on which this method is called can contain **replacement fields** delimited by braces **`{}`**
  - returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument
- The `str.format()` method and the `Formatter` class share the same syntax for format strings
  - the [syntax](https://docs.python.org/3/library/string.html#format-string-syntax) is related to that of [formatted string literals](#formatted-string-literals), but there are differences
  - the grammar for a replacement field:
    - `replacement_field ::= "{" [field_name] ["!" conversion] [":" format_spec] "}"`
  - **`field_name`** itself begins with an **`arg_name`**
    - if it's a _number_, it refers to a _positional argument_
      - if the numerical `arg_name`s are 0, 1, 2, ... in sequence, they can all be omitted
      - `"{0}, {1}, {2}".format("a", "b", "c")`
      - `"{}, {}, {}".format("a", "b", "c")`
      - `"{0}{1}{0}".format("abra", "cad")`
      - `"{2}, {1}, {0}".format(*"abc")`
      - see `test_args_by_position()`
    - if it's a _keyword_, it refers to a _named keyword argument_
      - `"{lat}, {long}".format(lat="37.2N", long="-15.8W")`
      - `"{lat}, {long}".format(**coord)` (where `coord` is a `dict`)
      - `"{0[lat]}, {0[long]}".format(coord)`
      - see `test_args_by_name()`
    - positional and keyword arguments can be arbitrarily combined
      - `"{}, {other}, {}".format(1, 2, other=3)`
      - see `test_args_combined()`
    - because `arg_name` is not quote-delimited, it is not possible to specify arbitrary dictionary keys within a format string
    - `arg_name` can be followed by any number of index or attribute expressions
      - `"{0.real}, {0.imag}".format(3 - 5j)`
      - `"x: {0[0]}, y: {0[1]}".format((3, 4))`
      - see `test_arg_index_attrs()`
  - nested **`replacement_field`** example:
    - `"result: {0:{1}.{2}}".format(value, width, precision)`
    - see `test_format_nested_fields()`
  - **`conversion`** example:
    - `"The {animal!s}'s name is {name!r}".format(animal="eel", name="Bob")`
    - see `test_conversion_modifiers()`
  - **`format_spec`** examples:
    - `"pi is approx {pi:.3f}".format(pi=math.pi)`
    - `"{:.<10}{:.>10}".format(name + " ", " " + str(phone))`
    - `"{ts:%d %B %Y %H:%M:%S}".format(ts=timestamp)`

#### Manual String Formatting

- See [`manual_formatting_test.py`](src/ch07/manual_formatting_test.py)
- The [`str.rjust()`](https://docs.python.org/3/library/stdtypes.html#str.rjust) method of string objects right-justifies a string in a field of a given width by padding it with spaces (by default) on the left
  - see `test_rjust()`
- There are similar methods [`str.ljust()`](https://docs.python.org/3/library/stdtypes.html#str.ljust) and [`str.center()`](https://docs.python.org/3/library/stdtypes.html#str.center)
- These methods do not write anything, they just return a new string
- If the input string is too long, they don't truncate it, but return it unchanged
  - if you really want truncation you can always add a slice operation, as in `x.ljust(n)[:n]`
- [`str.zfill()`](https://docs.python.org/3/library/stdtypes.html#str.zfill) pads a numeric string on the left with zeros
  - it understands about plus and minus signs
  - see `test_zfill()`

#### Old String Formatting

- The `%` operator (modulo) can also be used for string formatting
- Given `'string' % values`, instances of `%` in string are replaced with zero or more elements of `values`
- Commonly known as string interpolation
- For example: `print('The value of pi is approximately %5.3f.' % math.pi)`
- See [printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)

### Reading and Writing Files

- [`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`](https://docs.python.org/3/library/functions.html#open)
  - returns a file object
    - the type of file object depends on the mode
      - e.g., in text mode, it returns a subclass of [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase) (specifically [`io.TextIOWrappper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper))
        - `io.TextIOBase` inherits [`io.IOBase`](https://docs.python.org/3/library/io.html#io.IOBase), which supports the _iterator protocol_, and is a _context manager_
          - `for line in file_object:`: iterates through the file object, line by line
        - see [I/O streams class hierarchy](https://docs.python.org/3/library/io.html#class-hierarchy)
  - most commonly used with two arguments: `open(file, mode)`
  - **`file`**
    - path-like object giving the pathname (absolute or relative) of the file to be opened or an integer file descriptor of the file to be wrapped
    - path-like object:
      - a `str` or `bytes` object representing a path
      - an object implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) protocol, e.g., [`pathlib.PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath)
  - **`mode`**
    - the mode in which the file is opened
      - `r`: open for reading (default)
      - `w`: open for writing, truncating the file first
      - `x`: open for exclusive creation, failing if the file already exists
      - `a`: open for writing, appending to the end of the file if it exists
      - `b`: binary mode
      - `t`: text mode (default)
      - `+`: open for updating (reading and writing)
    - default mode is `r` (synonym of `rt`)
    - `r+` and `r+b` open the file for reading and writing with no truncation
    - `w+` and `w+b` open the file for reading and writing with truncation
  - **`encoding`**
    - in _text_ mode, if `encoding` is not specified (`None`), the default is platform-dependent
  - **`newline`**
    - in _text_ mode, if `newline` is not specified (`None`), the default when
      - reading: convert platform-specific line endings to just `\n`
      - writing: convert `\n` to platform-specific line ending, `os.linesep`
  - see also the file handling modules, such as, [`fileinput`](https://docs.python.org/3/library/fileinput.html#module-fileinput), [`io`](https://docs.python.org/3/library/io.html#module-io), [`os`](https://docs.python.org/3/library/os.html#module-os), [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path), [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile), and [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil)
- It is good practice to use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword when dealing with file objects
  - the file is properly closed after its suite finishes, even if an exception is raised at some point
- If you're not using the `with` keyword, then you should call `f.close()` to close the file and immediately free up any system resources used by it

#### Methods of File Objects

- See [`file_object_methods_test.py`](src/ch07/file_object_methods_test.py)
- [`f.read(size)`](https://docs.python.org/3/library/io.html#io.TextIOBase.read)
  - reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode)
  - `size` is an optional numeric argument - the number of characters to read
    - when omitted or is negative, the entire contents of the file will be read and returned
      - see `test_read_all()`
  - if the end of the file has been reached, `f.read()` will return an empty string (`''`)
    - see `test_read_incremental()`
- [`f.readline()`](https://docs.python.org/3/library/io.html#io.TextIOBase.readline)
  - reads a single line from the file
  - a newline character (`\n`) is left at the end of the string
    - omitted on the last line of the file if the file doesn't end in a newline
    - if `f.readline()` returns an empty string, the end of the file has been reached
    - a blank line is represented by '`\n`', a string containing only a single newline
    - see `test_read_file_line()`
- For reading lines from a file, you can loop over the file object
- If you want to read all the lines of a file in a list you can also use `list(f)` or [`f.readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines)
  - see `test_read_file_to_list()`
- [`f.write(string)`](https://docs.python.org/3/library/io.html#io.TextIOBase.write) writes the contents of `string` to the file, returning the number of characters written
  - other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode)
  - see `test_write_file()`
- [`f.writelines(lines)`](https://docs.python.org/3/library/io.html#io.IOBase.writelines) writes a list of lines to the stream
  - line separators are not added, so it is usual for each of the lines provided to have a line separator at the end
  - see `test_write_lines()`

#### Saving structured data with json

- See [`json_read_write_test.py`](src/ch07/json_read_write_test.py)
- The standard module called [`json`](https://docs.python.org/3/library/json.html#module-json) can take Python data hierarchies, and convert them to string representations
- [`json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`](https://docs.python.org/3/library/json.html#json.dumps)
  - serialize `obj` to a JSON formatted `str`
  - `json.dumps([1, "simple", "list"])`
  - see `test_list_to_json_str()`, `test_python_to_json_str()`
- [`json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`](https://docs.python.org/3/library/json.html#json.dump)
  - serialize `obj` as a JSON formatted stream to `fp` (a `.write()`-supporting file-like object)
  - see `test_dict_to_json_file()`
- [`json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`](https://docs.python.org/3/library/json.html#json.loads)
  - deserialize `s` (a `str`, `bytes` or `bytearray` instance containing a JSON document) to a Python object
  - `json.loads('{"boolean": true, "null": null}')`
  - see `test_json_str_to_python_types()`
- [`json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`](https://docs.python.org/3/library/json.html#json.load)
  - deserialize `fp` (a `.read()`-supporting text file or binary file containing a JSON document) to a Python object
  - see `test_json_file_to_obj()`

## 8. Errors and Exceptions

- See [`errors_exceptions_test.py`](src/ch08/errors_exceptions_test.py)

### Exceptions

- See [class hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) for built-in exceptions

### Handling Exceptions

- A `try` statement may have more than one `except` clause, to specify handlers for different exceptions
  - see `test_multiple_handlers_hierarchy()`
- An `except` clause may name multiple exceptions as a parenthesized tuple
  - see `test_except_multiple_exceptions()`
- A class in an `except` clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around)
- The last `except` clause may omit the exception name(s), to serve as a wildcard
  - can be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well)
  - see `test_bare_except()`
- The `try ... except` statement has an optional **`else`** clause
  - must follow all `except` clauses
  - useful for code that must be executed if the `try` clause does not raise an exception or execute a `return`, `continue`, or `break` statement
  - see `test_try_except_else()`
- When an exception occurs, it may have an associated value, also known as the exception's argument
  - depends on the exception type
- The `except` clause may specify a variable after the exception name using the **`as`** keyword
  - bound to an exception instance with the arguments stored in [`.args`](https://docs.python.org/3/library/exceptions.html#BaseException.args)
  - exception instance defines `__str__()` so the arguments can be printed directly without having to reference `.args`
  - `except Exception as ex`
  - see `test_as_keyword()`

### Raising Exceptions

- The `raise` statement allows the programmer to force a specified exception to occur
- The sole argument to `raise` indicates the exception to be raised, which must be
  - an exception instance, or
  - an exception class (a class that derives from `Exception`)
    - implicitly instantiated by calling its constructor with no arguments
- If you need to determine whether an exception was raised but don't intend to handle it, a simpler form of the `raise` statement allows you to re-raise the exception
  - re-raises the last exception that was active in the current scope
  - if no exception is active in the current scope, a `RuntimeError` exception is raised
- The **`from`** clause is used for _exception chaining_
  - if given, the second expression must be another exception class or instance
    - attached to the raised exception as the `__cause__` attribute (which is writable)
  - `raise RuntimeError("Something bad happened") from zde`
  - see `test_exception_chaining()`

### User-defined Exceptions

- Programs may name their own exceptions by creating a new exception class
  - should typically be derived from the `Exception` class, either directly or indirectly
- When creating a module that can raise several distinct errors, a common practice is to create a base class for exceptions defined by that module
  - subclass that to create specific exception classes for different error conditions
- Most exceptions are defined with names that end in "Error", similar to the naming of the standard exceptions
- see `test_custom_exception()`

### Defining Clean-up Actions

- If a `finally` clause is present, it will be executed as the last task before the `try` statement completes
  - runs whether or not the `try` statement produces an exception
  - if an exception occurs during execution of the `try` clause, and it is not handled by an `except` clause
    - the exception is re-raised after the `finally` clause has been executed
  - an exception could occur during execution of an `except` or `else` clause
    - the exception is re-raised after the `finally` clause has been executed
  - if the `try` statement reaches a `break`, `continue` or `return` statement
    - the `finally` clause will execute just prior to their execution
  - if a `finally` clause includes a `return` statement
    - the returned value will be the one from the `finally` clause, not the value from the `try` clause's `return` statement
  - see `test_finally()`
- The `finally` clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful

## 9. Classes

- Python's class mechanism is a mixture of the class mechanisms found in C++ and Modula-3
- In C++ terminology, normally class members (including the data members) are _public_, and all member functions are _virtual_ (can be overridden by derived classes)
- As in Smalltalk, classes themselves are objects
- Unlike C++ and Modula-3, built-in types can be used as base classes for extension by the user
- Like in C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for class instances

### A Word About Names and Objects

- Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object
  - known as _aliasing_
- Aliasing has an effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types
  - behave like pointers in some respects
  - passing an object is cheap since only a pointer is passed by the implementation
  - if a function modifies an object passed as an argument, the caller will see the change

### Python Scopes and Namespaces

- A **namespace** is a mapping from names to objects
  - most namespaces are currently implemented as Python dictionaries
  - examples of namespaces are:
    - the set of built-in names (containing functions such as `abs()`, and built-in exception names)
    - the global names in a module
    - the local names in a function invocation
    - (in a sense) the set of attributes of an object
  - there is absolutely no relation between names in different namespaces
    - 2 different modules may both define a function `maximize` - users of the modules must prefix it with the module name
- **Attribute** - any name following a dot
  - `z.real`: `real` is an attribute of the object `z`
  - references to names in modules are attribute references
    - `modname.funcname`: `modname` is a module object and `funcname` is an attribute of it
    - straightforward mapping between the module's attributes and the global names defined in the module: they share the same namespace
  - may be read-only or writable
    - module attributes are writable
      - `modname.the_answer = 42`
    - writable attributes may also be deleted with the `del` statement
      - `del modname.the_answer`: remove the attribute `the_answer` from the object named by `modname`
- Namespaces are created at different moments and have different lifetimes
  - namespace containing the built-in names
    - created when the Python interpreter starts up
    - never deleted
    - built-in names actually also live in a module called `builtins`
  - global namespace for a module
    - created when the module definition is read in
    - normally, module namespaces also last until the interpreter quits
  - statements executed by the top-level invocation of the interpreter
    - considered part of a module called `__main__`
    - have their own global namespace
  - local namespace for a function
    - created when the function is called
    - deleted (forgotten) when the function returns or raises an exception that is not handled within the function
    - recursive invocations each have their own local namespace
- A **scope** is a textual region of a Python program where a namespace is directly accessible (unqualified reference to a name to find the name in the namespace)
  - scopes are determined statically, they are used dynamically
  - at any time during execution, there are at least 3 nested scopes whose namespaces are directly accessible:
    - innermost scope: searched first, contains the local names
    - scopes of any enclosing functions: searched starting with the nearest enclosing scope, contains non-local, but also non-global names
    - next-to-last scope: contains the current module's global names
    - outermost scope: searched last, the namespace containing built-in names
  - if a name is declared global
    - all references and assignments go directly to the middle scope containing the module's global names
  - to rebind variables found outside of the innermost scope, the `nonlocal` statement can be used
    - if not declared `nonlocal`
      - those variables are read-only
      - an attempt to write to such a variable will simply create a new local variable in the innermost scope, leaving the identically named outer variable unchanged
  - the local scope references the local names of the (textually) current function
  - outside functions, the local scope references the same namespace as the global scope: the module's namespace
  - class definitions place yet another namespace in the local scope
  - scopes are determined textually: the global scope of a function defined in a module is that module's namespace, no matter from where or by what alias the function is called
  - if no `global` or `nonlocal` statement is in effect
    - assignments to names always go into the innermost scope
  - assignments do not copy data - they just bind names to objects
    - the same is true for deletions: `del x` removes the binding of `x` from the namespace referenced by the local scope
  - all operations that introduce new names use the local scope
    - `import` statements and function definitions bind the module or function name in the local scope
  - `global` statement
    - indicates that particular variables live in the global scope and should be rebound there
  - `nonlocal` statement
    - indicates that particular variables live in an enclosing scope and should be rebound there

### A First Look at Classes

#### Class Definition Syntax

- In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed
- When a class definition is entered, a new namespace is created, and used as the local scope
  - all assignments to local variables go into this new namespace
  - function definitions bind the name of the new function here
- When a class definition is left normally (via the end)
  - a **class object** is created
    - a wrapper around the contents of the namespace created by the class definition
  - the original local scope (the one in effect just before the class definition was entered) is reinstated
  - the class object is bound here to the class name given in the class definition header

#### Class Objects

- Class objects support two kinds of operations: attribute references and instantiation
- **Attribute references** use the standard syntax used for all attribute references in Python: `obj.name`
  - valid attribute names are all the names that were in the class's namespace when the class object was created
  - with the class definition below:
    - `MyClass.i` and `MyClass.f` are valid attribute references, returning an integer and a _function object_, respectively
    - class attributes can be assigned to, so you can change the value of `MyClass.i` by assignment
    - `__doc__` is also a valid attribute, returning the docstring belonging to the class: `"A simple example class."`

```python
class MyClass:
    """A simple example class."""
    i = 12345

    def f(self):
        return 'hello world'
```

- **Class instantiation** uses function notation
  - `x = MyClass()` creates a new instance of the class and assigns this object to the local variable `x`
  - a class may define a special method named `__init__()` to customize an instance to a specific initial state
    - automatically invoked during class instantiation

#### Instance Objects

- See [`a_first_look_test.py`](src/ch09/a_first_look_test.py)
- The only operations understood by instance objects are _attribute references_
- There are 2 kinds of valid attribute names:
  - data attributes
  - methods
- **Data attributes** need not be declared
  - like local variables, they spring into existence when they are first assigned to
  - see `test_data_attribute()`
- The other kind of instance attribute reference is a **method**
  - a method is a function that "belongs to" an object
  - by definition, all attributes of a class that are function objects define corresponding methods of its instances
  - in the `MyClass` example above:
    - `x.f` is a method reference since `MyClass.f` is a function
    - `x.f` is not the same thing as `MyClass.f` - it is a _method object_, not a function object

#### Method Objects

- See [`a_first_look_test.py`](src/ch09/a_first_look_test.py)
- In the `MyClass` example above, `x.f` is a _method object_
  - it can be stored away and called at a later time
  - the special thing about methods is that the instance object is passed as the first argument of the function (`self`)
    - the call `x.f()` is exactly equivalent to `MyClass.f(x)`
  - see `test_method_object()`

#### Class and Instance Variables

- See [`a_first_look_test.py`](src/ch09/a_first_look_test.py)
- **Instance variables** are for data unique to each instance
- **Class variables** are for attributes and methods shared by all instances of the class
  - shared data can have surprising effects when involving mutable objects such as lists and dictionaries
- For example, the `tricks` list in the following code should not be used as a class variable because just a single list would be shared by all `Dog` instances

```python
class Dog:

    shared_tricks: List[str] = []  # Mistaken use of a class variable
    ...
```

- Correct design of the class should use an instance variable
  - see `test_class_instance_variables()`

```python
class Dog:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tricks: List[str] = []
```

### Random Remarks

- See [`a_first_look_test.py`](src/ch09/a_first_look_test.py)
- Data attributes may be referenced by methods as well as by ordinary users ("clients") of an object
  - in fact, nothing in Python makes it possible to enforce data hiding - it is all based upon convention
- Clients should use data attributes with care
  - clients may mess up invariants maintained by the methods by stamping on their data attributes
  - clients may add data attributes of their own to an instance object without affecting the validity of the methods
    - as long as name conflicts are avoided
- Often, the first argument of a method is called `self`
  - this is nothing more than a convention
- Any function object that is a class attribute defines a method for instances of that class
  - it is not necessary that the function definition is textually enclosed in the class definition
  - assigning a function object to a local variable in the class is also ok
  - see `test_add_function_to_class()`
- Methods may call other methods by using method attributes of the self argument
  - see `test_calling_other_methods()`
- Each value is an object, and therefore has a class (also called its type)
  - stored as `object.__class__`

### Inheritance

- See [`inheritance_test.py`](src/ch09/inheritance_test.py)
- The syntax for a derived class definition looks like this:

```python
class DerivedClassName(BaseClassName):
    # <statement-1>
    # .
    # .
    # <statement-N>
```

- The name `BaseClassName` must be defined in a scope containing the derived class definition
- In place of a base class name, other arbitrary expressions are also allowed
  - useful, for example, when the base class is defined in another module
    - `class DerivedClassName(modname.BaseClassName):`
- When the class object is constructed, the base class is remembered
  - used for resolving attribute references
  - if a requested attribute is not found in the class, the search proceeds to look in the base class
- `DerivedClassName()` creates a new instance of the class
- If a base class has an `__init__()` method
  - the derived class's `__init__()` method, if any, must explicitly call it to ensure proper initialization of the base class part of the instance
    - `BaseClassName.__init__(self, arguments)`
    - `super().__init__(arguments)`
- Method references are resolved as follows:
  - the corresponding class attribute is searched, descending down the chain of base classes if necessary
- Derived classes may override methods of their base classes
  - methods have no special privileges when calling other methods of the same object
    - a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it
- An overriding method in a derived class may want to extend rather than simply replace the base class method of the same name
  - to call the base class method directly:
    - `BaseClassName.methodname(self, arguments)`
    - `super().methodname(arguments)`
- Python has two built-in functions that work with inheritance:
  - `isinstance()`
    - check an instance's type
    - `isinstance(obj, int)` will be `True` only if `obj.__class__` is `int` or some class derived from `int`
    - see `test_isinstance()`
  - `issubclass()`
    - check class inheritance
    - `issubclass(bool, int)` is `True` since `bool` is a subclass of `int`
    - `issubclass(float, int)` is `False` since `float` is not a subclass of `int`
    - see `test_issubclass()`

#### Multiple Inheritance

- See [`multiple_inheritance_test.py`](src/ch09/multiple_inheritance_test.py)
- A class definition with multiple base classes looks like this:

```python
class DerivedClassName(Base1, Base2, Base3):
    # <statement-1>
    # .
    # .
    # <statement-N>
```

- In the simplest cases, you can think of the search for attributes inherited from a parent class as
  - depth-first
  - left-to-right
  - not searching twice in the same class where there is an overlap in the hierarchy
- In fact, it is slightly more complex than that
  - method resolution order (mro) changes dynamically to support cooperative calls to `super()`
  - known in some other multiple-inheritance languages as call-next-method
  - see <https://www.python.org/download/releases/2.3/mro/>
  - given a class `C` in a complicated multiple inheritance hierarchy
    - the list of the ancestors of a class `C`, including the class itself, ordered from the nearest ancestor to the furthest, is called the class precedence list or the **linearization** of `C`
    - **Method Resolution Order (MRO)** is the set of rules that construct the linearization
      - in the Python literature, "the MRO of `C`" is synonymous to the linearization of the class `C`
    - in the case of single inheritance hierarchy, if `C` is a subclass of `C1`, and `C1` is a subclass of `C2`, then the linearization of `C` is simply the list `[C, C1 , C2]`
    - with multiple inheritance hierarchies, the construction of the linearization is more cumbersome, since it is more difficult to construct a linearization that respects local precedence ordering and monotonicity
    - an MRO is **monotonic** when the following is true:
      - if `C1` precedes `C2` in the linearization of `C`, then `C1` precedes `C2` in the linearization of any subclass of `C`
    - **`class.__mro__`**: a tuple of classes that are considered when looking for base classes during method resolution

#### Mixins

- See [`mixin_test.py`](src/ch09/mixin_test.py)
- Python doesn't provide support for mixins with any dedicated language feature, so we use multiple inheritance to implement them
  - classes that live in the normal inheritance tree, but are kept small
  - the delineation between using true inheritance and using mixins is nuanced
    - a mixin is independent enough that it doesn't feel the same as a parent class
    - mixins aren't generally used on their own, but aren't abstract classes either
  - shouldn't have common ancestors other than `object` with the other parent classes
- Mixins cannot usually be too generic
  - designed to add features to classes, but these new features often interact with other pre-existing features of the augmented class
- See:
  - <https://www.thedigitalcatonline.com/blog/2020/03/27/mixin-classes-in-python/>
  - <https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556>

### Private Variables

- See [`private_variables_test.py`](src/ch09/private_variables_test.py)
- "Private" instance variables that cannot be accessed except from inside an object don't exist in Python
- Convention: a name (function, method or data member)) **prefixed with an underscore** (e.g., `_spam`) should be treated as a non-public part of the API
  - should be considered an implementation detail and subject to change without notice
- There is limited support for class-private members, called **name mangling**
  - any identifier of the form `__spam` (at least 2 leading underscores, at most 1 trailing underscore) is textually replaced with `_classname__spam`
    - `classname` is the current class name
  - helpful for letting subclasses override methods without breaking intraclass method calls

### Odds and Ends

- See [`odds_ends_test.py`](src/ch09/odds_ends_test.py)
- **Struct**
  - an empty class definition can be used as a data type similar to the Pascal "record" or C "struct", bundling together a few named data items
  - see `test_struct()`
- **Duck typing/structural subtyping**
  - a piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead
  - see `test_structural_subtyping()`
- **Property**
  - `class property(fget=None, fset=None, fdel=None, doc=None)`
    - return a property attribute
    - `fget`: a function for getting an attribute value
    - `fset`: a function for setting an attribute value
    - `fdel`: a function for deleting an attribute value
    - `doc`: creates a docstring for the attribute
  - a typical use is to define a managed attribute
  - see `test_property()` and `test_read_only_property()`
  - see also <https://docs.python.org/3/library/functions.html#property>
  - using `property()` as a decorator
    - the `@property` decorator turns the decorated method into a "getter" for an attribute with the same name
    - a property object has `getter`, `setter`, and `deleter` methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function
    - see `test_property_decorator()`

### Iterators

- See [`iterators_test.py`](src/ch09/iterators_test.py)
- The `for` statement calls [**`iter()`**](https://docs.python.org/3/library/functions.html#iter) on the container object
  - `for element in [1, 2, 3]:`
  - returns an **iterator object**
    - defines the method `__next__()` which accesses elements in the container one at a time
    - defines the method `__iter__()` which return the iterator object itself
      - required to allow both containers and iterators to be used with the `for` and `in` statements
    - the 2 methods together form the _iterator protocol_
  - when there are no more elements, `__next__()` raises a `StopIteration` exception which tells the `for` loop to terminate
  - you can call the `__next__()` method using the `next()` built-in function
    - `next(letters_iter)`
- To add iterator behavior to your classes
  - define an `__iter__()` method which returns an object with a `__next__()` method (supports the iterator protocol)
  - if the class defines `__next__()`, then `__iter__()` can just return `self`
- See also:
  - <https://mypy.readthedocs.io/en/stable/protocols.html#iterator-t>
  - <https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes>

### Generators

- See [`generators_test.py`](src/ch09/generators_test.py)
- A generator is a function which returns a **generator iterator**
- It is written like a regular function but uses the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) statement whenever they want to return data
- When a generator function is called
  - returns an iterator known as a generator
  - that generator then controls the execution of the generator function
  - execution starts when one of the generator's `next()` or `send()` methods is called
  - execution proceeds to the first `yield` expression, where it is suspended again
    - returning the value of the `yield` expression to the generator's caller
    - all local state is retained
  - when the execution is resumed by calling one of the generator's `next()` or `send()` methods
    - the function can proceed exactly as if the `yield` expression were just another external call
    - the value of the `yield` expression after resuming depends on the method which resumed the execution
      - if `__next__()` is used (typically via either a `for` or the `next()` builtin) then the result is `None`
      - if `send()` is used, then the result will be the value passed in to that method
  - when the generator terminates, it automatically raises `StopIteration`
- Anything that can be done with generators can also be done with class-based iterators as described in the previous section
- What makes generators so compact is that the `__iter__()` and `__next__()` methods are created automatically
- Another key feature is that the local variables and execution state are automatically saved between calls
  - easier to write and much clearer than an approach using instance variables like `self.index` and `self.data`
- These features make it easy to create iterators with no more effort than writing a regular function
- A generator can be annotated by the generic type `Generator[YieldType, SendType, ReturnType]`
- Examples uses:
  - reading large files
  - generating an infinite sequence
- See also:
  - <https://docs.python.org/3/reference/expressions.html#generator-iterator-methods>
  - <https://realpython.com/introduction-to-python-generators/>

### Generator Expressions

- See [`generators_test.py`](src/ch09/generators_test.py)
- Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets
- Designed for situations where the generator is used right away by an enclosing function
- More compact but less versatile than full generator definitions
- Tend to be more memory friendly than equivalent list comprehensions
- Examples:
  - `(data[i] for i in range(len(data) - 1, -1, -1))`
  - `(i * i for i in range(10))`
  - `(words for line in file for words in line.split())`

## 10. Brief Tour of the Standard Library

### Operating System Interface

- See [`os_test.py`](src/ch10/os_test.py)
- The [`os`](https://docs.python.org/3/library/os.html#module-os) module provides dozens of functions for interacting with the operating system
  - use the `import os` style instead of `from os import *` to prevent `os.open()` from shadowing the built-in `open()` function
- For file and directory management tasks, the [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil) module provides a higher level interface that is easier to use
  - see also [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path) and [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib) modules

### File Wildcards

- See [`os_test.py`](src/ch10/os_test.py)
- The [`glob`](https://docs.python.org/3/library/glob.html#module-glob) module provides a function for making file lists from directory wildcard searches
  - `glob.glob(str(tmp_path.joinpath("**/*.txt")), recursive=True)`
- See also [`Path.glob(pattern)`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob)
  - `tmp_path.glob("**/*.txt")`

### Command Line Arguments

- Command line arguments are stored in the [**`sys`**](https://docs.python.org/3/library/sys.html#module-sys) module's `argv` attribute as a list
  - see [`cmd_line_args.py`](src/ch10/cmd_line_args.py)

```console
$ python cmd_line_args.py one two three
['cmd_line_args.py', 'one', 'two', 'three']
```

- The [**`argparse`**](https://docs.python.org/3/library/argparse.html#module-argparse) module provides a more sophisticated mechanism to process command line arguments
  - see [`top_lines.py`](src/ch10/top_lines.py)
  - see also <https://docs.python.org/3/howto/argparse.html#argparse-tutorial>

```console
$ python top_lines.py
usage: top_lines [-h] [-l LINES] filenames [filenames ...]
top: error: the following arguments are required: filenames

$ python top_lines.py -h
usage: top_lines [-h] [-l LINES] filenames [filenames ...]

Show top lines from each file

positional arguments:
  filenames

optional arguments:
  -h, --help            show this help message and exit
  -l LINES, --lines LINES

$ python top_lines.py -l 5 a.txt b.txt
Namespace(filenames=['a.txt', 'b.txt'], lines=5)
```

### Error Output Redirection and Program Termination

- The [**`sys`**](https://docs.python.org/3/library/sys.html#module-sys) module also has attributes for standard input, output and errors (`stdin`, `stdout` and `stderr`)
  - `stderr` is useful for emitting warnings and error messages to make them visible even when standard out has been redirected
  - see [`sys_stdout_stderr_test.py`](src/ch10/sys_stdout_stderr_test.py)
- The most direct way to terminate a script is to use `sys.exit()`

### String Pattern Matching

- See [`string_pattern_matching_test.py`](src/ch10/string_pattern_matching_test.py)
- The [**`re`**](https://docs.python.org/3/library/re.html#module-re) module provides regular expression tools for advanced string processing
- Compiling regular expressions
  - regular expressions are compiled into [**`Pattern` objects**](https://docs.python.org/3/library/re.html#regular-expression-objects)
  - `re.compile()` also accepts an optional flags argument, used to enable various special features and syntax variations
    - see <https://docs.python.org/3/howto/regex.html#compilation-flags>
- Performing matches
  - pattern objects have several methods and attributes, such as:
    - `search()`: scan through a string, looking for any location where this RE matches
      - see `test_pattern_search()`
    - `match()`: determine if the RE matches at the beginning of the string
      - see `test_pattern_match()`
    - `findall()`: find all substrings where the RE matches, and returns them as a list
    - `finditer()`: find all substrings where the RE matches, and returns them as an iterator
      - see `test_pattern_findall_iter()`
  - `match()` and `search()` return `None` if no match can be found
    - if they're successful, a [**`Match` object**](https://docs.python.org/3/library/re.html#match-objects) is returned
  - `Match` objects have methods and attributes such as:
    - `group()`: return the string matched by the RE
    - `start()`: return the starting position of the match
    - `end()`: return the ending position of the match
    - `span()`: return a tuple containing the (start, end) positions of the match
- Module-level functions
  - the `re` module also provides top-level functions called `match()`, `search()`, `findall()`, `finditer()`, and so forth
    - they take the same arguments as the corresponding `Pattern` method with the RE string added as the first argument
      - `re.search(r"\bclass\b", "no class at all")`
    - these functions simply create a pattern object for you and call the appropriate method on it
    - they also store the compiled object in a cache
      - if you're accessing a regex within a loop, pre-compiling it will save a few function calls
      - outside of loops, there's not much difference
    - see `test_module_functions()`
- Grouping
  - marked by the `(`, `)` metacharacters
  - numbered starting with 0
    - group 0 is always present; it's the whole RE
  - subgroups are numbered from left to right, from 1 upward
  - can be nested; to determine the number, just count the opening parenthesis characters, going from left to right
  - see `test_group_numbering()`
  - **backreferences** in a pattern allow you to specify that the contents of an earlier capturing group must also be found at the current location in the string
    - e.g., `\1` will succeed if the exact contents of group 1 can be found at the current position
      - `re.search(r"\b(\w+)\s+\1\b", "Paris in the the spring")`
    - see `test_backreference()`
- Named groups
  - the syntax for a named group is one of the Python-specific extensions: `(?P<name>...)`
  - behave exactly like capturing groups, and additionally associate a name with a group
    - `re.match(r"(?P<first>\w+) (?:[A-Z]\. )?(?P<last>\w+)", "Jane P. Doe")`
  - you can retrieve named groups by number or string, or as a dictionary with `groupdict()`
    - see `test_named_group()`
- Lookaround assertions
  - lookahead and lookbehind, collectively called "lookaround", are zero-length assertions
  - matches characters, but then gives up the match, returning only the result: match or no match
    - succeeds if the contained regular expression successfully matches (for a positive lookaround) or doesn't match (for a negative lookaround) at the current location, and fails otherwise
    - once the contained expression has been tried, the matching engine doesn't advance at all
      - the rest of the pattern is tried right where the assertion started
  - positive lookahead
    - `re.compile(r"\w+(?= Brown$)")`
    - see `test_positive_lookahead()`
  - negative lookahead
    - `re.compile(r".*[.](?!bat$|exe$)[^.]*$")`
    - see `test_negative_lookahead()`
  - positive lookbehind
    - `re.compile(r"(?<=-)\w+")`
    - see `test_positive_lookbehind()`
  - negative lookbehind
    - `re.compile(r"(?<!abc|bbc)def")`
    - see `test_negative_lookbehind()`
- Search and replace
  - `re.sub(pattern, repl, string, count=0, flags=0)`
  - return the string obtained by replacing the leftmost non-overlapping occurrences of `pattern` in `string` by the replacement `repl`
    - `pattern` may be a string or a pattern object
      - `re.sub(r"blue|white|red", "color", "blue socks and red shoes")`
      - see `test_sub()`
    - if the pattern isn't found, `string` is returned unchanged
    - `repl` can be a string or a function
      - replacement function: see `test_replacement_function()`
      - backreferences, such as `\6`, are replaced with the substring matched by group 6 in the pattern
        - `re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")`
        - see `test_group_backreference()`
      - `\g<number>` uses the corresponding group number
        - `\g<2>` is equivalent to `\2`
        - prevents ambiguity with, e.g., `\g<2>0`, which is a reference to group 2 followed by the literal `0` character
        - `re.sub("section{([^}]*)}", r"heading{\g<1>}", "section{One} section{Two}")`
      - named groups: `\g<name>` will use the substring matched by the group named `name`, as defined by `(?P<name>...)`
        - `re.sub("section{(?P<name>[^}]*)}", r"heading{\g<name>}", "section{One} section{Two}")`
        - see `test_backreference_variants()`
    - `count` is the maximum number of pattern occurrences to be replaced
      - if omitted or zero, all occurrences will be replaced
    - empty matches for the pattern are replaced only when not adjacent to a previous empty match
  - see also <https://docs.python.org/3/howto/regex.html>

### Mathematics

- See [`mathematics_test.py`](src/ch10/mathematics_test.py)
- The [`math`](https://docs.python.org/3/library/math.html#module-math) module gives access to the underlying C library functions for floating point math
- The [`random`](https://docs.python.org/3/library/random.html#module-random) module provides tools for making random selections
- The [`statistics`](https://docs.python.org/3/library/statistics.html#module-statistics) module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data
- The [SciPy project](https://scipy.org) has many other modules for numerical computations

### Internet Access

- See [`internet_access_test.py`](src/ch10/internet_access_test.py)
- There are a number of modules for accessing the internet and processing internet protocols
- Two of the simplest are:
  - [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for retrieving data from URLs
    - `urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)`
      - opens the URL `url`, which can be either a string or a `Request` object (see below)
      - `data` must be an object specifying additional data to be sent to the server, or `None` if no such data is needed (see `Request` for details)
      - the optional `timeout` parameter specifies a timeout in seconds for blocking operations like the connection attempt
        - if not specified, the global default timeout setting will be used
        - only works for HTTP, HTTPS and FTP connections
      - if `context` is specified, it must be an `ssl.SSLContext` instance describing the various SSL options
        - see [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection) for more details
      - the optional `cafile` and `capath` parameters specify a set of trusted CA certificates for HTTPS requests
        - more information: [`ssl.SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations)
      - the `cadefault` parameter is ignored
      - always returns an object which can work as a context manager and has methods such as:
        - `geturl()`: return the URL of the resource retrieved
        - `info()`: return the meta-information of the page, such as headers
        - `getcode()`: return the HTTP status code of the response
      - for HTTP and HTTPS URLs, this function returns a [`http.client.HTTPResponse`](https://docs.python.org/3/library/http.client.html#httpresponse-objects) object _slightly modified_
        - an _iterable_ object, and a _context manager_
      - raises `URLError` on protocol errors
      - if proxy settings are detected (for example, when a `*_proxy` environment variable like `http_proxy` is set), `ProxyHandler` is default installed and makes sure the requests are handled through the proxy
    - `class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)`
      - an abstraction of a URL request
      - `url` should be a string containing a valid URL
      - `data` must be an object specifying additional data to send to the server, or `None` if no such data is needed
        - currently HTTP requests are the only ones that use data
        - supported object types include bytes, file-like objects, and iterables of bytes-like objects
        - if neither Content-Length nor Transfer-Encoding header field has been provided, `HTTPHandler` will set these headers according to the type of data
        - for an HTTP POST request method, data should be a buffer in the standard _application/x-www-form-urlencoded_ format
          - `urllib.parse.urlencode()` function takes a mapping or sequence of 2-tuples and returns an ASCII string in this format
          - should be encoded to bytes before being used as the `data` parameter
        - `headers` should be a dictionary, and will be treated as if [`add_header()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header) was called with each key and value as arguments
        - an appropriate `Content-Type` header should be included if the `data` argument is present
          - if this header has not been provided and `data` is not `None`, `Content-Type: application/x-www-form-urlencoded` will be added as a default
      - the next two arguments are only of interest for correct handling of third-party HTTP cookies:
        - `origin_req_host` should be the request-host of the origin transaction, as defined by RFC 2965
        - `unverifiable` should indicate whether the request is unverifiable, as defined by RFC 2965
      - `method` should be a string that indicates the HTTP request method that will be used (e.g. 'HEAD')
        - the default is `'GET'` if `data` is `None`, or `'POST'` otherwise
      - note: the request will not work as expected if the data object is unable to deliver its content more than once (e.g. a file or an iterable that can produce the content only once) and the request is retried for HTTP redirects or authentication
  - [`smtplib`](https://docs.python.org/3/library/smtplib.html#module-smtplib) for sending mail
- The [Requests package](https://requests.readthedocs.io/en/master/) is recommended for a higher-level HTTP client interface
  - [`requests.request(method, url, **kwargs)`](https://requests.readthedocs.io/en/stable/api/#requests.request)
    - constructs and sends a `Request`
    - returns a [`requests.Response`](https://requests.readthedocs.io/en/stable/api/#requests.Response) object
  - [`requests.get(url, params=None, **kwargs)`](https://requests.readthedocs.io/en/stable/api/#requests.get)
    - sends a GET request
  - [`requests.Response.iter_lines(chunk_size=512, decode_unicode=False, delimiter=None)`](https://requests.readthedocs.io/en/stable/api/#requests.Response.iter_lines)
    - iterates over the response data, one line at a time
    - when `stream=True` is set on the request, this avoids reading the content at once into memory for large responses
    - if `decode_unicode=True`, content will be decoded using the best available encoding based on the response
  - [`requests.Response.content`](https://requests.readthedocs.io/en/stable/api/#requests.Response.content)
    - content of the response, in bytes
  - see also:
    - <https://requests.readthedocs.io/en/stable/user/quickstart/>
    - <https://requests.readthedocs.io/en/stable/user/advanced/>
    - <https://requests.readthedocs.io/en/stable/api/>

### Dates and Times

- See [`datetime_test.py`](src/ch10/datetime_test.py)
- The [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime) module supplies classes for manipulating dates and times
- While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation

#### Aware and Naive Objects

- Date and time objects may be categorized as "aware" or "naive" depending on whether or not they include timezone information
- An **aware** object can locate itself relative to other aware objects
  - represents a specific moment in time that is not open to interpretation
- A **naive** object does not contain enough information to unambiguously locate itself relative to other date/time objects
  - whether a naive object represents Coordinated Universal Time (UTC), local time, or time in some other timezone is purely up to the program, just like it is up to the program whether a particular number represents metres, miles, or mass
- For applications requiring aware objects, `datetime` and `time` objects have an optional time zone information attribute, [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo)
  - can be set to an instance of a subclass of the abstract `tzinfo` class
  - only one concrete `tzinfo` class, the [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone) class, is supplied by the `datetime` module
  - see also: <http://pytz.sourceforge.net/>

#### Determining if an Object is Aware or Naive

- Objects of the `date` type are always naive
- An object of type `time` or `datetime` may be aware or naive
  - a `datetime` object `d` is aware if both of the following hold:
    - `d.tzinfo` is not `None`
    - `d.tzinfo.utcoffset(d)` does not return `None`
  - a `time` object `t` is aware if both of the following hold:
    - `t.tzinfo` is not `None`
    - `t.tzinfo.utcoffset(None)` does not return `None`
- The distinction between aware and naive doesn't apply to `timedelta` objects

#### Common Properties

- The `date`, `datetime`, `time`, and `timezone` types share these common features:
  - objects of these types are immutable
  - objects of these types are hashable, meaning that they can be used as dictionary keys
  - objects of these types support efficient pickling via the `pickle` module

#### [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) Objects

- Represents a duration, the difference between two dates or times
- `class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`
  - only `days`, `seconds` and `microseconds` are stored internally
  - all other arguments are merged and converted (normalized) to those units
  - `repr(timedelta(hours=24, minutes=10)) == "datetime.timedelta(days=1, seconds=600)"`
  - see `test_timedelta_str_repr()` and `test_timedelta_normalization()`
- `timedelta` arithmetic
  - `ten_mins = timedelta(minutes=10)`
  - `ten_mins * 6 == timedelta(hours=1)`
  - `ten_mins - timedelta(seconds=60) == timedelta(minutes=9)`
  - `ten_mins / timedelta(minutes=5) == 2.0`
  - see `test_timedelta_arithmetic()`

#### [`date`](https://docs.python.org/3/library/datetime.html#datetime.date) Objects

- Represents a date (year, month and day) in an idealized calendar
- `class datetime.date(year, month, day)`
  - all arguments are required
- Some class methods:
  - `date.today()`
    - return the current local date
  - `date.fromisoformat(date_string)`
    - return a date corresponding to a `date_string` given in the format `YYYY-MM-DD`
    - `date.fromisoformat("2020-07-01") == date(2020, 7, 1)`
  - see `test_date_class_methods()`
- Some instance methods:
  - `date.replace(year=self.year, month=self.month, day=self.day)`
    - return a date with the same value, except for those parameters given new values
  - `date.weekday()`
    - return the day of the week as an integer, where Monday is 0 and Sunday is 6
  - `date.isoformat()`
    - return a string representing the date in ISO 8601 format, `YYYY-MM-DD`
  - `date.__str__()`
    - for a date `d`, `str(d)` is equivalent to `d.isoformat()`
  - see `test_date_instance_methods()`
- Some operations:
  - `some_date = date(2020, 7, 15)`
  - `some_date + timedelta(hours=24) == date(2020, 7, 16)`
  - `some_date + timedelta(hours=13) == date(2020, 7, 15)`
  - `some_date - date(2020, 7, 10) == timedelta(days=5)`
  - `some_date < date(2020, 7, 16)`
  - see `test_date_operations()`

#### [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) Objects

- A single object containing all the information from a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date) object and a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time) object
- `class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)`
  - `year`, `month` and `day` arguments are required
  - `tzinfo` may be `None`, or an instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo) subclass
- Some class methods:
  - `datetime.now(tz=None)`
    - returns the current local date and time
    - if optional argument `tz` is `None` or not specified, this is like `today()`
    - if `tz` is not `None`, it must be an instance of a `tzinfo` subclass, and the current date and time are converted to `tz`'s time zone
    - preferred over [`today()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.today) and [`utcnow()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow) (by calling `datetime.now(timezone.utc)`)
  - `datetime.fromisoformat(date_string)`
    - returns a `datetime` corresponding to a `date_string` in one of the formats emitted by `date.isoformat()` and `datetime.isoformat()`
      - `YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]`, where `*` can match any single character
    - does not support parsing arbitrary ISO 8601 strings
      - a more full-featured ISO 8601 parser, `dateutil.parser.isoparse` is available in the third-party package [`dateutil`](https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.isoparse)
    - `datetime.fromisoformat("2011-11-04T00:05:23+01:00") == datetime(2011, 11, 4, 0, 5, 23, tzinfo=timezone(timedelta(seconds=3600)))`
  - see `test_datetime_class_methods()`
- Some instance methods:
  - `datetime.astimezone(tz=None)`
    - returns a `datetime` object with new `tzinfo` attribute `tz`, adjusting the date and time data so the result is the same UTC time as `self`, but in `tz`'s local time
    - if called without arguments (or with `tz=None`) the system local timezone is assumed for the target timezone
      - the `.tzinfo` attribute of the converted `datetime` instance will be set to an instance of timezone with the zone name and offset obtained from the OS
    - `some_datetime.astimezone(timezone(timedelta(hours=1), "BST"))`
  - `datetime.timetuple()`
    - returns a [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time), a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple), such as returned by `time.localtime()`
    - is equivalent to:
      - `time.struct_time((d.year, d.month, d.day, d.hour, d.minute, d.second, d.weekday(), yday, dst))`
      - where
        - `yday`: `d.toordinal() - date(d.year, 1, 1).toordinal() + 1`, i.e., the day number within the current year starting with 1 for January 1st
        - `dst`: set according to the [`dst()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.dst) method
          - `-1`: `dst()` returns `None`
          - `1`: `dst()` returns a non-zero value
          - `0`: `dst()` returns zero
  - `datetime.toordinal()`
    - return the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1
  - `datetime.timestamp()`
    - returns POSIX timestamp corresponding to the `datetime` instance
    - a `float` similar to that returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time)
  - `datetime.isoformat(sep='T', timespec='auto')`
    - returns a string representing the date and time in ISO 8601 format:
      - `YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]`, if microsecond is not 0
      - `YYYY-MM-DDTHH:MM:SS+HH:MM[:SS[.ffffff]]`, if microsecond is 0
      - the UTC offset is omitted if `utcoffset()` returns `None`
    - `some_datetime.isoformat() == "2020-07-15T12:00:00+02:00"`
    - `some_datetime.isoformat(" ", "minutes") == "2020-07-15 12:00+02:00"`
  - `datetime.__str__()`
    - for a datetime instance `d`, `str(d)` is equivalent to `d.isoformat(' ')`
  - see `test_datetime_instance_methods()`
- Some operations:
  - `some_datetime = datetime(2020, 7, 15, 12, 0, 0, tzinfo=timezone(timedelta(hours=2)))`
  - `some_datetime + timedelta(hours=24) == datetime(2020, 7, 16, 12, 0, 0, tzinfo=timezone(timedelta(hours=2)))`
  - `some_datetime + timedelta(hours=13) == datetime(2020, 7, 16, 1, 0, 0, tzinfo=timezone(timedelta(hours=2)))`
  - `some_datetime - datetime(2020, 7, 10, 10, 0, 0, tzinfo=timezone(timedelta(hours=2))) == timedelta(days=5, hours=2)`
  - `some_datetime - datetime(2020, 7, 15, 10, 0, 0, tzinfo=timezone.utc) == timedelta()`
  - see `test_datetime_operations()`

#### `strftime()` and `strptime()` Behavior

- `strftime()`
  - instance method
  - supported by `date`, `datetime`, and `time` objects
  - creates a string representing the time under the control of an explicit format string
  - `some_datetime.strftime("%A, %d %B %Y %I:%M%p %Z") == "Wednesday, 15 July 2020 12:00PM UTC+02:00"`
  - see `test_strftime()`
- `datetime.strptime()`
  - class method
  - creates a `datetime` object from a string representing a date and time and a corresponding format string
  - `datetime.strptime("15/7/20 12:00 +0200", "%d/%m/%y %H:%M %z")`
  - see `test_strptime()`
- Format codes: see <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>

### Data Compression

- Common data archiving and compression formats are directly supported by modules including: [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib), [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip), [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2), [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma), [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile) and [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile)

#### `zipfile`

- See [`zipfile_test.py`](src/ch10/zipfile_test.py)
- The [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile) module provides tools to create, read, write, append, and list a ZIP file
- Does not currently handle multi-disk ZIP files
- Can handle ZIP files that use the ZIP64 extensions (that is ZIP files that are more than 4 GiB in size)
- Supports decryption of encrypted files in ZIP archives, but it currently cannot create an encrypted file
  - extremely slow as it is implemented in native Python rather than C
- `class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None, *, strict_timestamps=True)`
  - opens a ZIP file, where `file` can be a path to a file (a string), a file-like object or a path-like object
  - `mode` parameter:
    - `'r'` to read an existing file
    - `'w'` to truncate and write a new file
    - `'a'` to append to an existing file
    - `'x'` to exclusively create and write a new file
  - `compression` is the ZIP compression method to use when writing the archive
    - should be `ZIP_STORED`, `ZIP_DEFLATED`, `ZIP_BZIP2` or `ZIP_LZMA`
  - if `allowZip64` is `True` (the default) `zipfile` will create ZIP files that use the ZIP64 extensions when the zipfile is larger than 4 GiB
  - `compresslevel` controls the compression level to use when writing files to the archive
    - when using `ZIP_STORED` or `ZIP_LZMA` it has no effect
    - when using `ZIP_DEFLATED`, integers 0 (no compression), 1 (best speed) through 9 (best compression) are accepted
      - see [`zlib`](https://docs.python.org/3/library/zlib.html#zlib.compressobj) for more information
    - when using `ZIP_BZIP2` integers 1 through 9 are accepted
      - see [`bz2`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File) for more information
  - the `strict_timestamps` argument, when set to `False`, allows to zip files older than 1980-01-01 at the cost of setting the timestamp to 1980-01-01
    - similar behavior occurs with files newer than 2107-12-31, the timestamp is also set to the limit
  - `ZipFile` is also a context manager and therefore supports the `with` statement
- `ZipFile.namelist()`
  - returns a list of archive members by name
- `ZipFile.open(name, mode='r', pwd=None, *, force_zip64=False)`
  - access a member of the archive as a binary file-like object
  - `name` can be either the name of a file within the archive or a `ZipInfo` object
  - `pwd` is the password used to decrypt encrypted ZIP files
  - the `mode` parameter, if included, must be `'r'` (the default) or `'w'`
    - `mode='r'`: the file-like object (`ZipExtFile`) is read-only and provides the following methods:
      - `read()`, `readline()`, `readlines()`, `seek()`, `tell()`, `__iter__()`, `__next__()`
    - `mode='w'`: a writable file handle is returned, which supports the `write()` method
  - `open()` is also a context manager
- `ZipFile.extract(member, path=None, pwd=None)`
  - extracts a member from the archive to the current working directory
  - `member` must be its full name or a `ZipInfo` object
  - `path` specifies a different directory to extract to
  - `pwd` is the password used for encrypted files
  - returns the normalized path created (a directory or new file)
- `ZipFile.extractall(path=None, members=None, pwd=None)`
  - extract all members from the archive to the current working directory
  - `path` specifies a different directory to extract to
  - `members` is optional and must be a subset of the list returned by `namelist()`
- `ZipFile.read(name, pwd=None)`
  - returns the bytes of the file name in the archive
  - `name` is the name of the file in the archive, or a `ZipInfo` object
  - the archive must be open for read or append
- `ZipFile.testzip()`
  - reads all the files in the archive and check their CRCs and file headers
  - returns the name of the first bad file, or else returns `None`
- `ZipFile.write(filename, arcname=None, compress_type=None, compresslevel=None)`
  - writes the file named `filename` to the archive, giving it the archive name `arcname` (by default, this will be the same as filename, but without a drive letter and with leading path separators removed)
  - `compress_type` overrides the value given for the `compression` parameter to the constructor for the new entry
  - `compresslevel` overrides the constructor if given
  - the archive must be open with mode `'w'`, `'x'` or `'a'`
- `ZipFile.writestr(zinfo_or_arcname, data, compress_type=None, compresslevel=None)`
  - writes a file into the archive
  - the contents is `data`, which may be either a `str` or a `bytes` instance
  - `zinfo_or_arcname` is either the file name it will be given in the archive, or a `ZipInfo` instance
  - the archive must be opened with mode `'w'`, `'x'` or `'a'`
- `zipfile.is_zipfile(filename)`
  - returns `True` if `filename` is a valid ZIP file based on its magic number, otherwise returns `False`
  - `filename` may be a file or file-like object

### Performance Measurement

- The [`timeit`](https://docs.python.org/3/library/timeit.html#module-timeit) module provides a simple way to time small bits of Python code
- Has both a command line interface as well as a Python interface
- In contrast to `timeit`'s fine level of granularity, the [`profile`](https://docs.python.org/3/library/profile.html#module-profile) and [`pstats`](https://docs.python.org/3/library/profile.html#module-pstats) modules provide tools for identifying time critical sections in larger blocks of code

### Quality Control

- The [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest) module provides a tool for scanning a module and validating tests embedded in a program's docstrings
  - test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring
  - improves the documentation by providing the user with an example and it allows the `doctest` module to make sure the code remains true to the documentation
  - see [`doctest_factorial.py`](src/ch10/doctest_factorial.py)

```console
$ python ch10/doctest_factorial.py
**********************************************************************
File "ch10/doctest_factorial.py", line 37, in __main__.factorial
Failed example:
    factorial(1)
Expected:
    0
Got:
    1
**********************************************************************
1 items had failures:
   1 of   7 in __main__.factorial
***Test Failed*** 1 failures.
```

```console
$ python ch10/doctest_factorial.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
Trying:
    ...
ok
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
        ...
    OverflowError: n too large
ok
Trying:
    factorial(1)
Expecting:
    0
**********************************************************************
File "ch10/doctest_factorial.py", line 37, in __main__.factorial
Failed example:
    factorial(1)
Expected:
    0
Got:
    1
1 items passed all tests:
   1 tests in __main__
**********************************************************************
1 items had failures:
   1 of   7 in __main__.factorial
8 tests in 2 items.
7 passed and 1 failed.
***Test Failed*** 1 failures.
```

### Batteries Included

#### `csv`

- See [`csv_test.py`](src/ch10/csv_test.py)
- The [`csv`](https://docs.python.org/3/library/csv.html#module-csv) module implements classes to read and write tabular data in CSV format
  - default registered dialects: `'excel'`, `'excel-tab'`, `'unix'`
- Some `csv` module functions:
  - `csv.reader(csvfile, dialect='excel', **fmtparams)`
    - returns a reader object which will iterate over lines in the given `csvfile`
    - `csvfile` can be any object which supports the iterator protocol and returns a string each time its `__next__()` method is called
      - file objects and list objects are both suitable
      - if `csvfile` is a file object, it should be opened with `newline=''`
    - optional `dialect` parameter can be given which is used to define a set of parameters specific to a particular CSV dialect
      - an instance of a subclass of the `Dialect` class
      - one of the strings returned by the `list_dialects()` function
    - optional `fmtparams` keyword arguments can be given to override individual formatting parameters in the current dialect
      - see 'Dialects and formatting parameters' below
    - each row read from the csv file is returned as a list of strings
    - no automatic data type conversion is performed unless the `QUOTE_NONNUMERIC` format option is specified
      - unquoted fields are transformed into `float`s
  - `csv.writer(csvfile, dialect='excel', **fmtparams)`
    - returns a writer object responsible for converting the user's data into delimited strings on the given file-like object
    - `csvfile` can be any object with a `write()` method
      - if `csvfile` is a file object, it should be opened with `newline=''`
    - optional `dialect` parameter - see above
    - optional `fmtparams` keyword arguments - see above
    - the value `None` is written as the empty string
    - all other non-string data are stringified with `str()` before being written
  - `csv.register_dialect(name[, dialect[, **fmtparams]])`
    - associate dialect with `name` (a string)
    - the dialect can be specified either by:
      - passing a sub-class of `Dialect`
      - `fmtparams` keyword arguments
      - both, with keyword arguments overriding parameters of the dialect
- Some `csv` module classes:
  - `class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)`
    - creates an object that operates like a regular reader but maps the information in each row to a `dict` whose keys are given by the optional `fieldnames` parameter
    - `fieldnames` parameter is a sequence
      - if omitted, the values in the first row of file `f` will be used as the field names
    - if a row has more fields than `fieldnames`, the remaining data is put in a list and stored with the fieldname specified by `restkey`
    - if a non-blank row has fewer fields than `fieldnames`, the missing values are filled-in with the value of `restval`
    - all other optional or keyword arguments are passed to the underlying `reader` instance
  - `class csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)`
    - creates an object which operates like a regular writer but maps dictionaries onto output rows
    - `fieldnames` parameter is a sequence of keys that identify the order in which values in the dictionary passed to the `writerow()` method are written to file `f`
    - optional `restval` parameter specifies the value to be written if the dictionary is missing a key in `fieldnames`
    - if the dictionary passed to the `writerow()` method contains a key not found in `fieldnames`, the optional `extrasaction` parameter indicates what action to take
      - if it is set to `'raise'`, the default value, a `ValueError` is raised
      - if it is set to `'ignore'`, extra values in the dictionary are ignored
    - any other optional or keyword arguments are passed to the underlying `writer` instance
  - `class csv.Dialect`
    - a container class relied on primarily for its attributes, which are used to define the parameters for a specific `reader` or `writer` instance
- Dialects and formatting parameters
  - to make it easier to specify the format of input and output records, specific formatting parameters are grouped together into dialects
  - a dialect is a subclass of the `Dialect` class having a set of specific methods and a single `validate()` method
  - when creating `reader` or `writer` objects, the programmer can specify a string or a subclass of the `Dialect` class as the `dialect` parameter
  - in addition to, or instead of, the `dialect` parameter, the programmer can also specify individual formatting parameters, which have the same names as the attributes defined below for the `Dialect` class
  - some attributes:
    - `Dialect.delimiter` (default: `','`)
      - a one-character string used to separate fields
    - `Dialect.quoting` (default: `QUOTE_MINIMAL`)
      - controls when quotes should be generated by the writer and recognised by the reader
      - can take on any of the `QUOTE_*` constants
- Reader objects
  - some reader object (`DictReader` instances and objects returned by the `reader()` function) methods:
    - `csvreader.__next__()`
      - returns the next row of the reader's iterable object as a
        - `list`: if the object was returned from `reader()`
        - `dict`: if it is a `DictReader` instance
    - `csvreader.fieldnames` (for `DictReader`)
      - if not passed as a parameter when creating the object, this attribute is initialized upon first access or when the first record is read from the file
- Writer objects
  - some writer object (`DictWriter` instances and objects returned by the `writer()` function) methods:
    - `csvwriter.writerow(row)`
      - writes the `row` parameter to the writer's file object
      - a `row` must be
        - for `writer` objects: an iterable of strings or numbers
        - for `DictWriter` objects: a dictionary mapping fieldnames to strings or numbers (by passing them through `str()` first)
      - returns the return value of the call to the `write` method of the underlying file object
    - `csvwriter.writerows(rows)`
      - writes all elements in `rows` (an iterable of `row` objects as described above) to the writer's file object
    - `DictWriter.writeheader()` (for `DictWriter` objects)
      - writes a row with the field names (as specified in the constructor) to the writer's file object
      - returns the return value of the `csvwriter.writerow()` call used internally

#### `xml.etree.ElementTree`

- See [`elementtree_test.py`](src/ch10/elementtree_test.py)
- Python's interfaces for processing XML are grouped in the [`xml`](https://docs.python.org/3/library/xml.html#module-xml) package
- **XML handling submodules**
  - `xml.etree.ElementTree`
  - [`xml.dom`](https://docs.python.org/3/library/xml.dom.html#module-xml.dom): the DOM API definition
  - [`xml.dom.minidom`](https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom): a minimal DOM implementation
  - [`xml.dom.pulldom`](https://docs.python.org/3/library/xml.dom.pulldom.html#module-xml.dom.pulldom): support for building partial DOM trees
  - [`xml.sax`](https://docs.python.org/3/library/xml.sax.html#module-xml.sax): SAX2 base classes and convenience functions
  - [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat): the Expat parser binding
- The [**`xml.etree.ElementTree`**](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module implements a simple and efficient API for parsing and creating XML data
- `xml.etree.ElementTree` has two classes for representing XML data
  - [`class ElementTree.ElementTree(element=None, file=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree)
    - the whole XML document as a tree
  - [`class ElementTree.Element(tag, attrib={}, **extra)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element)
    - a single node in this tree
- **Parsing XML data from a string or from a file**
  - [`ElementTree.fromstring(text, parser=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.fromstring)
    - same as [`XML()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML)
    - `text` is a string containing XML data
    - returns an `Element` instance, which is the root element of the parsed tree
    - `root = ET.fromstring('<data><country name="Liechtenstein"/><country name="Panama"/></data>')`
    - see `test_parse_string_pretty_print()`
  - [`ElementTree.parse(source, parser=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.parse)
    - parses an XML section into an element tree
    - `source` is a filename or file object containing XML data
    - returns an `ElementTree` instance
    - `tree = ET.parse(xml_file)`
    - see `test_parse_file()`
- Push and pull APIs
  - [`class ElementTree.XMLParser(*, target=None, encoding=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser)
    - event-based parsing, parsing events are translated to a push API
  - [`class ElementTree.XMLPullParser(events=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser)
    - pull parser for non-blocking applications
- Pretty-printing an ElementTree requires the use of `xml.dom.minidom`
  - see `test_parse_string_pretty_print()`
- **Visiting all children in order**
  - [`ElementTree.iter(tag=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.iter) (same with `Element`)
    - creates and returns a tree iterator for the root element
    - loops over all elements in this tree, in section order
    - `tag` is the tag to look for (default is to return all elements)
    - `for elem in root.iter()`
  - see `test_traverse_all()`
- **Finding elements**
  - [`ElementTree.findall(match, namespaces=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.findall) (same with `Element`)
    - finds all matching subelements, by tag name or XPath
    - returns a list containing all matching elements in document order
    - `for neighbor in tree.findall(".//neighbor")`
  - [`ElementTree.find(match, namespaces=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.find) (same with `Element`)
    - finds the first subelement matching `match`
    - `match` may be a tag name or a path
    - returns an element instance or `None`
    - `country.find("rank")`
  - [`Element.get(key, default=None)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.get)
    - gets the element attribute named `key`
    - returns the attribute value, or `default` if the attribute was not found
    - `country.get("name")`
  - [`Element.text`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.text)
  - see `test_find()`
- **Modifying an XML document**
  - `Element.text`
  - [`Element.set(key, value)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.set)
    - sets the attribute `key` on the element to `value`
    - `rank_elem.set("value", "1")`
  - [`Element.append(subelement)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.append)
    - adds the element `subelement` to the end of this element's internal list of subelements
    - `tree.getroot().append(malaysia)`
  - [`Element.insert(index, subelement)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.insert)
    - inserts `subelement` at the given position in this element
    - `tree.getroot().insert(1, monaco)`
  - [`Element.remove(subelement)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.remove)
    - removes `subelement` from the element
    - unlike the `find*` methods this method compares elements based on the instance identity, not on tag value or contents
    - `country.remove(neighbor)`
  - see `test_modify()`
- **Building an XML document**
  - note: the following can also be used to modify an XML document
  - [`ElementTree.SubElement(parent, tag, attrib={}, **extra)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.SubElement)
    - subelement factory
    - creates an element instance, and appends it to an existing element
    - returns an element instance
    - `country = ET.SubElement(root, "country", {"name": "Liechtenstein"})`
  - [`Element.extend(subelements)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.extend)
    - appends subelements from a sequence object with zero or more elements
  - see `test_build()`
- **Writing an XML document to a file**
  - [`ElementTree.write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None, method="xml", *, short_empty_elements=True)`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write)
    - writes the element tree to a file, as XML
    - `file` is a file name, or a file object opened for writing
    - the output is either a string (`str`) or binary (`bytes`)
      - controlled by the `encoding` argument
        - if encoding is `"unicode"`, the output is a string; otherwise, it's binary
    - `write(tmp_xml_path, "UTF-8", True)`
  - see `test_write()` and `test_pretty_write()`
- **Parsing XML with namespaces**
  - if the XML input has namespaces, tags and attributes with prefixes in the form `prefix:sometag` get expanded to `{uri}sometag`
    - `prefix` is replaced by the full URI
  - if there is a default namespace, that full URI gets prepended to all of the non-prefixed tags
  - one way to search and explore namespaced XML is to manually add the URI to every tag or attribute in the XPath of a `find()` or `findall()`
    - `tree.find("{http://people.example.com}actor")`
  - a better way to search namespaced XML is to create a dictionary with your own prefixes and use those in the search functions
    - `tree.find("people:actor", namespaces)`
  - see `test_namespace_manual()` and `test_namespace_dict()`

#### `sqlite3`

- See [`sqlite3_test.py`](src/ch10/sqlite3_test.py)
- SQLite is a C library that provides a lightweight disk-based database that doesn't require a separate server process
- The [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) module provides a SQL interface compliant with the DB-API 2.0 specification described by [PEP 249](https://www.python.org/dev/peps/pep-0249)
- **SQLite and python types**

| Python type | SQLite type |
| ----------- | ----------- |
| `None`      | `NULL`      |
| `int`       | `INTEGER`   |
| `float`     | `REAL`      |
| `str`       | `TEXT`      |
| `bytes`     | `BLOB`      |

- **Creating a database**
  - [`sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements, uri])`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)
    - opens a connection to the SQLite database file database
    - by default returns a `Connection` object, unless a custom factory is given
  - file-based database
    - an SQLite database is stored as a single file on the file system
    - the library manages access to the file, including locking it to prevent corruption when multiple writers use it
    - the database is created the first time the file is accessed, but the application is responsible for managing the table definitions, or schema, within the database
    - `sqlite3.connect(tmp_path.joinpath("sqlite3.db"))`
    - see `fixture_connect_file_db()`
  - in-memory database
    - SQLite supports managing an entire database in RAM
    - each connection creates a separate database instance
    - `sqlite3.connect(":memory:")`
    - see `fixture_connect_memory_db()`
- **Using the connection as a context manager**
  - connection objects can be used as context managers that automatically commit or rollback transactions
  - in the event of an exception, the transaction is rolled back; otherwise, the transaction is committed
  - see `test_context_manager_commit()` and `test_context_manager_rollback()`
- **Performing SQL commands**
  - [`Cursor.executescript(sql_script)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript) (also with [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executescript))
    - non-standard convenience method for executing multiple SQL statements at once
    - returns a cursor
    - see `create_schema()`
  - [`Cursor.executemany(sql, seq_of_parameters)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany) (also with [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executemany))
    - executes an SQL command against all parameter sequences or mappings found in the `seq_of_parameters`
    - `seq_of_parameters` can be a list, tuple, iterator, generator or dictionary
    - returns a cursor
    - see `insert_data()`
  - [`Cursor.execute(sql[, parameters])`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute) (also with [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute))
    - executes an SQL statement
    - returns a cursor
  - `execute()` and `executemany()` support two kinds of placeholders:
    - question marks (qmark style)
      - `cursor.execute("insert into tasks (details, deadline) values (?, ?);", ("Task 1", "2020-07-11"))`
      - see `test_context_manager_commit()`
    - named placeholders (named style)
      - `cursor.execute("insert into tasks (details, deadline) values (:det, :dline);", {"det": "Task 1", "dline": "2020-07-11"})`
      - see `test_context_manager_rollback()`
- **Retrieving data**
  - cursor as an iterator
    - `list(cursor.execute("select * from tasks order by priority"))`
    - see `test_retrieve_iterator()`
  - [`Cursor.fetchone()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchone)
    - fetches the next row of a query result set
    - returns a single sequence, or `None` when no more data is available
    - see `test_retrieve_fetch_one()`
  - [`Cursor.fetchall()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchall)
    - fetches all (remaining) rows of a query result, returning a list
    - returns an empty list if no rows are available
    - see `test_retrieve_fetch_all()`
  - [`class sqlite3.Row`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row)
    - serves as a highly optimized [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory) for `Connection` objects
    - supports mapping access by column name and index, iteration, representation, equality testing and `len()`
    - if two `Row` objects have exactly the same columns and their members are equal, they compare equal
    - see `test_retrieve_row()`
  - [`Connection.row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory)
    - a callable:
      - accepts the cursor and the original row (as a tuple)
      - returns a customized result row object
    - see `test_retrieve_object()`
- **Adapters and converters**
  - [`sqlite3.register_adapter(type, callable)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_adapter)
    - registers a callable to convert the custom Python type type into one of SQLite's supported types
  - [`sqlite3.register_converter(typename, callable)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_converter)
    - registers a callable to convert a bytestring from the database into a custom Python type
  - [`sqlite3.PARSE_DECLTYPES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES)
    - constant, to be used with the `detect_types` parameter of the `connect()` function
    - makes the `sqlite3` module parse the declared type for each column it returns
      - e.g., "integer" from "integer primary key"
    - it will look into the converters dictionary and use the converter function registered for that type there
  - default adapters and converters for the `date` and `datetime` types
    - the default adapters send them as ISO dates/ISO timestamps to SQLite
    - the default converters are registered under the name "date" for `datetime.date`, and "timestamp" for `datetime.datetime`
    - see `test_default_date_adapter_converter()`
- **Saving a database**
  - [`iterdump()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.iterdump)
    - returns an iterator to dump the database in an SQL text format
    - see `test_save_database()`

#### `gettext`

- The [`gettext`](https://docs.python.org/3/library/gettext.html#module-gettext) module provides internationalization (I18N) and localization (L10N) services for Python modules and applications
- Supports both the GNU gettext message catalog API and a higher level, class-based API
- Compatible with the GNU `gettext` library for message translation and catalog management
- Provides tools to
  - extract messages from a set of source files
  - build a message catalog containing translations
  - use that message catalog to display an appropriate message for the user at runtime
- Translation workflow overview
  1. identify and mark up literal strings in the source code that contain messages to translate
  2. extract the messages
     - use `xgettext` to extract them and create a `.pot` (portable object template) file, or translation template
  3. translate the messages
     - give a copy of the `.pot` file to the translator, changing the extension to `.po` (portable object)
     - the translator should update the header text in the file and provide translations for all of the strings
  4. "compile" the message catalog from the translation
     - compile the completed `.po` file to the binary catalog format using `msgfmt`
     - the binary format is used by the runtime catalog lookup code
  5. load and activate the appropriate message catalog at runtime
     - add a few lines to the application to configure and load the message catalog and install the translation function
- Creating message catalogs from source code
  - `gettext` works by looking up literal strings in a database of translations, and pulling out the appropriate translated string
  - bind the _lookup function_ to the name `"_"` (a single underscore character)
    - see [`gettext_example.py`](src/ch10/gettext_example.py)
  - the message extraction program, `xgettext`, looks for messages embedded in calls to the catalog lookup functions
    - `_('This message is in the script.')`
  - extract the message and create the `.pot` file, using `pygettext.py` or `xgettext`
    - `$ xgettext -o example.pot gettext_example.py`
    - see [`example.pot`](src/ch10/example.pot)
  - message catalogs are installed into directories organized by _domain_ and _language_
    - domain: provided by the application or library, and is usually a unique value like the application name, e.g., `example`
    - language value: provided by the user's environment at runtime
      - through one of the environment variables `LANGUAGE`, `LC_ALL`, `LC_MESSAGES`, or `LANG`, depending on their configuration and platform
  - create the required directory structure and copy the template in to the right spot
    - `$localedir/$language/LC_MESSAGES/$domain.po`, e.g., `locale/en_GB/LC_MESSAGES/example.po`
    - `locale` directory inside the source tree
    - better to use a directory accessible system-wide so that all users have access to the message catalogs
  - edit `example.po`
    - change the values in the header
    - set the alternate messages
      - see [`example.po`](src/ch10/locale/en_GB/LC_MESSAGES/example.po)
  - build the catalog from the `.po` file using `msgformat`
    - `cd locale/en_GB/LC_MESSAGES && msgfmt -o example.mo example.po`
  - running `gettext_example.py` now produces:
    - `This message is in the en_GB catalog.`
- Plural values
  - `gettext` treats pluralization as a special case
  - depending on the language, the difference between the singular and plural forms of a message may vary by
    - the ending of a single word
    - the entire sentence structure
  - use `ngettext()` to access the plural substitution for a message
    - see [`gettext_example.py`](src/ch10/gettext_example.py)
  - in the `.po` file, since there are alternate forms to be translated
    - the replacements are listed in an array
    - the library needs to be told about the way plurals are formed so it knows how to index into the array for any given count value
      - the line `"Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\n"` includes two values to replace manually
      - `nplurals`: an integer indicating the size of the array (the number of translations used)
      - `plural`: a C language expression for converting the incoming quantity to an index in the array when looking up the translation
      - e.g., `"Plural-Forms: nplurals=2; plural=n != 1;\n"`
      - see [`example.po`](src/ch10/locale/en_GB/LC_MESSAGES/example.po)
- Switching Translations
  - earlier examples use a single translation for the duration of the program
  - some situations, especially web applications, need to use different message catalogs at different times, without exiting and resetting the environment
    - the class-based API provided in `gettext` will be more convenient
    - API calls are essentially the same as the global calls, but the message catalog object is exposed and can be manipulated directly, so that multiple catalogs can be used
- See also:
  - <https://pymotw.com/3/gettext/index.html>
  - <https://www.gnu.org/software/gettext/manual/gettext.html>

## 11. Brief Tour of the Standard Library - Part II

### Output Formatting

#### `reprlib`

- See [`reprlib_test.py`](src/ch11/reprlib_test.py)
- The [`reprlib`](https://docs.python.org/3/library/reprlib.html#module-reprlib) module provides a version of `repr()` customized for abbreviated displays of large or deeply nested containers
- Some `Repr` instance attributes:
  - [`maxstring`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxstring)
    - limit on the number of characters in the representation of the string
    - default is 30
    - see `test_reprlib_string()`
  - [`maxdict`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxdict)
    - limit on the number of entries represented for the the dictionary
    - default is 4 entries
    - see `test_reprlib_dict()`

#### `pprint`

- See [`pprint_test.py`](src/ch11/pprint_test.py)
- The [`pprint`](https://docs.python.org/3/library/pprint.html#module-pprint) module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter
- When the result is longer than one line, the "pretty printer" adds line breaks and indentation to more clearly reveal data structure
- [`class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True)`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter)
  - constructs a `PrettyPrinter` instance
  - `stream`: if not specified, `PrettyPrinter` uses `sys.stdout`
- Some `PrettyPrinter` instance methods:
  - [`PrettyPrinter.pformat(object)`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.pformat)
    - returns the formatted representation of `object`
    - see `test_pretty_printer()`
  - [`PrettyPrinter.pprint(object)`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.pprint)
    - prints the formatted representation of object on the configured stream, followed by a newline
- Some module shortcut functions:
  - [`pprint.pformat(object, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)`](https://docs.python.org/3/library/pprint.html#pprint.pformat)
    - returns the formatted representation of `object` as a string
  - [`pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)`](https://docs.python.org/3/library/pprint.html#pprint.pprint)
    - prints the formatted representation of `object` on `stream`, followed by a newline
    - see `test_pprint_pformat()`
  - [`pprint.pp(object, \*args, sort_dicts=False, \*\*kwargs)](https://docs.python.org/3/library/pprint.html#pprint.pp)`
    - prints the formatted representation of `object` followed by a newline
    - see `test_pp()`

#### `locale`

- See [`locale_test.py`](src/ch11/locale_test.py)
- The [`locale`](https://docs.python.org/3/library/locale.html#module-locale) module accesses the POSIX locale database of culture-specific data formats
- Note: on Linux
  - check supported locales: `locale -a`
  - add locale: `sudo locale-gen de_DE.UTF-8`
  - update locale settings: `sudo update-locale`
- Some module functions:
  - [`locale.setlocale(category, locale=None)`](https://docs.python.org/3/library/locale.html#locale.setlocale)
    - modifies the locale setting for the `category`
    - `locale` may be a string, or an iterable of two strings (language code and encoding)
    - returns the new locale settng as a string
  - [`locale.resetlocale(category=LC_ALL)`](https://docs.python.org/3/library/locale.html#locale.resetlocale)
    - sets the locale for `category` to the default setting
  - [`locale.format_string(format, val, grouping=False, monetary=False)`](https://docs.python.org/3/library/locale.html#locale.format_string)
    - formats a number `val` according to the current `LC_NUMERIC` setting
    - the format follows the conventions of the `%` operator
  - [`locale.currency(val, symbol=True, grouping=False, international=False)`](https://docs.python.org/3/library/locale.html#locale.currency)
    - formats a number `val` according to the current `LC_MONETARY` settings
  - [`locale.atof(string)`](https://docs.python.org/3/library/locale.html#locale.atof)
    - converts a string to a floating point number, following the `LC_NUMERIC` settings
  - [`locale.atoi(string)`](https://docs.python.org/3/library/locale.html#locale.atoi)
    - converts a string to an integer, following the `LC_NUMERIC` conventions

### Templating

- See [`template_test.py`](src/ch11/template_test.py)
- The `string` module includes a versatile [`Template class`](https://docs.python.org/3/library/string.html#string.Template) with a simplified syntax suitable for editing by end-users
- The format uses placeholder names formed by `$` with valid Python identifiers (alphanumeric characters and underscores)
  - surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces
  - `Template("${village}folk send $$10 to $cause")`
- [`substitute(mapping={}, /, **kwds)`](https://docs.python.org/3/library/string.html#string.Template.substitute)
  - performs the template substitution
  - returns a new string
  - see `test_template_substitute()`
  - raises `KeyError` exception if placeholders are missing from `mapping` and `kwds`
  - raises `ValueError` exception if a literal `$` is not escaped using `$$`
  - see `test_template_exception()`
- [`safe_substitute(mapping={}, /, **kwds)`](https://docs.python.org/3/library/string.html#string.Template.safe_substitute)
  - like `substitute()`, except that
    - if placeholders are missing from `mapping` and `kwds`, the original placeholder will appear in the resulting string intact
    - any other appearances of the `$` will simply return `$`
  - see `test_template_safe_substitute()`
- You can derive subclasses of `Template` to customize the placeholder syntax, delimiter character, or the entire regular expression used to parse template strings
  - by overriding certain class attributes
  - see `test_template_customise()`

### Multi-threading

TBD - as a separate chapter

### Logging

- See [`logging_test.py`](src/ch11/logging_test.py)
- The logging library offers several categories of components:
  - _loggers_: expose the interface that application code directly uses
  - _handlers_: send the log records (created by loggers) to the appropriate destination
  - _filters_: provide a finer grained facility for determining which log records to output
  - _formatters_: specify the layout of log records in the final output
- Log event information is passed between loggers, handlers, filters and formatters in a `LogRecord` instance
- Logging is performed by calling methods on instances of the `Logger` class
  - each instance has a name, and they are conceptually arranged in a namespace hierarchy using dots (periods) as separators
  - e.g., a logger named "scan" is the parent of the logger "scan.text"
  - a good convention to use when naming loggers is to use a module-level logger in each module that uses logging:
    - `logger = logging.getLogger(__name__)`
- Flow of log event information in loggers and handlers (any 'no' answer stops the flow):
  - logging call in user code
  - **logger** enabled for the level of call?
    - yes: create `LogRecord`
  - does a **filter** attached to logger accept the record?
    - yes: pass to handlers of current logger
      - **handler** enabled for level of `LogRecord`?
        - yes: pass `LogRecord` to attached filter
      - does a **filter** attached to handler accept the record?
        - yes: _emit (includes formatting)_
  - is **[`propagate`](https://docs.python.org/3/library/logging.html#logging.Logger.propagate)** true (default: true) for current logger?
    - yes: check parent logger
  - is there a **parent logger**?
    - yes: set current logger to parent
      - _go to 'pass to handlers of current (parent) logger'_
- The root of the hierarchy of loggers is called the root logger
  - the logger used by the module functions `debug()`, `info()`, `warning()`, `error()` and `critical()`
  - see <https://docs.python.org/3/library/logging.html#module-level-functions>
- Defaults
  - informational and debugging messages are suppressed and the output is sent to standard error
  - effective log level
    - if a level is not explicitly set on a logger, the level of its parent (or ancestor) is used as its effective level
    - the root logger always has an explicit level set (`WARNING` by default)
  - [`logging.lastResort`](https://docs.python.org/3/library/logging.html#logging.lastResort)
    - handler of last resort
    - a `StreamHandler` writing to `sys.stderr` with a level of `WARNING`
    - handle logging events in the absence of any logging configuration
  - [`logging.basicConfig(**kwargs)`](https://docs.python.org/3/library/logging.html#logging.basicConfig)
    - basic configuration for the logging system
    - creates a `StreamHandler` with a default `Formatter`, and adds it to the root logger
    - module functions `debug()`, `info()`, `warning()`, `error()` and `critical()` will call `basicConfig()` automatically if no handlers are defined for the root logger
- **Setting logging level**
  - the [default logging levels](https://docs.python.org/3/library/logging.html#logging-levels) are (from lowest to highest):
    - `NOTSET`, `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
  - [`Logger.setLevel(level)`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel)
    - when a logger is created, the level is set to `NOTSET`
      - root logger: all messages are processed
      - non-root logger: delegate to the parent
  - [`Handler.setLevel(level)`](https://docs.python.org/3/library/logging.html#logging.Handler.setLevel)
    - when a handler is created, the level is set to `NOTSET`
      - all messages are processed
  - see `test_set_level()`
- **Adding a handler to a logger**
  - [`Logger.addHandler(hdlr)`](https://docs.python.org/3/library/logging.html#logging.Logger.addHandler)
    - adds the specified [handler](https://docs.python.org/3/library/logging.html#logging.Handler) `hdlr` to this logger
    - see <https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers> for a list of handlers provided by the `logging` and `logging.handlers` modules
    - note:
      - if you attach a handler to a logger and one or more of its ancestors, it may emit the same record multiple times
      - attach it to the appropriate logger which is highest in the logger hierarchy, and leave its descendants' `propagate` property set to `True`
      - a common scenario is to attach handlers only to the root logger, and to let propagation take care of the rest
  - see `LoggerSettings`
- **Logging messages**
  - [`Logger.debug(msg, *args, **kwargs)`](https://docs.python.org/3/library/logging.html#logging.Logger.debug)`
    - similarly so with `.info()`, `.warning()`, `.error()` and `.critical()`
    - similarly so with `logging.debug()`, etc.
    - logs a message at the corresponding level on this logger
    - `msg`: message format string
    - `args`: arguments which are merged into `msg` using the string formatting operator
    - `kwargs`: keyword arguments `exc_info`, `stack_info`, `stacklevel` and `extra`
    - see `test_log_message_args()`
- **Logging exceptions**
  - [`Logger.exception(msg, *args, **kwargs)`](https://docs.python.org/3/library/logging.html#logging.Logger.exception)
    - similarly so with `logging.exception()`
    - logs a message with level `ERROR` on this logger
    - should only be called from an exception handler
    - exception info is added to the logging message
    - see `test_log_exception()`
  - exceptions can also be logged at specific logging levels using the methods above
    - specify the `exc_info` keyword argument in `kwargs` as `True` to add exception information to the logging message
    - `logger.warning("Calculation error", exc_info=True)`
    - see `test_log_exception_warning()`
- **Adding stack information to the logging message**
  - specify the `stack_info` keyword argument in `kwargs` as `True` (defaults to `False`)
  - `logger.debug("Debug message", stack_info=True)`
  - see `test_log_stack_info()`
- **Formatting log message**
  - [`class logging.Formatter(fmt=None, datefmt=None, style='%')`](https://docs.python.org/3/library/logging.html#logging.Formatter)
    - responsible for converting a `LogRecord` to (usually) a string which can be interpreted by either a human or an external system
    - `fmt`
      - format string for the message as a whole, making use of [`LogRecord` attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)
      - default: `'%(message)s'`
    - `datefmt`
      - format string for the date/time portion of a message
      - default: `'%Y-%m-%d %H:%M:%S,uuu'`, where `uuu` is a millisecond value, and the other letters are as per [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime)
      - `logging.Formatter("%(asctime)s %(message)s", "%d/%m/%Y %H:%M:%S")`
      - see `test_format_datefmt()`
    - `style`
      - `'%'`: [printf-style](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting) (default)
        - `logging.Formatter("%(levelname)s %(funcName)s %(thread)s: %(message)s")`
      - `'{'`: [`str.format()`](https://docs.python.org/3/library/string.html#format-string-syntax) style
        - `logging.Formatter("{levelname} {funcName} {thread}: {message}", style="{")`
      - `'$'`: [`string.Template`](https://docs.python.org/3/library/string.html#string.Template) style
        - `logging.Formatter("$levelname $funcName $thread: $message", style="$")`
      - see `test_format()`
- **Logging extra information**
  - the fourth keyword argument, **`extra`**, in the `.debug()` etc. module functions/`Logger` methods can be used to pass a dictionary with contextual or user-defined attributes
  - `logging.Formatter("%(levelname)s [%(user)s]: %(message)s")`
  - `logger.warning("The message", extra={"user": "Some User"})`
  - see `test_log_extra()`
- **Configuring logging**
  - logging can be configured in 3 ways:
    - creating loggers, handlers, and formatters using Python code
    - creating a logging config file and reading it using the `fileConfig()` function
    - creating a dictionary of configuration information and passing it to the `dictConfig()` function
  - [`logging.basicConfig(**kwargs)`](https://docs.python.org/3/library/logging.html#logging.basicConfig)
    - basic configuration for the logging system by creating a StreamHandler with a default `Formatter` and adding it to the root logger
    - does nothing if the root logger already has handlers configured, unless the keyword argument `force` is set to `True`
    - see [`logging_basicconfig.py`](src/ch11/logging_basicconfig.py)
  - [`logging.config.dictConfig(config)`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig)
    - takes the logging configuration from a dictionary
  - [dictionary schema](https://docs.python.org/3/library/logging.config.html#dictionary-schema-details) - the dictionary passed to `dictConfig()` must contain the `version` key, and the following optional keys:
    - `formatters`
      - key: id
      - value: a dict consisting of
        - `format` and `datefmt` to construct a `Formatter` instance
    - `filters`
      - key: id
      - value: a dict describing how to configure a `Filter` instance
    - `handlers`
      - key: id
      - value: a dict consisting of
        - `class` (required): fully qualified handler class name
        - `level`
        - `formatter`: id of the formatter for this handler
        - `filters`: list of ids of the filters for this handler
        - other keys passed through as keyword arguments to the handler's constructor
    - `loggers`
      - key: logger name
      - value: a dict consisting of
        - `level`
        - `propagate`
        - `filters`: list of ids of filters for this logger
        - `handlers`: list of ids of handlers for this logger
    - `root`
      - configuration of the root logger
      - value: same as `loggers`
  - see:
    - [`logging_config.json`](src/ch11/logging_config.json)
    - [`logging_config.py`](src/ch11/logging_config.py)
- **Buffering logging messages and outputting them conditionally**
  - [`class logging.handlers.MemoryHandler(capacity, flushLevel=ERROR, target=None, flushOnClose=True)`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler)
    - buffers log records in memory, periodically flushing them to a target handler
      - when the buffer is full, or when an event of a certain severity or greater is seen
    - `capacity`: number of records buffered
  - see `test_log_buffering()` and `test_log_buffering_decorator()`
  - see also: <https://docs.python.org/3/howto/logging-cookbook.html#buffering-logging-messages-and-outputting-them-conditionally>
- See also:
  - <https://docs.python.org/3/howto/logging.html#logging-howto>
  - <https://docs.python.org/3/howto/logging-cookbook.html>
  - <https://pymotw.com/3/logging/index.html>

### Weak References

- See [`weakref_test.py`](src/ch11/weakref_test.py)
- Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles)
- The memory is freed shortly after the last reference to it has been eliminated
- A weak reference to an object is not enough to keep the object alive
  - when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else
- A primary use for weak references is to implement caches or mappings holding large objects, where it's desired that a large object not be kept alive solely because it appears in a cache or mapping
- For example, if you have a number of large binary image objects, you may wish to associate a name with each
  - if you used a dictionary to map names to images, or images to names, the image objects would remain alive just because they appeared as values or keys in the dictionaries
  - the [`WeakKeyDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakKeyDictionary) and [`WeakValueDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary) classes supplied by the [`weakref`](https://docs.python.org/3/library/weakref.html#module-weakref) module are an alternative, using weak references to construct mappings
  - if an image object is a value in a `WeakValueDictionary`
    - when the last remaining references to that image object are the weak references held by weak mappings
    - garbage collection can reclaim the object, and its corresponding entries in weak mappings are simply deleted

### Tools for Working with Lists

- See [`tools_for_lists_test.py`](src/ch11/tools_for_lists_test.py)

#### `array`

- The [`array`](https://docs.python.org/3/library/array.html#module-array) module provides an `array()` object that is like a list that stores only homogeneous data and stores it more compactly
  - array objects support the ordinary sequence operations of indexing, slicing, concatenation, and multiplication
  - array objects also implement the buffer interface, and may be used wherever bytes-like objects are supported
- [`class array.array(typecode[, initializer])`](https://docs.python.org/3/library/array.html#array.array)
  - a new array whose items are restricted by `typecode`, and initialized from the optional `initializer` value, which must be a list, a bytes-like object, or iterable over elements of the appropriate type
  - see `test_array()`

#### `collections` and `deque`

- The [`collections`](https://docs.python.org/3/library/collections.html#module-collections) module provides a `deque()` object
  - like a list with faster appends and pops from the left side
  - slower lookups in the middle
  - well suited for implementing queues and breadth first tree searches
- [`class collections.deque([iterable[, maxlen]])`](https://docs.python.org/3/library/collections.html#collections.deque)

  - generalization of stacks and queues
  - supports thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction
  - if `maxlen` is not specified or is `None`, deques may grow to an arbitrary length
    - otherwise, the deque is bounded to the specified maximum length
    - once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end
  - supports
    - iteration
    - pickling
    - `len(d)`
    - `reversed(d)`
    - `copy.copy(d)`
    - `copy.deepcopy(d)`
    - membership testing with the `in` operator
    - subscript references such as `d[0]` to access the first element
      - indexed access is O(1) at both ends but slows to O(n) in the middle
      - for fast random access, use lists instead
  - see `test_deque()`

#### `bisect`

- The [`bisect`](https://docs.python.org/3/library/bisect.html#module-bisect) module provides support for maintaining a list in sorted order without having to sort the list after each insertion
  - for long lists of items with expensive comparison operations, this can be an improvement over the more common approach
  - called bisect because it uses a basic bisection algorithm to do its work
- Some module functions:
  - [`bisect.bisect_left(a, x, lo=0, hi=len(a))`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left)
    - locates and returns the insertion point for `x` in `a` to maintain sorted order
    - if `x` is already present in `a`, the insertion point will be before (to the left of) any existing entries
    - the returned insertion point `i` partitions the array `a` into two halves so that:
      - `all(val < x for val in a[lo:i])` for the left side
      - `all(val >= x for val in a[i:hi])` for the right side
    - see `test_bisect_left()`
  - [`bisect.bisect(a, x, lo=0, hi=len(a))`](https://docs.python.org/3/library/bisect.html#bisect.bisect)
    - similar to `bisect_left()`, but returns an insertion point which comes after (to the right of) any existing entries of `x` in `a`
    - see `test_bisect_bisect()`
  - [`bisect.insort(a, x, lo=0, hi=len(a))`](https://docs.python.org/3/library/bisect.html#bisect.insort)
    - insert `x` in `a` in sorted order
    - `x` is inserted in `a` after any existing entries of `x`
    - note: the O(log n) search is dominated by the slow O(n) insertion step
    - see `test_bisect_insort()`

#### `heapq`

- The [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq) module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm
  - provides functions for implementing heaps based on regular lists
  - the lowest valued entry is always kept at position zero
  - heaps are binary trees for which every parent node has a value less than or equal to any of its children
  - this implementation uses arrays for which `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all `k`, counting elements from zero

```text
       0
   1       2
 3   4   5   6
```

- Some module functions:
  - [`heapq.heapify(x)`](https://docs.python.org/3/library/heapq.html#heapq.heapify)
    - transforms list `x` into a heap, in-place, in linear time
    - see `test_heapq_heapify()`
  - [`heapq.heappush(heap, item)`](https://docs.python.org/3/library/heapq.html#heapq.heappush)
    - pushes the value `item` onto the `heap`, maintaining the heap invariant
  - [`heapq.heappop(heap)`](https://docs.python.org/3/library/heapq.html#heapq.heappop)
    - pops and return the smallest item from the heap, maintaining the heap invariant
    - to access the smallest item without popping it, use `heap[0]`
  - [`heapq.heappushpop(heap, item)`](https://docs.python.org/3/library/heapq.html#heapq.heappushpop)
    - pushes `item` on the `heap`, then pop and return the smallest item from the `heap`
    - more efficient than `heappush()` followed by `heappop()`
    - see `test_heapq_push_pop()`
  - [`heapq.nlargest(n, iterable, key=None)`](https://docs.python.org/3/library/heapq.html#heapq.nlargest)
    - returns a list with the `n` largest elements from the dataset defined by `iterable`
    - performs best for smaller values of `n`
      - for larger values, it is more efficient to use the [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) function
    - see `test_heapq_nlargest()`

### Decimal Floating Point Arithmetic

- See [`decimal_test.py`](src/ch11/decimal_test.py)
- The [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal) module offers a [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal) datatype for decimal floating point arithmetic
- Compared to the built-in `float` implementation of binary floating point, the class is especially helpful for:
  - financial applications and other uses which require exact decimal representation,
  - control over precision,
  - control over rounding to meet legal or regulatory requirements,
  - tracking of significant decimal places, and
  - applications where the user expects the results to match calculations done by hand
- [`decimal.getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext)
  - returns the current context for the active thread
- [`class decimal.Context(prec=None, rounding=None, Emin=None, Emax=None, capitals=None, clamp=None, flags=None, traps=None)`](https://docs.python.org/3/library/decimal.html#decimal.Context)
  - creates a new context

## 12. `enum` - Enumerations

- See [`enum_test.py`](src/ch12/enum_test.py)
- The [`enum`](https://docs.python.org/3/library/enum.html#module-enum) module defines an enumeration type
- An enumeration is a set of symbolic names (members) bound to unique, constant values
  - can be used to create well-defined symbols for values, instead of using literal integers or strings
- **Creating an enumeration**
  - created using the `class` syntax or using a functional API
  - nomenclature:
    - class `Color` is an _enumeration_ (or _enum_)
    - attributes `Color.RED`, `Color.GREEN`, etc., are _enumeration members_ (or _enum members_) and are functionally constants
      - enum members are singletons
    - enum members have _names_ and _values_
      - the name of `Color.RED` is `RED`, the value of `Color.RED` is `1`
    - member values can be anything: `int`, `str`, etc.
  - enum members are hashable, so they can be used in dictionaries and sets
  - see `test_create()`
- **Iteration**
  - enums support iteration, in definition order
  - see `Color()` and `test_iteration()`
- **Comparing enumeration members**
  - enum members are compared by identity and equality
  - see `test_comparison()`
  - use [`IntEnum`](https://docs.python.org/3/library/enum.html#intenum) for `<` and `>` comparisons
    - see `test_comparison_intenum()`
- **Enumeration values**
  - duplicate enum values
    - having two enum members with the same same name is invalid, but two enum members are allowed to have the same value
    - given two members A and B with the same value, and A is defined first, B is an alias to A
    - see `test_enum_alias()`
  - unique enumeration values
    - use the `@enum.unique` class decorator to disallow enum members with te same value
  - automatic values
    - use [`auto()`](https://docs.python.org/3/library/enum.html#enum.auto) to automatically generate enum values
    - `CIRCLE = auto()`
    - see `test_auto_values()`
- **Creating enumerations programmatically**
  - the `Enum` class is callable to create enums programmatically
  - `Enum(value='NewEnumName', names=<...>, *, module='...', qualname='...', type=<mixed-in class>, start=1)`
    - `value`: what the new Enum class will record as its name
    - `names`: the enum members, which can be:
      - a whitespace- or comma-separated string of names
        - `PrimaryColor = Enum("PrimaryColor", "YELLOW RED BLUE")`
      - a sequence of names
      - a sequence of 2-tuples with key/value pairs
      - a mapping (e.g., dictionary) of names to values
    - see `test_programmatic_enums()`
- **Non-integer member values**
  - enum member values are not restricted to integers
    - can be any type of object
  - if your enumeration defines `__new__()` and/or `__init__()`, then whatever value(s) were given to the enum member will be passed into those methods
  - enums are Python classes, and can have methods and special methods
  - see `test_nonint_member_values()`
- See also:
  - <https://pymotw.com/3/enum/index.html>

## 13. Hashable Objects in Sets and Dictionaries

- See [`hash_test.py`](src/ch13/hash_test.py)
- [`object.__eq__(self, other)`](https://docs.python.org/3/reference/datamodel.html#object.__eq__)
  - `x == y` calls `x.__eq__(y)`
  - by default, `object` implements `__eq__()` by using `is`
    - returns `NotImplemented` in the case of a false comparison
  - `__ne__()` by default delegates to `__eq__()` and inverts the result unless it is `NotImplemented`
- For an object to be **hashable**
  - needs a **`__hash__()`** method
    - has a hash value which never changes during its lifetime
  - needs an **`__eq__()`** method
    - can be compared to other objects
  - hashable objects which compare equal must have the same hash value
  - note: you can use the [`dataclass`](https://docs.python.org/3.9/library/dataclasses.html) decorator with `eq=True` and `frozen=True` to create a hashable object
- [`object.__hash__(self)`](https://docs.python.org/3/reference/datamodel.html#object.__hash__)
  - called by built-in function `hash()` and for operations on members of **hashed collections** including `set`, `frozenset`, and `dict`
  - should return an integer
  - mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple

```python
def __hash__(self):
    return hash((self.name, self.nick, self.color))
```

- If a class **does not define an `__eq__()`** method, then it should **not define a `__hash__()`** operation either
  - if it **defines `__eq__()` but not `__hash__()`**, its instances will not be usable as items in hashable collections
    - its `__hash__()` is implicitly set to `None`
      - instances of the class will raise an appropriate `TypeError` when a program attempts to retrieve their hash value
      - will also be identified as unhashable when checking `isinstance(obj, collections.abc.Hashable)`
  - if a class defines **mutable objects** and implements an `__eq__()` method, it should not implement `__hash__()`
    - the implementation of hashable collections requires that a key's **hash value is immutable**
    - if the object's hash value changes, it will be in the wrong hash bucket
- User-defined classes have `__eq__()` and `__hash__()` methods by default
  - all objects compare unequal except with themselves
  - `x.__hash__()` returns an appropriate value such that `x == y` implies both that `x is y` and `hash(x) == hash(y)`
- If a class that overrides `__eq__()` needs to retain the implementation of `__hash__()` from a parent class
  - set `__hash__ = <ParentClass>.__hash__`
- If a class that does not override `__eq__()` wishes to suppress hash support
  - include `__hash__ = None` in the class definition
- A **set** object is an **unordered** collection of distinct **hashable objects**
  - 2 built-in set types: `set` and `frozenset`
  - the `set` type is mutable
    - since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set
  - the `frozenset` type is immutable and hashable
- A **mapping** object maps **hashable values** to arbitrary objects
  - mappings are mutable objects
  - 1 standard mapping type: the dictionary
  - values that are not hashable may not be used as keys

## Main Source

- "The Python Tutorial." _The Python Tutorial - Python 3.8.3 Documentation_, 19 May 2020, [docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html).
