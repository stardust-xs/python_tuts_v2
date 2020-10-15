# Navigated to that file.
# Accessing the file ending with .pem extension.
# Rename.

# import glob
# from os.path import join
# from kaamiki import socket

import os

# "/mnt/storage/development/programming/xa.py" -> Absolute Path/Complete Path
# "xa.py" -> Basename
# "xa" -> Stem

path = "/mnt/storage/development/programming/beta/python_tutorials/exercises/basics/atm_emulator/"

# xa = os.listdir(f"{path}")

# src = xa[3]
# dst = xa[3].replace("__init__", "xa")

# src = path + src
# dst = path + dst

# os.rename(src, dst)

for obj in os.listdir(path):
  if "__init__.py" == obj:
    src = obj
    dst = obj.replace("__init__", "xa-is-god")
    src = path + src
    dst = path + dst
    os.rename(src, dst)

  #   source = os.path.join(path, file)
  #   dest = os.path.join(path, "XA.xa")
  #   print(source, dest)

    # os.rename(f"{path}{file}", f"{path}XA.xa")

# print(dir(str.replace()))

# a = 10
# b = 10
# c = a
# print(a is b)




# isinstance


# xa = ["xa", "pranali", "srushti", "shailesh", "nimesh"]
# xa = [idx.upper() for idx in xa]
# ya = xa.copy()
# za = []
# for idx in xa:
#   (idx.upper())
# print(xa)
# print(za)
