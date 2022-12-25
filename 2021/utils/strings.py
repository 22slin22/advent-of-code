from typing import *
from utils.lists import *

def str_before(pattern: str, string: str, include_match: bool = False) -> str:
    res = string.split(pattern)[0]
    return res + pattern if include_match else res
    
def str_after(pattern: str, string: str, include_match=False) -> str:
    res = string.split(pattern)[-1]
    return pattern +res if include_match else res

def splits(string: str, seps: Iterable[str]) -> list[str]:
    split_strs = [string]
    for sep in seps:
        split_strs = [s for split_str in split_strs for s in split_str.split(sep)]
    return split_strs

def ints(string: str, seps: Iterable[str] = [' ', ',', '\n']) -> list[int]:
    res = []
    for x in splits(string, seps):
        try:
            n = int(x)
            res.append(n)
        except ValueError:
            pass
    return res

def first_int(string: str, seps: Iterable[str] = [' ', ',', '\n']) -> int:
    for x in splits(string, seps):
        try:
            n = int(x)
            return n
        except ValueError:
            pass
    raise ValueError(f"There was no int in \"{string}\"")
    

def nats(string: str, seps: Iterable[str] = [' ', ',', '\n', '-']) -> list[int]:
    return [int(x) for x in splits(string, seps) if x.isdigit()]

def first_nat(string: str, seps: Iterable[str] = [' ', ',', '\n', '-']) -> int:
    return int(first(lambda n: n.isdigit(), splits(string, seps)))

def split_strip(string: str, sep: str = '\n') -> list[str]:
    return [line.strip() for line in string.strip().split(sep)]
    
def lines(string: str) -> list[str]:
    return split_strip(string)

lower_abc = 'abcdefghijklmnopqrstuvwxyz'
upper_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'