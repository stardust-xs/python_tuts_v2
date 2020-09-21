# Datatypes in Python

**[Datatypes](https://en.wikipedia.org/wiki/Data_type)** are the one of the fundamental concepts in **computer science**. In simple terms it means **type of data**.
Now this data is often referred as an **object** in python.

In this session we'll see how these datatypes **look** like and can be **created** in python.

The most primitive or basic types of python **[built-in](https://docs.python.org/3/library/stdtypes.html?highlight=list#built-in-types)** objects are numeric type (**[int/float/complex](https://docs.python.org/3/library/stdtypes.html?highlight=list#numeric-types-int-float-complex)**), strings (**[str](https://docs.python.org/3/library/stdtypes.html?highlight=list#text-sequence-type-str)**), lists (**[list](https://docs.python.org/3/library/stdtypes.html?highlight=list#lists)**), dictionaries (**[dict](https://docs.python.org/3/library/stdtypes.html?highlight=list#mapping-types)**), sets (**[set](https://docs.python.org/3/library/stdtypes.html?highlight=list#set-types-set-frozenset)**), tuples (**[tuple](https://docs.python.org/3/library/stdtypes.html?highlight=list#tuples)**) and booleans (**[bool](https://docs.python.org/3/library/stdtypes.html?highlight=list#boolean-values)**). Datatypes mainly help python interpreter to understand the type of object it is working with and so it prepares the interpreter to be ready to execute a particular operation on the data.

Before understanding Datatypes, we need to understand type of data (**objects**) in python.

## Type of Data

In Python, objects come in all shapes and sizes.
If you want to understand datatypes my way, we'll classify the data into **two** major types: **Single type** and **Containers type** data.

### Single Type

Single type data (object) is a **single entity** assigned to a variable. Strings, Numbers, NoneType (**[None](https://docs.python.org/3/library/constants.html?highlight=nonetype#None)**), Boolean (**[bool](https://docs.python.org/3/library/functions.html#bool)**), etc are examples of Single type data. We can consider them as **constants** or **[Literals](https://render.githubusercontent.com/view/ipynb?commit=f59d18d2eb0a7b939a8e53bfdfe35c20ae48536f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f78616d6573332f707974686f6e5f7475746f7269616c732f663539643138643265623061376239333961386535336266646665333563323061653438353336662f6261736963732f303230305f7661726961626c65735f696e5f707974686f6e2e6970796e62&nwo=xames3%2Fpython_tutorials&path=basics%2F0200_variables_in_python.ipynb&repository_id=283241123&repository_type=Repository#Introduction). Read more here about [**built-in constants**](https://docs.python.org/3/library/constants.html?highlight=nonetype#built-in-constants) in python.

#### Strings (str)

By definition, *strings are [**immutable**] sequences or collections of **characters***.

Strings are what I like to call, "**Kachha Limbu**" in python. It behaves like both Single Type and a Container Type object. Strings are often referred as **Text Sequence Type** as they are literally a sequence (collection) of **characters** or **texts**. Unlike C, in python we don't have a dedicated **char** datatype.

Anything and everything wrapped in pair of either single quotes (**'like this'**), double quotes (**"or like this"**) or even triple quotes (**'''or even like this'''**) and (**"""this too...sigh"""**) is considered as a String object. Triple quotes are often used for writing string object that span over multiple lines. String objects can have one or multiple characters.

```python
# Single quotes
'This is a string with single quotes.'
# These quotes are useful for writing strings which use ("") in statements.
'I am not able to "see him".'

# Double quotes
"This is a string with double quotes."
# These quotes are useful for writing strings which use apostrophe (') in statements.
"Of course you can't see him, he's John Cena!"

# Triple quotes
'''This is a string with triple single quotes.'''
# These are helpful for writing long paragraphs or multi-line statements.
"""
I thought this is good example for displaying
Multi-line statements but turns out it's not!

You guys have a better suggestion?
"""
```

#### Numbers (int/float/complex)

There are three distinct numeric types: **integers**, **floating point** numbers, and **complex** numbers. In addition, Booleans are a subtype (child) of integers. Integers have **unlimited precision**.

Numbers are created by numeric literals (constants **0-9**). Numeric literals containing a decimal point (**.**) or an exponent sign (**e**) yield floating point numbers. Adding **'j'** or **'J'** to a numeric literal yields an imaginary number (a complex number with a zero real part) which you can add to an integer or float to get a complex number with real and imaginary parts. They support all sort of arithmetics. Please see [**this**](https://render.githubusercontent.com/view/ipynb?commit=f59d18d2eb0a7b939a8e53bfdfe35c20ae48536f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f78616d6573332f707974686f6e5f7475746f7269616c732f663539643138643265623061376239333961386535336266646665333563323061653438353336662f6261736963732f303230315f6f7065726174696f6e735f6f6e5f7661726961626c65732e6970796e62&nwo=xames3%2Fpython_tutorials&path=basics%2F0201_operations_on_variables.ipynb&repository_id=283241123&repository_type=Repository#Operations-on-Variables) for quick reference.

These are few ways of representing Integers in python:

```python
var_1 = 69              # Unsigned int

var_2 = -69             # Signed int

var_3 = 69_000_000      # Integer with commas (69,000,000)
```

These are few ways of representing Floats in python:

```python
var_1 = 69.0            # Unsigned float

var_2 = -69.0           # Signed float

var_3 = 69_000_000.420  # Float with commas (69,000,000.420)

var_4 = 6.9e+8          # Exponents
```

This is how we represent Complex in python:

```python
var_1 = 69j             # Only imaginary part

var_2 = 420 + 69j       # With real part
```

#### None (NoneType)

By definition, *None represents the absence of a value or [**null**](https://docs.python.org/3/library/stdtypes.html?highlight=list#the-null-object).*

None is a **singleton** (fancy advance concept that we will explore later). Python uses the keyword **None** to define null objects and variables.

This is how we write None:

```python
xa = None
```

**Note:** None resets the variable. It doesn't **delete** it.

#### Booleans (bool)

By definition, *Booleans mean either of the two literals (constant) objects **False** and **True**.*

They are used to represent truth values. Also Booleans are subclass (child class) of Integers, hence in python 0 and 1 can also be resolved or treated as False and True respectively.

```python
xa_is_god = True

xa_is_mortal = False
```

### Container Type

Container objects in this context means any python object that holds multiple elements. In simple terms, containers are exactly what it sounds like - they contain **elements**. These containers are special and play very important role in python's ecosystem. Strings, Sequences ([**list**](https://docs.python.org/3/library/stdtypes.html?highlight=list#list)/[**tuple**](https://docs.python.org/3/library/stdtypes.html?highlight=list#tuple)), Dictionaries ([**dict**](https://docs.python.org/3/library/stdtypes.html?highlight=list#mapping-types-dict)) and Sets ([**set**](https://docs.python.org/3/library/stdtypes.html?highlight=list#set-types)) etc are examples of Container type data.

#### Lists (list)

Lists are probably one of the most used and simplest datatype (data-structure) in python which is used to **contain** (hence a container) or store or hold a **list** of values.

Technically, a "*List is an **ordered** collection of elements.*"

But what does **ordered** means? Ordered means having **index** and retaining the **order** of creation in layman terms.
Lists have [**indexes**](https://en.wikipedia.org/wiki/Index_notation#In_computing) or **index notations**. Hence, we can access elements of a list using its **index** position. In python, like most of the programming languages the index starts with **zero**.

Lists are usually written with **"\[\]"** (square brackets) in python.

```python
# Empty list
xa = []

# List with single element
xa = ["Srusthi"]

# List of all string elements
xa = ["Shailesh", "Mini", "Shivam", "Sagar", "Pranali"]

# List of elements with different datatypes and duplicates
xa = [1, True, 4.0, 5, "6", None, _, 4.0, "Karnik", None]
```

Lists can hold virtually any valid python object and need not to be homogeneous (same elements). There are **no restrictions** on having number of elements in a list but lists are always **definite**! Meaning all the elements in the **"\[ \]"** (square brackets) seperated by **","** (commas) will be part of the list. There can be an empty list (zero elements), there can be list with only one element or there could be multiple elements.

A list could nest another list too.

#### Tuple (tuple)

Like Lists, Tuples are another **Sequence Type** data-structure (datatype) in python. If you understand lists, you'll be able to understand tuples in no time! Just like lists again, tuples also have **indexes** hence you can access elements of a tuple like a list. Tuples are usually written with **"()"** (round brackets) in python.

By definition, ***~~List~~** Tuple is an ordered collection of elements too but its **immutable**.*

```python
# Empty tuple
xa = ()

# Tuple with single element
xa = ("Ashish",) # Comma is very important here

# Tuple of all string elements
xa = ("DOCUMENT SAVER", "CR07", "Game Player", "XA", "Shubham")

# Tuple of elements with different datatypes and duplicates
xa = (None, _, 1, "DragonBall Z", 42.0, tuple(), "DragonBall Z")
```

Tuple can also hold virtually any valid python object and need not to be homogeneous (same elements). Similarly, there are **no restrictions** on having number of elements in a tuple and are **definite** too. There can be an empty tuple (zero elements), there can be list with only one element (intermediate level stuff) or there could be multiple elements. A tuple could nest another tuple too just like a list.

**Note:** Tuples are **faster** than a list in terms of program execution.

#### Dictionary (dict)

By definition, *Dictionaries are **unordered** collection of a **key-value** pairs*.

Dictionaries are unordered means, it doesn't support indexing and the order of the **"elements"** are not retained after the creation. This is not completely **true**! Python 3.6 and up **retains** a dictionary's order. Dictionaries are created using **{}** (curly brackets) in python.

There are some important things to note before creating a dictionary:

- A dictionary needs to have a key-value pair.
- The dictionary keys must be unique (not a compulsion though).
- Key must be an immutable object (more on that in next session).
- A dictionary can be empty.
- Dictionary's value can hold nested objects.

```python
# Empty dictionary
xa = {}

# Dictionary with single key-value pair
xa = {"name": "XA"}

# Dictionary with multiple key-value pairs
xa = {"name": "XA", "age" : 25, "gender": "Male", "type": "God-Tier"}
```

Here for the last example, **"name"** is the key whose paired value is **"XA"**. Similarly, for **"age"** its respective value is **25** (integer) and so on. This tells us value of a key-value pair of a dictionary object could be of any datatype.

#### Set (set)

By definition, *Sets are **unordered** collection of **unique** elements.*

These are unordered too, meaning the elements of a set cannot be accessed using an **index**. These is for a special reason. Since, a **set** is a collection of **unique** elements the duplicates are ignored and so is their **index**. It would be difficult to visualize this so its better to test it out by ourselves.

A set **looks like** combination of a sequence (list/tuple) and a dictionary. Just like a Dictionary, sets are created using **{}** (curly brackets) with elements seperated by commas (**,**) in python but you **cannot** create an empty set using this method. Since a pair of curly brackets **{}** resembles an empty dictionary, we need to use the **built-in** set type for creating an empty set.

```python
# Empty set
xa = set()

# Set with single element
xa = {"Shivam"}

# Set of elements with different datatypes and duplicates
xa = {True, "Game Player", 42.0, "Daulat", 69, range(10), "Daulat"}
```

Here for the last example, we can see there are **duplicates**. By definition, we cannot have duplicates in sets and hence when you print the output of last example, you'll get something like this

```python
print(xa)

# Output of last example
{True, range(0, 10), 69, 42.0, 'Game Player', 'Daulat'}
```
