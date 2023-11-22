# FSI Búsquedas

In search problems, we can employ a strategy known as branch and bound. This strategy belongs to uninformed search, meaning the only information available about the problem is its initial state and its goal state. With this strategy, we aim to find the optimal solution more efficiently by attempting to reduce the search space.
To carry out the implementation of this strategy in the code, an open list will be used to order the partial paths based on the accumulated cost of each.

Besides employing branch and bound, a heuristic will be used to guide the search, reduce the search space, enhance execution time, and optimize the solution.

For this project, the problem of Romania will be employed to apply the implementation of branch and bound. This is a famous problem in artificial intelligence and heuristic search involving finding the shortest route between cities on a map of Romanian roads.

![imagen](https://github.com/0xM4rc/FSI_busquedas/assets/140960974/95d150e8-6af7-411f-aa35-6a791b907f4a.png)

# Data structures

Datas structrure is a storage that is used to store and manage data. 
In the base code, the stack and FIFO queue structures are provided as a starting point. These structures are used for the implementation of depth-first search (DFS) and breadth-first search (BFS), respectively.

## Stack

![imagen](https://github.com/0xM4rc/FSI_busquedas/assets/140960974/c2925024-8cdd-4837-ae16-baf84a05a6fe.png)  
Source: [wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/e/e4/Lifo_stack.svg)

## FIFO

![imagen](https://github.com/0xM4rc/FSI_busquedas/assets/140960974/78d9aae7-e179-4b6c-a6e7-30089ddb5069)  
Source: [wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/d/d3/Fifo_queue.png)

# Implementation

## Branch and Bound

Branch and bound (BB, B&B, or BnB) is a method for solving optimization problems by breaking them down into smaller sub-problems and using a bounding function to eliminate sub-problems that cannot contain the optimal solution.

```python
class BnBQueue(Queue):
    """ Branch and Bound Queue"""

    def __init__(self):
        self.A = []
        self.start = 0

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        def sort_key(item):
            return item.path_cost

        self.A.extend(items)
        self.A.sort(key=sort_key, reverse=True)

    def pop(self):
        return self.A.pop()
```

```python
class BnBHeuristicQueue(Queue):
    """ Branch and Bound Queue with Heuristic """

    def __init__(self, problem):
        self.A = []
        self.start = 0
        self.problem = problem

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        def custom_sort_key(n):
            return n.path_cost + self.problem.h(n)

        self.A.extend(items)
        self.A.sort(key=custom_sort_key, reverse=True)

    def pop(self):
        return self.A.pop()
```
