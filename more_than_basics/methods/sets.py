xa = {1, 2, 3, 4, 5}
pp = {1, 2, 3, 4, 5, 6}



# pp = xa & pp # xa = pp - xa
pp = xa.update(pp)

print("XA:\n", xa, "\nPP:\n", pp)
