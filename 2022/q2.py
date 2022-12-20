with open("q2.txt") as file:
    lines = file.readlines()

def shape(play):
    if play == "X":
        return 1
    elif play == "Y":
        return 2
    else:
        return 3

def outcome(opp, you):
    if (opp == "A" and you == "X") or (opp == 'B' and you == 'Y') or (opp == 'C' and you == 'Z'):
        return 3
    if (opp == "A" and you == "Y") or (opp == "B" and you == "Z") or (opp == "C" and you == "X"):
        return 6
    return 0

with open("q2.txt") as file:
    s = 0
    for line in file:
        opp, out = line.split()
        a = 'ABC'
        b = 'XYZ'
        if out == 'X':
            you = b[(a.index(opp) - 1) % 3]
        if out == 'Y':
            you = b[(a.index(opp)) % 3]
        if out == 'Z':
            you = b[(a.index(opp) + 1) % 3]

        s += shape(you) + outcome(opp, you)

    print(s)

