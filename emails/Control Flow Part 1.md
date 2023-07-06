## If-Else Statements:

If-else statements allow you to make decisions in your program based on certain conditions. They control the flow of execution by executing different blocks of code depending on whether a condition is true or false. Here's the basic syntax of an if-else statement in Python:

```python
if condition:
    # code to be executed if the condition is true
else:
    # code to be executed if the condition is false
```

- The `condition` is an expression that evaluates to either `True` or `False`.
- If the condition is true, the code inside the if block will be executed.
- If the condition is false, the code inside the else block (if present) will be executed.

Example:

```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

In this example, if the `age` variable is greater than or equal to 18, the program will print "You are eligible to vote." Otherwise, it will print "You are not eligible to vote."

<br>
<hr>

## Elif Statements:

The `elif` statement allows you to check additional conditions after the initial `if` condition is false. It provides an alternative choice among multiple conditions. Here's the syntax of an if-elif-else statement:

```python
if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition2 is true
else:
    # code to be executed if all conditions are false
```

- The `elif` statement is placed after the initial `if` statement and before the `else` statement (if present).
- It allows you to specify a new condition to check if the previous conditions are false.
- You can have multiple `elif` statements to check multiple conditions.

Example:

```python
grade = 85

if grade >= 90:
    print("Your grade is A.")
elif grade >= 80:
    print("Your grade is B.")
elif grade >= 70:
    print("Your grade is C.")
elif grade >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
```

In this example, the program checks the value of the `grade` variable and prints the corresponding grade. If the grade is greater than or equal to 90, it prints "Your grade is A." If the grade is between 80 and 89, it prints "Your grade is B." Similarly, it checks subsequent conditions with `elif` statements. If none of the conditions match, the `else` block executes, printing "Your grade is F."
Using if-elif-else statements allows you to handle multiple conditions and choose different paths of execution based on the evaluation of those conditions. It provides flexibility in decision-making and enables you to create more complex logic in your programs.

<br>
<hr>

## Nested if-else Statements:

You can also have nested if-else statements, where an if-else statement is placed inside another if or else block. This allows for more complex decision-making. Here's an example:

```python
age = 21

if age >= 18:
    if age == 18:
        print("You just reached the voting age.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

The nested if-else statements check the value of `age` to determine if the person is eligible to vote. If the age is greater than or equal to `18`, it checks if the age is exactly `18` using an inner `if` statement. If the age is `18`, it prints "You just reached the voting age." Otherwise, it prints "You are eligible to vote." If the age is less than `18`, it executes the outer `else` block and prints "You are not eligible to vote."

Nested if-else statements allow for more complex decision-making by combining multiple conditions and code blocks to handle various scenarios in your program.




<br>
<hr>

# Summary

## If Statement
```python
# if statement
# if (Condition evaluates to true):
    # do this
name = "Doobsie"
if name == "Luyanda":
    print("My name is Luyanda")
    print("still inside")
```
- The `if` statement is used to check a condition and execute the code block if the condition evaluates to `True`.
- If the condition `name == "Luyanda"` is `True`, the program will execute the indented code block under the `if` statement.
- In this case, since `name` is not equal to "Luyanda", the code block will not be executed.

## If-Else Statement
```python
# if - else statement
# if (Condition evaluates to true):
    # do this
# else:
    # do this instead
name = "Luyanda"
if name == "Luyanda":
    print("My name is Luyanda")
else:
    print("My name is not Luyanda")
```
- The `if-else` statement provides an alternative choice. It executes one code block if the condition is `True`, and a different code block if the condition is `False`.
- If the condition `name == "Luyanda"` is `True`, the program will execute the code block under the `if` statement. Otherwise, it will execute the code block under the `else` statement.
- In this case, since `name` is equal to "Luyanda", the code block under the `if` statement will be executed.

## Elif Statement
```python
# elif statement (just means else if)
# if (Condition evaluates to true):
    # do this
# elif (this condition is true):
    # do this instead
# else:
    # just do this
name = "Konke"
if name == "Luyanda":
    print("My name is Luyanda")
elif name == "Jabu":
    print("My name is Jabu")
else:
    print("My name is not Luyanda and it is not Jabu")
```
- The `elif` statement is short for "else if." It provides an additional condition to check if the previous condition(s) are `False`.
- If the condition `name == "Luyanda"` is `True`, the program will execute the code block under the `if` statement.
- If the condition `name == "Luyanda"` is `False`, it will check the next condition `name == "Jabu"`. If this condition is `True`, the program will execute the code block under the `elif` statement.
- If both conditions are `False`, the program will execute the code block under the `else` statement.
- In this case, since `name` is not equal to "Luyanda" or "Jabu", the code block under the `else` statement will be executed.

These control flow structures (`if`, `if-else`, and `elif`) allow you to make decisions in your programs based on specific conditions, enabling different paths of execution.
