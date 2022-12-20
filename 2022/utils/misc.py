def top(n, nums):
    nums = list(nums)
    tops = []
    for _ in range(n):
        if len(nums) == 0:
            return tops
        m = max(nums)
        tops.append(m)
        nums.remove(m)
    return tops

def bottom(n, nums):
    nums = list(nums)
    tops = []
    for _ in range(n):
        m = min(nums)
        tops.append(m)
        nums.remove(m)
    return tops

        
def prod(iter):
    p = 1
    for x in iter:
        p *= x
    return p

def memorize(f):
    mem = {}
    
    def mem_f(*args):
        if args in mem:
            return mem[args]
        else:
            res = f(*args)
            mem[args] = res
            return res

    return mem_f