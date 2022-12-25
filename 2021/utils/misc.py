def top(n, nums):
    nums = list(nums)
    tops = []
    for _ in range(n):
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