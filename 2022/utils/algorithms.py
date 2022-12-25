from typing import *
from queue import Queue, PriorityQueue, LifoQueue
from dataclasses import dataclass, field, astuple

T = TypeVar('T')
S = TypeVar('S')

def recreate_path(pred: dict[T, T], goal: T) -> list[T]:
    path = [goal]
    while pred[goal] is not None:
        goal = pred[goal]
        path.append(goal)
    path.reverse()
    return path

def bfs_find(start: T, succ: Callable[[T], Iterable[T]], goal: T | Callable[[T], bool]) -> list[T]:
    pred = {}
    
    queue = Queue()
    queue.put(start)
    pred[start] = None

    while not queue.empty():
        cur = queue.get()

        # print(cur)

        for s in succ(cur):
            if s not in pred:
                pred[s] = cur

                if callable(goal):
                    if goal(s):
                        return recreate_path(pred, s)
                elif s == goal:
                    return recreate_path(pred, s)

                queue.put(s)

def bfs(start: T, succ: Callable[[T], Iterable[T]], do: Callable[[T], Any]):
    queue = Queue()
    queue.put(start)
    
    done = {start}

    while not queue.empty():
        cur = queue.get()

        do(cur)        

        for s in succ(cur):
            if s not in done:
                done.add(s)
                queue.put(s)
    

def dfs_find(start: T, succ: Callable[[T], Iterable[T]], goal: T | Callable[[T], bool]) -> list[T]:
    pred = {}
    
    stack = [start]
    pred[start] = None

    while not len(stack.empty()):
        cur = stack[-1]
        del stack[-1]

        for s in succ(cur):
            if s not in pred:
                pred[s] = cur

                if callable(goal):
                    if goal(s):
                        return recreate_path(pred, s)
                elif s == goal:
                    return recreate_path(pred, s)

                stack.append(s)

def bfs(start: T, succ: Callable[[T], Iterable[T]], do: Callable[[T], Any]):
    q = LifoQueue()
    q.put(start)

    done = {start}

    while not q.empty():
        cur = q.get()
        
        do(cur)

        for s in succ(cur):
            if s not in done:
                done.add(s)
                q.put(s)
                

@dataclass(order=True)
class PrioItem:
    priority: Any
    item: Any=field(compare=False)

    def __iter__(self):
        return iter(astuple(self))

def a_star(start: T, succ: Callable[[T], Iterable[tuple[T,Any]]], heuristic: Callable[[T], Any],goal: T | Callable[[T], bool]) -> list[T]:
    pred = {}
    pred[start] = None
    
    done = set()

    min_cost = {start: 0}

    queue = PriorityQueue()
    queue.put(PrioItem(0, start))

    while not queue.empty():
        _, cur = queue.get()
        if cur in done:
            continue

        done.add(cur)

        if callable(goal):
            if goal(cur):
                return recreate_path(pred, cur), min_cost[cur]
        elif cur == goal:
            return recreate_path(pred, cur), min_cost[cur]

        for s, dist in succ(cur):
            if s not in done:
                new_f = min_cost[cur] + dist
                if s not in min_cost or new_f < min_cost[s]:
                    pred[s] = cur
                    min_cost[s] = new_f
                    queue.put(PrioItem(new_f + heuristic(s), s))