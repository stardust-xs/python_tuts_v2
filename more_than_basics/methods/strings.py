xa = "I'm XAMES3 and I can do whatever dafaq I want!"


print(xa[-5:]) # Pranali's version


def slice(string: str,
          start: int = None,
          stop: int = None,
          step: int = None,
          reverse: bool = False) -> str:
  """Does slicing of a string."""
  start = start if start else 0
  stop = stop if stop else len(string)
  step = step if step else 1

  if reverse:
    return string[start:stop:step][::-1]
  else:
    return string[start:stop:step]


ya = slice(xa, 4, 10, 2)
print("XA:\n", (xa), "\nYA:\n", (ya))



'''

https://gist.github.com/nicolasdao/a7adda51f2f185e8d2700e1573d8a633
https://www.freecodecamp.org/news/how-open-source-licenses-work-and-how-to-add-them-to-your-projects-34310c3cf94/

'''
