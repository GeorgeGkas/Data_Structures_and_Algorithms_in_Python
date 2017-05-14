lines = []
while True:
    try:
        read_line = input()
        lines.append(read_line)
    except EOFError:
        break
