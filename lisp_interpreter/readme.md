# Basic Lisp Interpreter

This is a basic Lisp interpreter implemented in Python. It allows you to enter Lisp programs and execute them, providing the output of each evaluation.

## Usage

To use the Lisp interpreter, follow these steps:

1. Run the Python script `lisp.py` in your preferred Python environment.
2. The interpreter will start a Read-Eval-Print Loop (REPL) where you can enter Lisp expressions.
3. Enter a Lisp expression at the prompt (`lisp[count]> `) and press Enter to execute it.
4. The interpreter will evaluate the expression and display the result.

You can enter multiple expressions in sequence, and the interpreter will evaluate them one by one.

## Supported Features

The basic Lisp interpreter supports the following features:

- Arithmetic operations: addition, subtraction, multiplication, and division.
- Comparison operations: equality (`eq`).
- List operations: `car`, `cdr`, `cons`.
- Conditional statements: `cond`.
- User-defined functions: `defun`. (The implementation for this is glitchy, it works for basic one-parameter functions but not more complex ones.)

You can use these features to build more complex Lisp programs and execute them using the interpreter.

## Examples

Here are some examples of Lisp expressions that you can try in the interpreter:

1. Addition:

   ```
   lisp[1]> (+ 2 3)
   => 5
   ```

2. Conditional statement:

   ```
   lisp[2]> (cond ((eq 2 3) 'equal) ((eq 4 4) 'not_equal))
   => not_equal
   ```

3. User-defined function:

   ```
   lisp[3]> (defun double (x) (* x 2))
   => function created

   lisp[4]> (double 5)
   => 10
   ```

4. List operations:

   ```
   lisp[5]> (car (cons 1 (cons 2 (cons 3 '()))))
   => 1

   lisp[6]> (cdr (cons 1 (cons 2 (cons 3 '()))))
   => (2 3)
   ```

## Clearing the Terminal

To clear the terminal, simply enter the command `clear` at the prompt (`lisp[count]> `).


## Quitting the Interpreter

To exit the Lisp interpreter, simply enter the command `quit` at the prompt (`lisp[count]> `).

## Acknowledgements

This Lisp interpreter was developed using the Python programming language and the concepts of Lisp programming. It was inspired by the Lisp language and its rich history in the field of programming languages.

## Contact

For any questions, suggestions, or feedback, please contact [me](mailto:3rdtimecoder@gmail.com).