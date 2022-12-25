from typing import *
from queue import Queue

T = TypeVar('T')

def recreate_path(pred: dict[T, T], goal: T) -> list[T]:
    path = [goal]
    while pred[goal] is not None:
        goal = pred[goal]
        path.append(goal)
    path.reverse()
    return path

def bfs(start: T, succ: Callable[[T], list[T]], goal: T | Callable[[T], bool]) -> list[T]:
    pred = {}
    
    queue = Queue()
    queue.put(start)
    pred[start] = None

    while not queue.empty():
        cur = queue.get()

        for s in succ(cur):
            if s not in pred:
                pred[s] = cur

                if callable(goal):
                    if goal(s):
                        return recreate_path(pred, s)
                elif s == goal:
                    return recreate_path(pred, s)

                queue.put(s)

def dfs(start: T, succ: Callable[[T], list[T]], goal: T | Callable[[T], bool]) -> list[T]:
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
                