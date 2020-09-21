# Operations on Variables

In Python, operations on variables look similar to a mathematical expressions with some minor differences. Therefore, all the rules of basic mathematical properties like **[Associative property](https://en.wikipedia.org/wiki/Associative_property)**, **[Commutative property](https://en.wikipedia.org/wiki/Commutative_property)**, etc. apply in Python too.

There are couple of operations that we can do on variables like **Arithmetic operations**, **Assignments operations**, **Comparison operations** (Relational operations), **Logical operations** and **Identity-Membership operations**.

## Arithmetic Operations

The basic **[Arithmetic operations](https://en.wikipedia.org/wiki/Arithmetic#Arithmetic_operations)** in Python are **addition**, **subtraction**, **multiplication**, **division**, **floored division**, **modulus** and **exponential** operations.

**Note:** These can be performed only on **Numbers** and few operations are supported by **Strings** and **Lists**.

### Addition

Addition is the most basic operation of arithmetics.
Addition is **commutative** and **associative**, so the order in which terms are added does not matter.

**Note:** This is true only for adding numbers.

```python
first_operand, second_operand = 415, 5 # Parallel variable assignment
total = first_operand + second_operand # total = 420
```

In Python, we can take addition to one step further. Python supports addition of **strings** and **lists**.

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

total = list_1 + list_2 # total = [1, 2, 3, 4, 5, 6] - This is called List Extension.
```

and

```python
str_1 = "Hello"
str_2 = "World"

total = str_1 + str_2 # total = "HelloWorld" - This is called String Concatenation.
```

**Note:** You can perform addition only on values of **same** type (datatype). Performing addition on variables of different datatype will throw **TypeError**.

### Subtraction

Subtraction is **opposite** of Addition. Subtraction is neither **commutative** nor **associative**, so the order in which terms are subtracted does matter alot. Subtraction is only supported by numbers in Python.

```python
first_operand, second_operand = 425, 5
total = first_operand - second_operand # total = 420
```

### Multiplication

Multiplication is also **commutative** and **associative** like addition and it is [**distributive**](https://en.wikipedia.org/wiki/Distributive_property) as well.

```python
first_operand, second_operand = 42, 10
total = first_operand * second_operand # total = 420
```

Just like Addition, Multiplication can be performed on **strings** and **lists**.

```python
list_1 = [1, 2, 3]

total = list_1 * 3 # total = [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

and

```python
str_1 = "Ha"

total = str_1 * 3 # total = "HaHaHa"
```

**Note:** You can perform multiplication of **lists** and **strings** with **integers** only.

### Division

Division is essentially **opposite** of Multiplication. Like Subtraction, Division is also neither **commutative** nor **associative**, so the order in which terms are divided does matter alot. Division is only supported by numbers in Python and output of division operation always returns a **float** value.

```python
first_operand, second_operand = 4200, 10
total = first_operand / second_operand # total = 420.0
```

**Note:** Division returns **quotient** in **float**.

### Floored Division

Floored Division is just like normal division but this return an **Integral** part of the output value. Means it always returns an **integer** part before the decimal. Floored Division is carried out with **"//"** operator in Python.

```python
# Normal Division:
first_operand, second_operand = 25, 9
total = first_operand / second_operand # total = 2.7777777777777777

# Floored Division:
first_operand, second_operand = 25, 9
total = first_operand // second_operand # total = 2
```

**Note:** Floored Division returns **quotient** as **integer without rounding-off** the value.

### Modulus

Modulus or **[Modulo](https://en.wikipedia.org/wiki/Modulo_operation)** operation returns **remainder**. It is carried out using **"%"** operator in Python. The output of a modulus operation could be either **float** or **integer** depending upon the **type of the operands**.

```python
first_operand, second_operand = 4200, 10
total = first_operand % second_operand # total = 0
```

### Exponentiations

[**Exponentiation**](https://en.wikipedia.org/wiki/Exponentiation) or Powers in Python are represented using **"\*\*"** (double asterisk) operator. Like Modulus, the output of Exponentiation operation could also be either **float** or **integer** depending upon the **type of the operands**.

```python
first_operand, second_operand = 2, 3
total = first_operand ** second_operand # total = 8
```

## Assignment Operations

**[Assignments operations](https://en.wikipedia.org/wiki/Augmented_assignment)** are carried out using **[Augmented Assignment](https://en.wikipedia.org/wiki/Augmented_assignment)** or **Compound Assignment**.

An augmented assignment is generally used to replace a statement where an operator takes a variable operates on it and then assigns the result back to the same variable.

We can perform Assignment operations for basic arithmetic operators since this method is a short-hand (shortcut) for writing the arithmetic expression. Also Assignment operations are neither **commutative** nor **associative** so the sequence of operands **does** matter a lot.

**Note:** Please remember all the execution or operations on objects in Python happen from **Right to Left**.

### Addition Assignment

This is how we write Addition assignment.

```python
first_operand, second_operand = 415, 5
first_operand += second_operand # first_operand = 420

# This is basically
first_operand = first_operand + second_operand
```

**Note**: Please note that the first object (object to the left-hand side) gets assigned with the output.

### Subtraction Assignment

This is how we write Subtraction assignment. Execution is **similar** to that of Addition Assignment.

```python
first_operand, second_operand = 425, 5
first_operand -= second_operand # first_operand = 420

# This is basically
first_operand = first_operand - second_operand
```

### Multiplication Assignment

This is how we write Multiplication assignment. Again execution is **similar** to that of above assignment methods.

```python
first_operand, second_operand = 42, 10
first_operand *= second_operand # first_operand = 420

# This is basically
first_operand = first_operand * second_operand
```

### Division Assignment

This is how we write Division assignment. **Similar** execution as above.

This too will return **float** as output by default.

```python
first_operand, second_operand = 4200, 10
first_operand /= second_operand # first_operand = 420.0

# This is basically
first_operand = first_operand / second_operand
```

### Floored Division Assignment

This is how we write Floored Division assignment.

```python
first_operand, second_operand = 4200.0, 10.0
first_operand //= second_operand # first_operand = 420

# This is basically
first_operand = first_operand // second_operand
```

### Modulus Assignment

This is how we write Modulus assignment.

```python
first_operand, second_operand = 420, 10
first_operand %= second_operand # first_operand = 0

# This is basically
first_operand = first_operand % second_operand
```

### Exponentiation Assignment

This is how we write Exponentiation assignment.

```python
first_operand, second_operand = 2, 3
first_operand **= second_operand # first_operand = 8

# This is basically
first_operand = first_operand ** second_operand
```

## Comparison Operations

**[Comparison operations](https://en.wikipedia.org/wiki/Relational_operator)** or **Relational operations** are carried out to check the **similarities** in Python object. These return **boolean** and are usually used in **If - Else** conditional loops.

Read more **[here](https://en.wikipedia.org/wiki/Relational_operator#Sameness_(object_identity)_vs._content_equality)**. This article will help you understand how, when and why to use **Comparison operations**.

### Equal to

**Equal to** operations are carried out using **"=="** (double equal to) operator in Python.

Equal to is **commutative**.

```python
first_operand, second_operand = 69, 69
output = first_operand == second_operand # output = True

first_operand, second_operand = 619, 69
output = first_operand == second_operand # output = False
```

### Not Equal to

**Not Equal to** operations are carried out using **"!="** operator in Python.

Like Equal to, Not Equal to is **commutative** too.

```python
first_operand, second_operand = 69, 69
output = first_operand != second_operand # output = False

first_operand, second_operand = 619, 69
output = first_operand != second_operand # output = True
```

### Less Than, Greater Than, LTET and GTET

These are the obvious ones.

```python
# Less than operation
first_operand, second_operand = 69, 420
output = first_operand < second_operand # output = True

# Greater than operation
first_operand, second_operand = 619, 69
output = first_operand > second_operand # output = True

# Less than equal to operation
first_operand, second_operand = 420, 420
output = first_operand <= second_operand # output = True

# Greater than equal to operation
first_operand, second_operand = 619, 69
output = first_operand >= second_operand # output = True
```

## Logical Operations

**[Logical operations](https://en.wikipedia.org/wiki/Logical_connective#Computer_science)** are the ones which usually revolves around the concepts of **[logical gates](https://en.wikipedia.org/wiki/Logic_gate)** in Digital Electronics and kinda works exactly like the same. These are **usually\*** used along in the Comparison Operations.

The output of the logical operations is often in **0** and **1**.
**None**, **False**, **0** (integer/float), **\[\]** (empty list) and **{}** (empty dictionary) are considered to be **0** in Logical operations.

**Note:** Booleans are **subclass** (child class) of **Integers**, hence in Python **0** and **1** can also be resolved or treated as **False** and **True** respectively.

### Logical AND

If all values are **True** output will be **True**. Treat **AND** operation as **multiplication** (at least for understanding).
See this table:

| Operand 1 | AND | Operand 2 | Output |
|:---------:|:---:|:---------:|:------:|
|     0     |  .  |     0     |    0   |
|     0     |  .  |     1     |    0   |
|     1     |  .  |     0     |    0   |
|     1     |  .  |     1     |    1   |

```python
first_operand, second_operand = 420, 420  # Non - Zero values represent True
output = first_operand and second_operand # output = 420 (This represents 1 or True)

first_operand, second_operand = [], 420
output = first_operand and second_operand # output = [] (This represents 0 or False)
```

**Important Tip:** If both the operands are False, **first operand** will be considered as the output.

### Logical OR

If all values are **False** output will be **False**. Treat **OR** operation as **addition** (at least for understanding).
See this table:

| Operand 1 | OR | Operand 2 | Output |
|:---------:|:--:|:---------:|:------:|
|     0     |  + |     0     |    0   |
|     0     |  + |     1     |    1   |
|     1     |  + |     0     |    1   |
|     1     |  + |     1     |    1   |

```python
first_operand, second_operand = 420, 420  # Non - Zero values represent True
output = first_operand or second_operand  # output = 420 (This represents 1 or True)

first_operand, second_operand = [], 0
output = first_operand or second_operand  # output = 0 (This represents 0 or False)
```

**Important Tip:** If both the operands are False, **last operand** will be considered as the output.

### Logical NOT

This is a simple negation.

```python
first_operand = 420         # Non - Zero value represent True
output = not first_operand  # output = False

first_operand = 0           # False value
output = not first_operand  # output = 1 (This represents True)
```

## Identity - Membership Operations

These operations are left out for self-exploration over **[here](https://www.tutorialspoint.com/python/identity_operators_example.htm)** and **[here](https://www.tutorialspoint.com/python/membership_operators_example.htm)**.
