#### Example 1: Iterating over a String

```python
my_string = "Hello World"

# Print each character in the string
for i in range(len(my_string)):
    print(my_string[i])
```

- In this example, the `for` loop iterates over the indices of the characters in the string.
- The `range(len(my_string))` function generates a sequence of numbers from 0 to the length of the string minus 1.
- In each iteration, the loop variable `i` takes on the value of each index, and the corresponding character is printed.

#### Example 2: `for` Loop with a Specified Range and Step

```python
# Print odd numbers from 1 to 10
for i in range(1, 11, 2):
    print(i)
```

- In this example, the `for` loop prints the odd numbers from 1 to 10.
- The `range(1, 11, 2)` function generates a sequence of numbers starting from 1, up to but not including 11, with a step of 2.
- In each iteration, the loop variable `i` takes on the value of each number in the sequence, and it is printed.

#### Example 3: Reversing a String

```python
name = input("Enter your name: ")
for i in range(len(name)-1, -1, -1):
    print(name[i], end="")
```

- In this example, the `for` loop is used to reverse a string entered by the user.
- The `range(len(name)-1, -1, -1)` function generates a sequence of indices in reverse order, starting from the last index of the string and ending at 0.
- In each iteration, the loop variable `i` takes on the value of each index, and the character at that index is printed.
- By using `end=""` in the `print()` function, each character is printed on the same line, resulting in the reversed string.

### `while` Loop

A `while` loop is used to repeat a block of code as long as a certain condition is `True`. Here's the basic syntax of a `while` loop:

```python
while condition:
    # Code to be executed as long as the condition is True
```

The loop continues to execute the code block as long as the `condition` remains `True`.

#### Example 4: `while` Loop with a Counter

```python
i = 0
while i < 6:
    print(i)
    i = i + 1  # Update the counter

print("done")
```

- In this example, the `while` loop is used to print numbers from 0 to 5.
- The loop continues as long as the value of `i` is less than 6.
- In each iteration, the value of `i` is printed, and then it is incremented by 1 using `i = i + 1`.
- When `i` becomes 6, the condition becomes `False`, and the loop terminates.

#### Example 5: `while` Loop with User Input

```python
while True:
    user_input = input("Enter number: ")
    print(user_input)
    if user_input == "quit":
        break
```

- In this example, the `while` loop takes user input repeatedly and prints it.
- The loop continues indefinitely because the condition `True` is always `True`.
- The user is prompted to enter a number, which is then printed.
- If the user enters the word "quit", the `break` statement is executed, and the loop is terminated.

These examples demonstrate how `for` and `while` loops can be used in different scenarios to repeat code execution based on different conditions. They offer flexibility and control for automating repetitive tasks and performing iterative operations in Python.
