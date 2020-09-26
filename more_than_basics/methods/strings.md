# String methods

**Note:** This session presumes you know something about strings in Python. For a quick review see **[this](https://github.com/xames3/python_tuts_v2/blob/master/basics/0300_datatypes_in_python.md#strings-str)**.

As we know by now, strings are built-in Python **classes**. Each and every class has some inherent **methods** by default. These string methods are useful for **string manipulation**.

## Methods

### str.capitalize()

It converts **first character** of a string to **uppercase** letter and rest to lowercases.

```python
>>> string = "I'm XAMES3 and I can do whatever dafaq I want!"
>>> print(string.capitalize())
```

### str.casefold()

Casefolding is used for **caseless matching** when comparing strings basically it means comparing or matching a string **case-insensitively**. It converts all the text in lowercase when comparing.

```python
uppercase_string = "ß"
lowercase_string = "ss"
print(uppercase_string.casefold() == uppercase_string.casefold())
```

### str.center()

It **pads** string with the specified character and takes **two** arguments.

- **width** - Length of the string with padded characters.
- **fillchar** (optional) - Padding character, default: **" "**.

**Note:** The total length of the string would be equal to the **width** argument.

```python
>>> string = "Hello Ladies"
>>> print(string.center(50, "*"))
```

### str.count()

It counts the occurrences of a **substring** (word/sentence) in the given string and takes **three** arguments.

- **substring** - String that needs to be counted.
- **start** (optional) - Starting index from where the substring needs to be searched, default: **0** (start of the string).
- **end** (optional) - Ending index till where the substring needs to be searched, default: total length of characters - 1.

```python
>>> string = "I'm XA. People call me XA for a reason. People keep chanting XA! XA!"
>>> print(string.count("XA"))
>>> print(string.count("XA", 2, 30))
```

### str.encode()

It **encodes** the string. Converting normal string to byte-string is called as **encoding**. Python supports various encoding standards like **Unicode (UTF-8)**, **ASCII**, **ISO**, etc. You can find more information **[here](https://docs.python.org/3/library/codecs.html#standard-encodings)**.
This method takes **two** arguments.

- **encoding** (optional)  - Encoding type or the Codecs, default: **utf-8 (Unicode Transformation Format - 8)**.
- **errors** (optional)  - Encoding failure response (substitution used), default: **strict**.

**Note:** There are multiple error responses:

- **strict** - Default response which raises a **UnicodeDecodeError** exception on failure.
- **ignore** - Ignores the unencodable unicode from the result.
- **replace** - Replaces the unencodable unicode with a question mark **"?"**.
- **xmlcharrefreplace** - Inserts XML character reference instead of unencodable unicode.
- **backslashreplace** - Inserts a **\uNNNN** escape sequence instead of unencodable unicode.
- **namereplace** - Inserts a **\N{...}** escape sequence instead of unencodable unicode

```python
>>> string = "XA is just awesome!
>>> print(string.encode())
>>> print(string.encode("utf-8"))
>>> print(string.encode("ascii", "ignore"))
```

### str.endswith()

It checks if the string **ends** with the specified string and returns **True** if the string ends with the specified string else vice versa.
This method takes **three** arguments.

- **suffix** - String or tuple of suffixes to be checked.
- **start** (optional) - Starting index from where the suffix needs to be searched, default: **0** (start of the string).
- **end** (optional) - Ending index till where the suffix needs to be searched, default: total length of characters - 1.

```python
>>> string = "XA is just an awesome person"
>>> print(string.endswith("person"))
>>> print(string.endswith("awesome", 10, 20))
>>> print(string.endswith(("god", "person", "human")))
```

### str.expandtabs()

It **replaces** all tab characters, **\t** with **whitespace** characters and takes a **single** argument.

- **tabsize** (optional) - Tab size to replace with whitespaces, default: **8**.

```python
>>> string = "XA is f#@king\tawesome"
>>> print(string.expandtabs())
>>> print(string.expandtabs(5))
```

### str.find()

It **finds** the **index** position of first occurrence of the substring, if present else it will returns **-1**.
This method takes **three** arguments.

- **sub** - Substring to be searched.
- **start** (optional) - Starting index from where the substring needs to be searched, default: **0** (start of the string).
- **end** (optional) - Ending index till where the substring needs to be searched, default: total length of characters - 1.

```python
>>> string = "I'm XA. People call me XA for a reason. People keep chanting XA! XA!"
>>> print(string.find("XA"))
>>> print(string.find("XA", 10, 30))
>>> print(string.find("XAMES3"))
```

### str.format()

It **formats** the string as per expectation and take **multiple** (both **args** and **kwargs**) arguments.
Basically, it is best used for substituting values in a static string with dynamic inputs.

```python
>>> string = "{} is good at using {}"
>>> print(string.format("XA", "GitHub")) # Using it as args
>>> print(string.format("Shivam", "Django"))
>>>
>>> string = "{name} is good at using {app}"
>>> print(string.format(name="XA", app="GitHub")) # Using it as kwargs
>>> print(string.format(name="Pranali", app="Flask"))
```
