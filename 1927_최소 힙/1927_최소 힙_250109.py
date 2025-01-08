import sys


class MinHeap:
    def __init__(self):
        self.binary_tree: list[int] = [-1]
        self.size = 0

    def top(self):
        if self.size == 0:
            return 0
        return self.binary_tree[1]

    def _bubble_up(self, index: int):
        while index > 1:
            parent_idx = index // 2
            if self.binary_tree[parent_idx] > self.binary_tree[index]:
                self.binary_tree[parent_idx], self.binary_tree[index] = (
                    self.binary_tree[index],
                    self.binary_tree[parent_idx],
                )
                index = parent_idx
            else:
                break

    def push(self, e: int):
        self.binary_tree.append(e)
        self.size += 1
        self._bubble_up(self.size)

    def _sift_down(self, index: int):
        while index <= self.size:
            smallest = index
            left = 2 * index
            right = 2 * index + 1

            if (
                left <= self.size
                and self.binary_tree[left] < self.binary_tree[smallest]
            ):
                smallest = left
            if (
                right <= self.size
                and self.binary_tree[right] < self.binary_tree[smallest]
            ):
                smallest = right

            if smallest == index:
                break

            self.binary_tree[index], self.binary_tree[smallest] = (
                self.binary_tree[smallest],
                self.binary_tree[index],
            )
            index = smallest

    def pop(self):
        if self.size == 0:
            return 0
        self.binary_tree[1], self.binary_tree[-1] = (
            self.binary_tree[-1],
            self.binary_tree[1],
        )
        self.size -= 1
        v = self.binary_tree.pop()
        if self.size > 0:
            self._sift_down(1)
        return v


def solution(operations: list[int]):
    min_heap = MinHeap()
    for op in operations:
        if op == 0:
            yield min_heap.pop()
        else:
            min_heap.push(op)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    operations = list(map(int, sys.stdin.read().rstrip().split("\n")))
    for output in solution(operations):
        sys.stdout.write(f"{output}\n")


# # Solution using Built-in function
# import heapq
# import sys

# N = int(sys.stdin.readline())
# operations = list(map(int, sys.stdin.read().rstrip().split("\n")))
# heap: list[int] = []
# for op in operations:
#     if op == 0:
#         if not heap:
#             sys.stdout.write(f"{0}\n")
#         else:
#             sys.stdout.write(f"{heapq.heappop(heap)}\n")
#     else:
#         heapq.heappush(heap, op)
