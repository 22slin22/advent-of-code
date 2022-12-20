with open("q6.txt") as file:
    line = file.readline()

    for i in range(14, len(line)):
        if len(set(line[i-14:i])) == 14:
            print(i)
            break