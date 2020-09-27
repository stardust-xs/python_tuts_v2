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

### str.format_map()

It **formats** the string as per expectation using a **dictionary**. It is similar to **str.format()** method but takes only **one** argument.

- **mapping** - Dictionary of arguments to expand/replace in the **"{}"** placeholder.

```python
>>> string = "{name} is pretty active on {game}"
>>> mapping = {"name": "XA", "game": "YouTube"}
>>> print(string.format_map(mapping))
```

### str.index()

Similar to **str.find()**, it return the **index** position of the substring, if present else it will raise **ValueError**.
This method takes **three** arguments.

- **sub** - Substring to be searched.
- **start** (optional) - Starting index from where the substring needs to be searched, default: **0** (start of the string).
- **end** (optional) - Ending index till where the substring needs to be searched, default: total length of characters - 1.

```python
>>> string = "I'm XA. People call me XA for good reason now. They keep chanting XA! XA!"
>>> print(string.index("XA"))
>>> print(string.index("XA", 10, 30))
>>> print(string.index("XAMES3"))
```

### str.isalnum()

It checks if all the characters in string are **alphanumeric** (only alphabets and numbers) characters. If not returns **False**.

```python
>>> string = "XAMES3"
>>> print(string.isalnum())
>>>
>>> string = "XAMES3 is learning Java"
>>> print(string.isalnum())
```

### str.isalpha()

It checks if all the characters in string are only **alphabets**. If not returns **False**.

```python
>>> string = "XA"
>>> print(string.isalpha())
>>>
>>> string = "XAMES3 is still learning Java"
>>> print(string.isalpha())
```

### str.isdecimal()

It checks if all the characters in string are only **decimals**. If not returns **False**.
Here, decimal means just pure integers no subscripts, no superscripts and no fractions.

```python
>>> string = "69"
>>> print(string.isdecimal())
>>>
>>> string = "XAMES3"
>>> print(string.isdecimal())
>>>
>>> string = "4²"
>>> print(string.isdecimal())
```

### str.isdigit()

It checks if all the characters in string are only **digits**. If not returns **False**.
Here, digit means integers with support for Unicode based subscripts and superscripts but no fractions.

```python
>>> string = "69"
>>> print(string.isdigit())
>>>
>>> string = "½"
>>> print(string.isdigit())
>>>
>>> string = "4²"
>>> print(string.isdigit())
```

### str.isidentifier()

It checks if the string could be used as a **valid identifier**. If not returns **False**.

```python
>>> string = "xames3"
>>> print(string.isidentifier())
>>>
>>> string = "_xam"
>>> print(string.isidentifier())
>>>
>>> string = "3semax"
>>> print(string.isidentifier())
```

### str.islower()

It checks if all the characters in the string are in **lowercase**. If not returns **False**.

```python
>>> string = "xames3"
>>> print(string.islower())
>>>
>>> string = "XA is a good man"
>>> print(string.islower())
>>>
>>> string = "xa is a really good man"
>>> print(string.islower())
```

### str.isnumeric()

It checks if all the characters in string are only **numbers**. If not returns **False**.
Here, numeric means numbers with support for Unicode based subscripts, superscripts, fractions, roman numerals, etc.

```python
>>> string = "xames3"
>>> print(string.isnumeric())
>>>
>>> string = "4²"
>>> print(string.isnumeric())
>>>
>>> string = "½"
>>> print(string.isnumeric())
```

### str.isprintable()

It checks if all the characters in the string are **printable** (letters, symbols, digits, punctuation and whitespace) or if the string is empty. If not returns **False**.

```python
>>> string = "xames3"
>>> print(string.isprintable())
>>>
>>> string = ""
>>> print(string.isprintable())
>>>
>>> string = "Hello\nWorld"
>>> print(string.isprintable())
```
