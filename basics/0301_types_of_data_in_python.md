# Types of Data in Python

As from the very first takeaway mentioned **[here](https://github.com/xames3/python_tutorials/blob/master/basics/0100_introduction_to_python.md#key-takeaways-from-python)**, *Everything in python is an **object***.

Even the **[datatypes](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#datatypes-in-python)**!
Based on the datatype we can classify an object to be either **Mutable** or **Immutable** object. This classification of datatype is a classical distinguishing factor in python.

**Note:** Please read **[this](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)** post as it does a better job of explaining the Mutable and Immutable objects in python.

**Container** types like **list**, **dict** and **set** are all **mutable** objects whereas **Single** type are all **immutable** objects along one container type, **tuple**. So even though its a container **tuples** are **immutable**. So now we know which python objects are mutable and which aren't.

But what the heck does these "**Mutable**" and "**Immutable**" means?!

**Note:** The descriptions of the Mutable and Immutable objects are intended for the **beginners** only.

## Mutable Objects

For starters, *Mutable objects (containers) are ones whose sequences can be altered or changed after their creation.*

Now lets break it down into smaller digestable pieces.
As stated above, *Mutable objects are those python objects whose **sequences***... **WAIT!**

What are **sequences**?
Sequence means the way the elements in a container have been written or arranged.

```python
# List is a Container (mutable object)
xa = [1, "XA", 69.0, {"this is a set object nested in a list"}]
```

Here, the created list has **[indexes](https://github.com/xames3/python_tutorials/blob/master/basics/0300_datatypes_in_python.md#lists-list)** starting with **0** where index position of integer **1** is **0**, index position of string object "**XA**" is **1** and so on. These indexes tell us that "**XA**" comes after **1** because of its index position and are hence in an increasing **Sequence**.

So, *Mutable objects are those python objects whose sequences can be **altered** or **changed***...

```python
# We created a list
xa = [1, "XA", 69.0, {"this is a set object nested in a list"}]

# Wrote some fancy python code and tried to modify the above list
...
...

# And later we got this -
xa = [1, "XAMES3", 69.0, {"this is a set object nested in a list"}]
```

Here we somehow (we'll see this later) updated or modified the string object "**XA**" to "**XAMES3**". What it means is we can **add** or **re-arrange** or **modify** or even **delete** the elements of a list (mutable objects) programmatically. The term **programmatically** signifies that the modifications or the updates have been done by the code after the object was created thus meaning **after creation**.

Lists, Dictionaries and Sets are **Mutable** objects, meaning you can update or modify the elements from these containers.

**Note:** The "**\[\]**" (square bracket) notation for accessing the elements has nothing to do with the Lists. We can access the values of a container using "**\[\]**" (square brackets) only!

### Mutability of a List

Lists are one the most versatile objects in python. They can grow, shrink and update values of the elements. For updating any value from a container, one must access it first!

```python
# Lets assume we created a list, xa
xa = ["I'm XA", "I'm great!", 2]

# Now we'll be accessing first element from the list
xa[0] # This will return "I'm XA"
```

The numbers we put in the square brackets are the **index** positions of the elements in the container. Once we're able to access the elements we'll try to modify it.

```python
xa[0] = "I'm XAMES3 actually"
```

The above means we are updating the value of element on **0th** index position. We can say that we're **updating** or **overwriting** the first value in that list. So when you try to print out the list you'll get the updated values.

```python
["I'm XAMES3 actually", "I'm great!", 2]
```

### Mutability of a Dictionary

Dictionaries on the other side **do not have indexes** but are considered as Mutable objects, so it means we can **update** or **add/delete** the elements off of a dictionary. Here, the role of the indexes is carried out by the **keys** of the dictionary.

Rest all is the same.

```python
# Lets assume we have a dictionary
xa = {"name": "XA", "age": 25}

# Now we want to update the elements here
xa["age"] = "25 years 3 months"

# The output would be {"name": "XA", "age": "25 years 3 months"}
```

### Mutability of a Set

Sets behave differently when it comes to their mutability. Dictionary and List objects let user to modify the elements but Set **doesn't**! This is because they are an **unordered** collection of unique elements. If they don't have order (index) they can't be accessed using the above mentioned "**\[\]**" (square bracket) notation.

Since sets don't hold duplicates, but they're considered to be mutable objects meaning because python **updates** or **modifies** the written or created set object (with duplicates) to collection of unique elements (without duplicates). In simple terms python is deleting the duplicates in a set object internally thus sticking to the definition of Mutable object.

## Immutable Objects

Immutable Objects are the one which do not let user to modify the elements of the container (**tuple** and **str**). Immutable objects include **str**, **tuple**, **bool**, etc.

If you try to **access** the elements of an Immutable object you won't have any problems, **BUT** if you try to **update** the element using "**\[\]**" (square bracket) notation you'll get an **Error**!

Try this yourself...
