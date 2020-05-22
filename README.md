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
- If you don’t want characters prefaced by `\` to be interpreted as special characters, you can use **raw strings** by adding an `r` before the first quote
  - see `test_raw_strings()`
- String literals can span **multiple lines**
  - one way is using triple-quotes: `"""..."""` or `'''...'''`
  - end of lines are automatically included in the string
    - possible to prevent this by adding a `\` at the end of the line
  - see `test_multiline()`
- Strings can be **concatenated** with the `+` operator, and **repeated** with `*`
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

- See examples in [`c04_more_control_flow_tools.py`](src/c04_more_control_flow_tools.py)

### `if` Statements

- An `if ... elif ... elif ...` sequence is a substitute for the `switch` or `case` statements found in other languages
- See `TestIf`

### `for` Statements

- Python's `for` statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence, rather than
  - always iterating over an arithmetic progression of numbers (like in Pascal), or
  - giving the user the ability to define both the iteration step and halting condition (as C)
- Code that modifies a collection while iterating over that same collection should loop over a copy of the collection or to create a new collection
- See `TestFor`

### The `range()` Function

- If you do need to iterate over a sequence of numbers, the built-in function [`range()`](https://docs.python.org/3/library/stdtypes.html#range) comes in handy
- The object returned by `range()` is an iterable
- See `TestRange`

### `break` and `continue` Statements, and `else` Clauses on Loops

- The `break` statement breaks out of the innermost enclosing `for` or `while` loop
- The `continue` statement continues with the next iteration of the loop
- Loop statements may have an `else` clause
  - executed when
    - the loop terminates through exhaustion of the iterable (with `for`)
    - the condition becomes false (with `while`)
  - but not when the loop is terminated by a `break` statement
- See `TestBreakElse`

### `pass` Statements

- The `pass` statement does nothing
- It can be used when a statement is required syntactically but the program requires no action
- Another place is as a placeholder for a function or conditional body when you are working on new code
- See `MyEmptyClass`

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
  - although they may be referenced
  - see `test_var_assign()`
- The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called
  - arguments are passed using _call by value_ (where the value is always an _object reference_, not the value of the object)
- When a function calls another function, a new local symbol table is created for that call
- A function definition introduces the function name in the current symbol table
  - the value of the function name can be assigned to another name which can then also be used as a function
    - serves as a general renaming mechanism
  - see `test_function_rename()`
- Functions without a `return` statement do return a value - `None`
  - see `test_function_no_return()`

### More on Defining Functions

- It is possible to define functions with a variable number of arguments

#### Default Argument Values

- See `TestFunctionArguments`
- The most useful form is to specify a default value for one or more arguments
  - creates a function that can be called with fewer arguments than it is defined to allow
  - see `test_default_args()`
- **Important warning**
  - the default value is evaluated only once
  - this makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes
    - can result in the default mutable object accumulating arguments passed to it on subsequent calls
  - see `test_default_value_accumulation()`

#### Keyword Arguments

- See `TestFunctionArguments`
- Functions can also be called using keyword arguments of the form `kwarg=value`
  - keyword parameters are also referred to as named parameters
- In a function call
  - keyword arguments must follow positional arguments
  - all the keyword arguments passed must match one of the arguments accepted by the function
  - keyword arguments' order is not important
  - no argument may receive a value more than once
- See `test_keyword_arguments()`

#### Arbitrary Argument Lists

- See `TestArbitraryArguments`
- When a final formal parameter of the form `**name` is present
  - it receives a **dictionary** containing all keyword arguments except for those corresponding to a formal parameter
    - see `test_arbitrary_keyword_arguments()`
  - may be combined with a formal parameter of the form `*name`
    - receives a **tuple** containing the positional arguments beyond the formal parameter list
- `*name` must occur before `**name`
  - see `test_combined_arbitrary_arguments()`
- Before the variable number of arguments, zero or more normal arguments may occur
- Any formal parameters which occur after the `*name` parameter are 'keyword-only' arguments
  - see `test_arbitrary_argument_list()`

#### Special parameters

- _Note: This works with Python 3.8+ only_
- A function definition may look like:

```text
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

##### Keyword-Only Arguments

- Placing an `*` in the arguments list just before the first keyword-only parameter
  - mark parameters as keyword-only
  - indicating the parameters must be passed by keyword argument

#### Unpacking Argument Lists

- The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments
  - write the function call with the `*`-operator to unpack the arguments out of a list or tuple
- In the same fashion, dictionaries can deliver keyword arguments with the `**`-operator
- See `TestUnpackArgumentLists`

#### Lambda Expressions

- Small anonymous functions can be created with the `lambda` keyword
- Lambda functions can be used wherever function objects are required
- They are syntactically restricted to a single expression
- Like nested function definitions, lambda functions can reference variables from the containing scope
- See `TestLambda`

#### Function Annotations

- Function annotations are completely optional metadata information about the types used by user-defined functions
  - see [PEP 3107](https://www.python.org/dev/peps/pep-3107) and [PEP 484](https://www.python.org/dev/peps/pep-0484) for more information
- Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation
- Return annotations are defined by a literal `->`, followed by an expression, between the parameter list and the colon denoting the end of the `def` statement
- Example: `def function_annotations(ham: str, eggs: str = "eggs") -> str`

## Source

- "The Python Tutorial." _The Python Tutorial - Python 3.8.3 Documentation_, 19 May 2020, docs.python.org/3/tutorial/index.html.
