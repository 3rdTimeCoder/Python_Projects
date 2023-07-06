# Logical and Comparison Operations in Python

Logical operations in Python involve evaluating the truth or falsity of expressions and working with boolean values (`True` or `False`). Python provides three main logical operators: `and`, `or`, and `not`.

- `and` operator: Returns `True` if both operands are `True`, and `False` otherwise.
   ```python
   result = True and False  # result is False
   ```

- `or` operator: Returns `True` if at least one of the operands is `True`, and `False` if both operands are `False`.
   ```python
   result = True or False  # result is True
   ```

- `not` operator: Returns the opposite boolean value of the operand.
   ```python
   result = not True  # result is False
   ```

Logical operators can be used with boolean values or expressions that evaluate to boolean values. They are commonly used in conditional statements and loops to make decisions based on certain conditions.

In addition to the logical operators, Python also provides comparison operators that allow you to compare values and generate boolean results:

- `==` (Equality): Returns `True` if the operands are equal, and `False` otherwise.
   ```python
   result = 5 == 3  # result is False
   ```

- `!=` (Inequality): Returns `True` if the operands are not equal, and `False` if they are equal.
   ```python
   result = 5 != 3  # result is True
   ```

- `>` (Greater than): Returns `True` if the left operand is greater than the right operand, and `False` otherwise.
   ```python
   result = 5 > 3  # result is True
   ```

- `<` (Less than): Returns `True` if the left operand is less than the right operand, and `False` otherwise.
   ```python
   result = 5 < 3  # result is False
   ```

- `>=` (Greater than or equal to): Returns `True` if the left operand is greater than or equal to the right operand, and `False` otherwise.
   ```python
   result = 5 >= 3  # result is True
   ```

- `<=` (Less than or equal to): Returns `True` if the left operand is less than or equal to the right operand, and `False` otherwise.
   ```python
   result = 5 <= 3  # result is False
   ```

Logical and comparison operators allow you to make decisions and perform actions based on the truth or falsity of conditions, enabling you to create conditional statements and control the flow of your program.

<br>
<hr>

# Summary
## evaluates to True/False (boolean - bool)

# == - means equals to, checks equality.
```
x = 1
y = "hello"
print(x == y)  # False
```

```
x = "Hello"
y = "hello"
print(x == y)  # False
```

```
x = "hello"
y = "hello"
print(x == y)  # True

```

# != - checks whether two things are not equal
```
x = "hello"
y = "hello"
print(x != y)  # False
```

# >, >=, <, <=
```
x = 1
y = 3
print(x > y)  # False
print(y > x)  # True
```

# >= - greater than or equals to
```
x = 1
y = 1
print(x >= y)  # True
print(y >= x)  # True
```

# and - only True if both conditions are True
```
x = 1 < 3
y = 2 >= 2
print(x and y)  # True
```

# or - only False if both conditions are False
```
x = 1 > 3
y = 2 > 2
print(x or y)  # False
```
