import time

idx = 10
# ["\\", "|", "/", "-"]
while idx > 0:
    for dx in [">", "->", "-->", "--->", " ", "  ", "   ", "    "]:
        print("This is loading", dx, end="\r")
        time.sleep(0.25)
    idx -= 1