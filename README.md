# The Python Tutorial

Examples from [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

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
  - [Source](#source)

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

## Source

- "The Python Tutorial." _The Python Tutorial - Python 3.8.3 Documentation_, 19 May 2020, [docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html).
