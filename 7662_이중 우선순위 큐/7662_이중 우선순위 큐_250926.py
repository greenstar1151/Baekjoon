import heapq

import sys

input = sys.stdin.readline


# from functools import total_ordering
# from typing import Any, Self


# @total_ordering
# class LinkedComparable:
#     def __init__(self, n: int, link: list[bool]):
#         self.node = (n, link)

#     @property
#     def value(self):
#         return self.node[0]

#     @property
#     def is_dirty(self):
#         return len(self.node[1]) != 0

#     def mark_dirty(self):
#         self.node[1].append(True)

#     def __lt__(self, other: Self):
#         return self.node[0] < other.node[0]

#     def __eq__(self, other: Any):
#         if isinstance(other, LinkedComparable):
#             return self.node[0] == other.node[0]
#         raise NotImplementedError


# class DualPriorityQueue:
#     def __init__(self):
#         self.min_q: list[LinkedComparable] = []
#         self.max_q: list[LinkedComparable] = []
#         self.clean = True

#     def push(self, n: int):
#         self.clean = False
#         is_dirty: list[bool] = []
#         heapq.heappush(self.min_q, LinkedComparable(n, is_dirty))
#         heapq.heappush(self.max_q, LinkedComparable(-n, is_dirty))

#     def pop_min(self) -> int | None:
#         while self.min_q:
#             e = heapq.heappop(self.min_q)
#             if not e.is_dirty:
#                 e.mark_dirty()
#                 return e.value

#         return None

#     def pop_max(self) -> int | None:
#         while self.max_q:
#             e = heapq.heappop(self.max_q)
#             if not e.is_dirty:
#                 e.mark_dirty()
#                 return e.value
#         return None

#     def vacuum(self):
#         if self.min_q:
#             self.min_q = [e for e in self.min_q if not e.is_dirty]
#         if self.max_q:
#             self.max_q = [e for e in self.max_q if not e.is_dirty]

#         self.clean = True

#     def max(self):
#         if not self.clean:
#             self.vacuum()
#         return heapq.nlargest(1, self.min_q)[0].value

#     def min(self):
#         if not self.clean:
#             self.vacuum()
#         return heapq.nsmallest(1, self.min_q)[0].value

#     def is_empty(self):
#         if not self.clean:
#             self.vacuum()


class DualPriorityQueue:
    def __init__(self) -> None:
        self.min_q: list[tuple[int, list[bool]]] = []
        self.max_q: list[tuple[int, list[bool]]] = []
        self.clean = True

    def push(self, n: int):
        self.clean = False
        is_dirty: list[bool] = []
        heapq.heappush(self.min_q, (n, is_dirty))
        heapq.heappush(self.max_q, (-n, is_dirty))

    def pop_min(self) -> int | None:
        while self.min_q:
            e = heapq.heappop(self.min_q)
            if len(e[1]) == 0:
                e[1].append(True)
                return e[0]

        return None

    def pop_max(self) -> int | None:
        while self.max_q:
            e = heapq.heappop(self.max_q)
            if len(e[1]) == 0:
                e[1].append(True)
                return -e[0]
        return None

    def vacuum(self):
        if self.min_q:
            self.min_q = [e for e in self.min_q if len(e[1]) == 0]
        if self.max_q:
            self.max_q = [e for e in self.max_q if len(e[1]) == 0]

        self.clean = True

    def max(self):
        if not self.clean:
            self.vacuum()
        return heapq.nlargest(1, self.min_q)[0][0]

    def min(self):
        if not self.clean:
            self.vacuum()
        return heapq.nsmallest(1, self.min_q)[0][0]

    def is_empty(self):
        if not self.clean:
            self.vacuum()
        return len(self.min_q) == 0


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        K = int(input())
        dpq = DualPriorityQueue()
        for _ in range(K):
            op, arg = input().split()
            if op == "I":
                dpq.push(int(arg))
            elif op == "D":
                if arg == "1":
                    dpq.pop_max()
                elif arg == "-1":
                    dpq.pop_min()

        if dpq.is_empty():
            print("EMPTY")
        else:
            print(f"{dpq.max()} {dpq.min()}")
