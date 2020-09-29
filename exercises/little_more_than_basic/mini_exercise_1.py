# 1. Reverse a list of 5 numbers.
# _list = [10, 20, 30, 40, 50]
# Output: [50, 40, 30, 20, 10] or print the values.
_list = [10, 20, 30, 40, 50]
for idx in range(len(_list) - 1, -1, -1):
  print(_list[idx], end=" ")


# 2. Reverse a 6-digit number without converting it to string.
# Take an integer input from user and print the reverse.
inp = int(input("Enter: "))

for _ in range(len(str(inp))):
  ret = inp % 10
  inp //= 10
  print(ret, end="")
print()
