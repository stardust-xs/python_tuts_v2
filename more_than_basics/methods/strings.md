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
