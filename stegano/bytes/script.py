from random import randint
data = open("task_source.txt", "r")
result = b""
for line in data:
    cnt = 0
    current = []
    for c in line:
        if c == '.':
            current.append(randint(128, 255))
        elif c == 'X':
            current.append(randint(65, 126))
        else:
            continue
        cnt += 1
    result += bytes(current)
open("file", "wb").write(result)