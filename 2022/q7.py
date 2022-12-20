from utils import *

with open("q7.txt") as file:

    dirs = defaultdict(int)

    path = []

    for line in file:
        match line.split():
            case ['$', 'cd', '..']:
                del path[-1]
            case ['$', 'cd', dir]:
                path.append(dir)
            case ['$', 'ls'] | ['dir', _]:
                pass
            case [size, file]:
                for pre in prefixes(path):
                    dirs["/".join(pre)] += int(size)

print(min(s for _,s in dirs.items() if s >= 30000000 - (70000000 - dirs["/"])))
