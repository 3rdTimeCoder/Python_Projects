## Program 1: Basic Calculator

```python
# Basic calculator.
# User input is always a string!!!
print("Valid operators: add, sub, mul, div, mod") # Tells the user what valid operations our calculator can do.
operator = input("Enter operator: ") # Prompts the user to enter input and stores it in the variable 'operator'.
num1 = int(input("Enter first number: ")) # Converts the input from string to an integer.
num2 = int(input("Enter second number: ")) # Converts the input from string to an integer.

if operator == "add":
    result = num1 + num2
    print(result)
elif operator == "sub":
    result = num1 - num2
    print(result)
elif operator == "mul":
    result = num1 * num2
    print(result)
elif operator == "div":
    result = num1 / num2
    print(result)
elif operator == "mod":
    result = num1 % num2
    print(result)
else:
    print("Invalid operator!")
```

- This program demonstrates the basic concepts of variables, data types, mathematical operations, logical operations, and control flow.
- The program acts as a simple calculator that performs operations based on user input.
- The valid operators are displayed to the user with the `print()` statement, providing information about the available operations.
- The program prompts the user to enter an operator and stores the input as a string in the variable `operator`.
- The program prompts the user to enter two numbers, which are then converted from strings to integers using the `int()` function, and stored in the variables `num1` and `num2`.
- The program uses an `if-elif-else` control flow structure to determine which operation to perform based on the value of `operator`.
- If the value of `operator` matches one of the valid operations ("add", "sub", "mul", "div", "mod"), the corresponding block of code is executed to perform the operation and display the result using the `print()` statement.
- If the value of `operator` does not match any of the valid operations, the `else` block is executed, and the program displays an "Invalid operator!" message.
- This program showcases the use of variables, input handling, type conversion, and conditional statements in Python.

<br>
<hr>

### Program 2: Number Classifier

```python
# Number Classifier
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

- This program classifies a number as positive, negative, or zero based on user input.
- The user is prompted to enter a number using the `input()` function, which is then converted to an integer using the `int()` function and stored in the variable `number`.
- The program uses an `if-elif-else` structure to determine the classification of the number.
- If the number is greater than 0, the program displays "The number is positive."
- If the number is less than 0, the program displays "The number is negative."
- If the number is neither greater nor less than 0 (i.e., equal to 0), the program displays "The number is zero."

<br>
<hr>

### Program 3: Temperature Converter

The formula for converting Celsius to Fahrenheit is:

```
F = (C * 9/5) + 32
```

Where:
- `F` represents the temperature in Fahrenheit.
- `C` represents the temperature in Celsius.

```python
# Temperature Converter
temperature = float(input("Enter the temperature in Celsius: "))
converted_temperature = (temperature * 9/5) + 32
print("The temperature in Fahrenheit is:", converted_temperature)
```

- This program converts a temperature from Celsius to Fahrenheit.
- The user is prompted to enter a temperature in Celsius using the `input()` function, which is converted to a float using the `float()` function and stored in the variable `temperature`.
- The program uses the conversion formula `(temperature * 9/5) + 32` to convert the temperature to Fahrenheit and stores the result in the variable `converted_temperature`.
- The program displays the converted temperature using the `print()` statement.

These examples demonstrate how the concepts of data types, variables, mathematical and logical operations, control flow, and input/output can be combined to create simple programs that perform specific tasks based on user input.

