# The Python Tutorial

Examples from [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

## 3. An Informal Introduction to Python

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

- See examples in [`src/c03_an_informal_introduction_to_python.py`](src/c03_an_informal_introduction_to_python.py)
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

- See examples in [`src/c03_an_informal_introduction_to_python.py`](src/c03_an_informal_introduction_to_python.py)
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

## Source

- "The Python Tutorial." _The Python Tutorial - Python 3.8.3 Documentation_, 19 May 2020, docs.python.org/3/tutorial/index.html.
