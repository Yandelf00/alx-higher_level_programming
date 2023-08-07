# Python - Hello, World

In this project, I practiced using the Python interpreter, printing text
and variables, and working with strings, lists, and functions in Python.

## Function Prototypes :floppy_disk:

Below are the function prototypes for the functions written in this project:

| File                       | Prototype                             |
| -------------------------- | ------------------------------------- |
| `10-check_cycle.c`         | `int check_cycle(listint_t *list);`   |
| `102-magic_calculation.py` | `def magic_calculation(a, b):`        |

## Tasks :page_with_curl:

1. **Run Python File**
   - [0-run](./0-run): A Bash script that executes a Python script file saved in the environment variable `$PYFILE`.

2. **Run inline**
   - [1-run_inline](./1-run_inline): A Bash script that runs Python code saved in the environment variable `$PYCODE`.

3. **Hello, print**
   - [2-print.py](./2-print.py): A Python script that uses the `print` function to output `"Programming is like building a multilingual puzzle"`, followed by a new line.

4. **Print integer**
   - [3-print_number.py](./3-print_number.py): A Python script that prints an integer stored in the variable `number`, followed by `"Battery street"`, and a new line.

5. **Print float**
   - [4-print_float.py](./4-print_float.py): A Python script that prints a float stored in the variable `number` with a precision of two digits.

6. **Print string**
   - [5-print_string.py](./5-print_string.py): A Python script that prints a string stored in the variable `str` three times, followed by a new line, and then outputs the first nine characters of `str`, followed by another new line.

7. **Play with strings**
   - [6-concat.py](./6-concat.py): A Python script that uses string variables `str1 = "Holberton"` and `str2 = "School"` to print the string `"Welcome to Holberton School!"`.

8. **Copy - Cut - Paste**
   - [7-edges.py](./7-edges.py): A Python script that manipulates the string variable `word` to create three new string variables:
     - `word_first_3`: First three letters of `word`.
     - `word_last_2`: Last two letters of `word`.
     - `middle_word`: `word` without the first and last letters.

9. **Create a new sentence**
   - [8-concat_edges.py](./8-concat_edges.py): A Python script that directly outputs `"object-oriented programming with Python"`, followed by a new line, by manipulating the given string without creating new variables or string literals.

10. **Easter Egg**
    - [9-easter_egg.py](./9-easter_egg.py): A Python script that prints "The Zen of Python" by Tim Peters, followed by a new line.

11. **Linked list cycle**
    - [10-check_cycle.c](./10-check_cycle.c): A C function that checks if a linked list contains a cycle.
    - Returns `0` if there is no cycle and `1` if there is.
    - Helper files:
      - [linked_lists.c](./linked_lists.c): C functions for handling linked lists (provided by [source](https://github.com/holbertonschool/0x00.py/blob/master/linked_lists.c)).
      - [lists.h](./lists.h): Header file containing definitions and prototypes for functions used in [linked_lists.c](./linked_lists.c) and [10-check_cycle.c](./10-check_cycle.c).

12. **Hello, write**
    - [100-write.py](./100-write.py): A Python script that outputs `"and that piece of art is useful - Dora Korpar, 2015-10-19"`, followed by a new line, to the `stderr` stream using the `write` function from the `sys` module. The script exits with a status code of `1`.

13. **Compile**
    - [101-compile](./101-compile): A Python script that compiles a Python script file stored in the environment variable `$PYFILE` and saves the compiled bytecode to an output file named `$PYFILEc` (e.g., if `export PYFILE=my_main.py`, the output filename will be `my_main.pyc`).

14. **ByteCode -> Python #1**
    - [102-magic_calculation.py](./103-magic_calculation.py): A Python function that matches a given bytecode, provided by ALX.


