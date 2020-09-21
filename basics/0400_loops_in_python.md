# Loops in Python

**[Loops](https://en.wikipedia.org/wiki/LOOP_(programming_language))** are yet another fundamental concepts in **computer science**. In simple terms it means to **iterate** or **repeat** something.

**Note:** To understand loops properly, it is presumed that you know little bit about **[Containers](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)**.

In programming, usually all statements are executed **sequentially** i.e. line by line. But many times we come across instances wherein we need to repeat the execution multiple times. Loops come in handy during those situations. Most of the programming languages have the concept of **loops**. They help the developer to reduce the efforts for doing repetitive work. Essentially, loops are a **[control flow](https://en.wikipedia.org/wiki/Control_flow)** structure which deals with **iterations**.

By definition, *Repetitive execution of the same block of code is called as **looping** or **iterations**.*

These are usually called as **[Compound](https://docs.python.org/3/reference/compound_stmts.html)** statements as the statements or the code spans multiple lines. While (no pun intended) there are various types of loops in Python but, according to me loops could be classified into **two** simple types: **[Iterative](https://en.wikipedia.org/wiki/Iteration#Computing)** loop and **[Conditional](https://en.wikipedia.org/wiki/Conditional_loop)** loop.

## Iterative Loop

Iterative loops are the structures (**[syntax](https://en.wikipedia.org/wiki/Python_syntax_and_semantics)**) that repeats till it gets exhausted. Means **iterative** loops run till all the elements from the **[containers](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)** are processed.

In Python, we classify iterative loops into **two** types: **[for](https://docs.python.org/3/reference/compound_stmts.html#for)** loop and **[while](https://docs.python.org/3/reference/compound_stmts.html#while)** loop.

### For loop

**For loop** is the most basic and common type of loop in programming. They are used for iterating over a **[container](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)** or **[sequence](https://github.com/xames3/python_tutorials/blob/master/basics/0301_types_of_data_in_python.md#mutable-objects)**. They are usually used to iterate upto a **definite** range or **fixed** range (some limit). Hence these are also considered as **Definite Loops**.

```python
# This is basic and general syntax of for loops in Python
for new_variable in container_object:
    # do something with the new variable
    new_variable...
```

From the above format, **new_variable** is some random variable that has never been created. This variable will be representing each member or element of the **[container_object](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#container-type)** till all the elements of the container are exhausted.

```python
>>> # Actual usage in Python using list object
>>> some_list = [1, "xa", 2.0, (), {"name": "kaamiki"}]
>>>
>>> for idx in some_list:
...     print(idx)
...
1
"xa"
2.0
()
{"name": "kaamiki"}
>>>
```

In the above example, we first defne our **container_object** which is a **[list](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#lists-list)** in our case.
Here, **idx** represents **new_variable** from the above format. What **for loop** essentially does is, it makes the **idx** variable to **[access each member](https://github.com/xames3/python_tutorials/blob/master/basics/0301_types_of_data_in_python.md#mutability-of-a-list)** or element of the **some_list** (**[list](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#lists-list)**) object.

The above format of the **for loop** can be used for writing any basic **for loop** with the basic types of containers like **[list](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#lists-list)**, **[tuple](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#tuple-tuple)**, **[set](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#set-set)** and **[dict](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#dictionary-dict)**.

**Note:** Using the above format while iterating through a dictionary object, only the **keys** would be accessed. Not the values.

#### For loop for Tuple object

```python
random_tuple = (69, 420.0, "xa")

for idx in random_tuple:
    # Doing something using idx, in this case printing values
    print(idx)
```

#### For loop for Set object

```python
set_object = {21, "nirvana"}

for idx in set_object:
    print(idx)
```

#### For loop for Dictionary object

Here, **idx** would represent the "**key**" of the the **lame_dict** dictionary object.

```python
lame_dict = {"key_1": "value_1", "key_2": "value_2"}

for idx in lame_dict:
    print(idx)
```

Besides the traditional containers (lists/dicts/tuples/set) there are other **two** basic built-in Python containers: **[range()](https://docs.python.org/3/library/stdtypes.html#ranges)** and **[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)**.

### Range in Python

**[range()](https://docs.python.org/3/library/stdtypes.html#ranges)** is a built-in function of Python. It is an **iterable** (something which contains more than one element) just like **Containers** and retuns something called as "**range object**". It essentially generates or returns an immutable sequence of **integers** between some starting point, stopping point and a step count.

**Note:** The range object is an instance of the **[range()](https://docs.python.org/3/library/stdtypes.html#ranges)** class (we usually call and treat it like a function) and not a list, tuple or any other container.

#### Defining a Range

```python
# Syntax of the range object
range(start, stop, step)
```

Typically, we define **range()** using some arguments. It takes mainly three arguments:

- **start**
  - Starting point or Starting integer of the sequence.
  - This is an optional argument, meaning we can ignore specifying any value to it.
  - By default, value of start is set to **0**.
- **stop**
  - Stopping point or Stopping integer of the sequence.
  - This is a required argument or positional argument, meaning we need to specify an integer.
  - The generated sequence usually ends or stops at `stop - 1`.
- **step**
  - Incrementation steps or gaps between each number of the sequence.
  - This is also an optional argument.
  - By default, value of the step is set to **1**.

**Note:** Please note that all the arguments of a range object take **integers** only.

#### Range in action

```python
range(10)       # Creates a range obj of 10 integers starting from 0 to 9

range(1, 11)    # Creates a range obj of 10 integers starting from 1 to 10

range(0, 10, 2) # Creates a range obj of 05 integers (even numbers)
```

If you try to print any of the above defined range object, you would get the same thing and thats really frustating! You cannot visualize a range object unless you encapsulate or wrap it in either a **list** or a **tuple**.

So try running this instead -

```python
>>> print(list(range(10))            # Here, start = 0, stop = 10 and step = 1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]       # The sequence starts with 0, stops at 10 - 1 and is incrementing by 1
>>>
>>> print(list(range(1, 11))         # Here, start = 1, stop = 11 and step = 1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      # The sequence starts with 1, stops at 11 - 1 and is incrementing by 1
>>>
>>> print(list(range(0, 10, 2))      # Here, start = 0, stop = 10 and step = 2
[0, 2, 4, 6, 8]                      # The sequence is starting off with 0 till 9 but incrementing by 2
```

#### Key takeaways while using range()

- A **range()** function (technically a class) always returns a **range** object which is neither a list or a tuple.
- All the input arguments should be **integers**.
- It supports 3 arguments at most and all 3 arguments could be **signed** or **unsigned** integers.
- Stop argument ensures that the sequence always stops or ends at **stop - 1**.
- The total number of integers generated by a range object can be calculated by **stop - start**.

```python
# range() using for loop
>>> for idx in range(5):
...    print(idx)
...
0
1
2
3
4
>>>
```

### Enumerate in Python

**[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)** is another built-in function of Python. Like **range()** it too is an **iterable** and retuns something called as "**enumerate object**". Similarly, it generates an immutable sequence of **tuples** of an **integer** and **element** of an iterable.

**Note:** Just like range, an enumerate object is an instance of the **[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)** class (we usually call and treat it like a function).

#### Defining Enumeration

```python
# Syntax of the enumerate object
enumerate(iterable, start)
```

At most, it takes only two arguments:

- **iterable**
  - This is a required or positional argument.
  - It could hold ay valid container object like strings, lists, tuple, etc.
- **start**
  - Starting point or Starting integer of the sequence.
  - This is an optional argument, meaning we can ignore specifying any value to it.
  - By default, value of start is set to **0**.

**Note:** Please note that all the arguments of a enumerate object take **integers** only.

#### Enumerate in action

```python
enumerate("XAMES3")             # Creates a enumerate obj which starts with 0

enumerate("XAMES3", start=1)    # Creates a enumerate obj which starts with 1
```

If you print any of the above enumerate object, like range you would get the same thing. This too cannot be visualize a enumerate object unless we encapsulate or wrap it in either a **list** or a **tuple**.

So try running this instead -

```python
>>> print(list(enumerate("XAMES3"))              # Here, start = 0
[(0, 'X'), (1, 'A'), (2, 'M'), (3, 'E'), (4, 'S'), (5, '3')]
>>>
>>> print(list(enumerate("XAMES3", start=1)))    # Here, start = 1
[(1, 'X'), (2, 'A'), (3, 'M'), (4, 'E'), (5, 'S'), (6, '3')]
>>>
```

#### Points to remember while using range()

- An **enumerate()** function (technically a class) always returns an **enumerate** object.
- First argument should always be an **iterable** or a **container**.
- Value assigned to `start` (second argument) should be an **integer**.

```python
# enumerate() using for loop
>>> for idx in enumerate("XAMES3", start=2):
...    print(idx)
...
(2, 'X')
(3, 'A')
(4, 'M')
(5, 'E')
(6, 'S')
(7, '3')
>>>
```
