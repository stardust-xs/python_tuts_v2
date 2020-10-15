# Navigated to that file.
# Accessing the file ending with .pem extension.
# Rename.

import os

path = "/mnt/storage/extracted/impactor_test/"
# xa = os.listdir(path)
# os.rename(f'{path}/xa2.pem', f"{path}/xa3.pem")

for file in os.listdir(path):
#   print(file, type(file))
  if file.endswith(".so"):
    source = os.path.join(path, file)
    dest = os.path.join(path, "XA.xa")
    print(source, dest)

    # os.rename(f"{path}{file}", f"{path}XA.xa")

# print(dir(str))







# isinstance


# xa = ["xa", "pranali", "srushti", "shailesh", "nimesh"]
# xa = [idx.upper() for idx in xa]
# ya = xa.copy()
# za = []
# for idx in xa:
#   (idx.upper())
# print(xa)
# print(za)
