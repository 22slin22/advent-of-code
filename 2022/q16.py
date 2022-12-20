from utils import *

with open('q16.txt') as file:
    file = file.read()

succ = defaultdict(lambda: defaultdict(int))
rate = {}

for line in lines(file):
    words = line.split()
    v = words[1]
    rate[v] = first_nat(words[4], seps='=;')
    for u in ''.join(words[9:]).split(','):
        succ[v][u] = 1
            
def heuristic(s):
    (minute,v,e,_,_,opened) = s
    return -sum(top(minute, (r for v,r in rate.items() if v not in opened))) * (minute-1)

def succ_states(s):
    (minute,v,e,opened) = s
    l = []
    if v not in opened:
        if v != e and e not in opened:
            l.append(((minute-1,v,e,tuple(list(opened) + [v,e])), - rate[v] * (minute-1) - rate[e] * (minute-1)))
        else:
            for f in succ[e]:
                l.append(((minute-1,v,f,tuple(list(opened) + [v])), - rate[v] * (minute-1)))
    if e not in opened:
        for u in succ[v]:
            l.append(((minute-1,u,e,tuple(list(opened) + [e])), - rate[e] * (minute-1)))
    for u in succ[v]:
        for f in succ[e]:
            l.append(((minute-1,u,f,opened), 0))

    # if s == (25,'DD','II',()):
    #     print('succs', l)

    return l

def goal(s):
    return s[0] <= 0

# print(a_star((26, 'AA', 'AA', ()), succ_states, heuristic, goal)[1])

for v,r in rate.items():
    if r == 0 and v != 'AA':
        for u, usucc in succ.items():
            if v in usucc:
                for w,d in succ[v].items():
                    if w in usucc:
                        usucc[w] = min(usucc[w], usucc[v] + d)
                    else:
                        usucc[w] = usucc[v] + d
                del usucc[v]

def succ_states2(s):
    (minute,v,e,cool_v,cool_e,opened) = s
    todo = []

    if v not in opened and rate[v] > 0 and cool_v == 0:
        if cool_e > 0:
            todo.append(((minute-1, v, e, cool_v, cool_e-1, tuple(sorted(list(opened) + [v]))), - rate[v] * (minute-1)))
        else:
            if e != v and e not in opened:
                todo.append(((minute-1, v, e, 0, 0, tuple(sorted(list(opened) + [e,v]))), - rate[v] * (minute-1) - rate[e] * (minute-1)))    
            for f,d in succ[e].items():
                todo.append(((minute-1, v, f, 0, d-1, tuple(sorted(list(opened) + [v]))), - rate[v] * (minute-1)))

    if e not in opened and cool_e == 0:
        if cool_v > 0:
            todo.append(((minute-1, v, e, cool_v-1, 0, tuple(sorted(list(opened) + [e]))), - rate[e] * (minute-1)))
        else:
            for u,d in succ[v].items():
                todo.append(((minute-1, v, e, d-1, 0, tuple(sorted(list(opened) + [e]))), - rate[e] * (minute-1)))

    if cool_v <= 0:
        if cool_e <= 0:
            for u,du in succ[v].items():
                for f,df in succ[e].items():
                    m = min(du, df)
                    todo.append(((minute-m, u, f, du-m, df-m, opened), 0))
        else:
            for u,du in succ[v].items():
                m = min(du, cool_e)
                todo.append(((minute-m, u, e, du-m, cool_e-m, opened), 0))
    else:
        for f,df in succ[e].items():
            m = min(df, cool_v)
            todo.append(((minute-m, v, f, cool_v-m, df-m, opened), 0))

    # ss = set()

    # for ((m,v,e,cv,ce,opened), val) in todo:
    #     if cv <= ce:
    #         p = ((m,v,e,cv,ce,opened), val)
    #     else:
    #         p = ((m,e,v,ce,cv,opened), val)
    #     ss.add(p)

    return todo

print(a_star((26, 'AA', 'AA', 0, 0, ()), succ_states2, heuristic, goal)[1])

exit(0)

opened = set()

max_rate = max(rate.values())



def solve(minute, v, val, max_p):
    if minute <= 0:
        if val > max_p:
            print(val)
        return val
    if val + sum(top(minute//2, (r for v,r in rate.items() if v not in opened))) * (minute - 1) <= max_p:
        return val
    if v not in opened and rate[v] > 0:
        opened.add(v)
        max_p = max(max_p, solve(minute-1, v, val + rate[v] * (minute-1), max_p))
        opened.remove(v)
    for u,d in succ[v].items():
        if d == 0:
            print('OOF')
        max_p = max(max_p, solve(minute-d,u,val,max_p))
    return max_p

sol = None

def solve2(minute, v, e, cool_v, cool_e, val, max_p, seq):
    if minute <= 0:
        if val > max_p:
            print(val)
        return val

    if cool_e > 0 and cool_v > 0:
        m = min(cool_e, cool_v)
        return solve2(minute-m, v, e, cool_e-m, cool_e-m, val, max_p, seq)

    # max_p = max(val, max_p)
    if val + sum(top(minute//2, (r for v,r in rate.items() if v not in opened))) * (minute - 1) <= max_p:
        return val

    if v not in opened and rate[v] > 0 and cool_v == 0:
        # seq.append(str(27 - minute) + ': You open ' + str(v))
        opened.add(v)
        if cool_e > 0:
            max_p = max(max_p, solve2(minute-1, v, e, cool_v, cool_e-1, val + rate[v] * (minute-1), max_p, seq))
        else:
            if e not in opened:
                opened.add(e)
                # seq.append(str(27 - minute) + ': Elephant opens ' + str(e))
                max_p = max(max_p, solve2(minute-1, v, e, 0, 0, val + rate[v] * (minute-1) + rate[e] * (minute-1), max_p, seq))    
                opened.remove(e)
                # del seq[-1]
            for f,d in succ[e].items():
                # seq.append(str(27 - minute) + ': Elephant to ' + str(f))
                max_p = max(max_p, solve2(minute-1, v, f, 0, d-1, val + rate[v] * (minute-1), max_p, seq))
                # del seq[-1]
        opened.remove(v)
        # del seq[-1]

    if e not in opened and cool_e == 0:
        opened.add(e)
        # seq.append(str(27 - minute) + ': Elephant opens ' + str(e))
        if cool_v > 0:
            max_p = max(max_p, solve2(minute-1, v, e, cool_v-1, 0, val + rate[e] * (minute-1), max_p, seq))
        else:
            for u,d in succ[v].items():
                # seq.append(str(27 - minute) + ': You to ' + str(u))
                max_p = max(max_p, solve2(minute-1, v, e, d-1, 0, val + rate[e] * (minute-1), max_p, seq))
                # del seq[-1]
        opened.remove(e)
        # del seq[-1]

    if cool_v <= 0:
        if cool_e <= 0:
            for u,du in succ[v].items():
                # seq.append(str(27 - minute) + ': You to ' + str(u))
                for f,df in succ[e].items():
                    # seq.append(str(27 - minute) + ': Elephant to ' + str(f))
                    m = min(du, df)
                    max_p = max(max_p, solve2(minute-m, u, f, du-m, df-m, val, max_p, seq))
                    # del seq[-1]
                # del seq[-1]
        else:
            for u,du in succ[v].items():
                # seq.append(str(27 - minute) + ': You to ' + str(u))
                m = min(du, cool_e)
                max_p = max(max_p, solve2(minute-m, u, e, du-m, cool_e-m, val, max_p, seq))
                # del seq[-1]
    else:
        for f,df in succ[e].items():
            # seq.append(str(27 - minute) + ': Elephant to ' + str(f))
            m = min(df, cool_v)
            max_p = max(max_p, solve2(minute-m, v, f, cool_v-m, df-m, val, max_p, seq))
            # del seq[-1]

    # for u,d in succ[v].items():
    #     max_p = max(max_p, solve2(minute-d,u,val,max_p))
    return max_p

def solve3(minute, v, e, cool_v, cool_e, val, max_p):
    if val > max_p:
        print(val)
        if minute <= 0:
            return val
        max_p = val

    if minute <= 0:
        return val
    
    # if minute <= 0:
    #     if val > max_p:
    #         print(val)
    #     return val

    if cool_e > 0 and cool_v > 0:
        m = min(cool_e, cool_v)
        return solve3(minute-m, v, e, cool_e-m, cool_e-m, val, max_p)

    if val + sum(top(minute//2, (r for v,r in rate.items() if v not in opened))) * (minute - 1) <= max_p:
        return val

    todo = []

    if v not in opened and rate[v] > 0 and cool_v == 0:
        if cool_e > 0:
            todo.append((minute-1, v, e, cool_v, cool_e-1, val + rate[v] * (minute-1), [v]))
        else:
            if e != v and e not in opened:
                todo.append((minute-1, v, e, 0, 0, val + rate[v] * (minute-1) + rate[e] * (minute-1), [v,e]))    
            for f,d in succ[e].items():
                todo.append((minute-1, v, f, 0, d-1, val + rate[v] * (minute-1), [v]))

    if e not in opened and cool_e == 0:
        if cool_v > 0:
            todo.append((minute-1, v, e, cool_v-1, 0, val + rate[e] * (minute-1), [e]))
        else:
            for u,d in succ[v].items():
                todo.append((minute-1, v, e, d-1, 0, val + rate[e] * (minute-1), [e]))

    if cool_v <= 0:
        if cool_e <= 0:
            for u,du in succ[v].items():
                for f,df in succ[e].items():
                    m = min(du, df)
                    todo.append((minute-m, u, f, du-m, df-m, val, []))
        else:
            for u,du in succ[v].items():
                m = min(du, cool_e)
                todo.append((minute-m, u, e, du-m, cool_e-m, val, []))
    else:
        for f,df in succ[e].items():
            m = min(df, cool_v)
            todo.append((minute-m, v, f, cool_v-m, df-m, val, []))

    todo.sort(key = lambda p: (1 if p[1] not in opened else 0) + (1 if p[2] not in opened else 0), reverse=True)
    todo.sort(key = lambda p: p[5], reverse=True)

    for (m,v,e,cv,ce,val,os) in todo:
        for o in os:
            opened.add(o)
        max_p = max(max_p, solve3(m, v, e, cv, ce, val, max_p))
        for o in os:
            opened.remove(o)

    return max_p
            

# print(solve(30, 'AA', 0, 0))

print(solve3(26, 'AA', 'AA', 0, 0, 0, 0))

for s in sol:
    print(s)