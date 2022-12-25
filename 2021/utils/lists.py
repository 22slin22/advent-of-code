from typing import *

T = TypeVar('T')

def prefixes(seq: Iterable[T], include_empty: bool = False) -> list[T]:
    return [seq[0:i] for i in range(0 if include_empty else 1, len(seq)+1)]

def dedup(seq: Iterable[T]) -> list[T]:
    return [x for i,x in enumerate(seq) if x not in seq[:i]]

def take_while(pred: Callable[[T], bool], seq: Iterable[T], include_breaking: bool = False) -> list[T]:
    res = []
    for x in seq:
        if pred(x):
            res.append(x)
        else:
            if include_breaking:
                res.append(x)
            break
    return res
    
def drop_while(pred: Callable[[T], bool], seq: Iterable[T]) -> list[T]:
    res = []
    for x in seq:
        if not pred(x):
            res.append(x)
        else:
            break
    return res

def first(pred: Callable[[T], bool], seq: Iterable[T]) -> T:
    for s in seq:
        if pred(s):
            return s
    raise ValueError(f"No such element found in sequence {seq}")