import sys
from typing import Any, Callable

input = sys.stdin.readline
print = sys.stdout.write

Tree = dict[str, tuple[str, str]]
TraversalCallback = Callable[[str], Any]


def traversal(
    tree: Tree,
    start: str,
    pre_callback: TraversalCallback | None = None,
    in_callback: TraversalCallback | None = None,
    post_callback: TraversalCallback | None = None,
):
    pre_callback = (lambda x: ...) if pre_callback is None else pre_callback
    in_callback = (lambda x: ...) if in_callback is None else in_callback
    post_callback = (lambda x: ...) if post_callback is None else post_callback

    def _traversal(v: str):
        pre_callback(v)
        _traversal(tree[v][0]) if tree[v][0] != "." else None
        in_callback(v)
        _traversal(tree[v][1]) if tree[v][1] != "." else None
        post_callback(v)

    _traversal(start)


def solution(tree: Tree):
    traversal(tree, "A", pre_callback=lambda v: print(v))
    print("\n")
    traversal(tree, "A", in_callback=lambda v: print(v))
    print("\n")
    traversal(tree, "A", post_callback=lambda v: print(v))
    print("\n")


if __name__ == "__main__":
    N = int(input())
    tree: Tree = dict()
    for _ in range(N):
        parent, child_l, child_r = input().split()
        tree[parent] = (child_l, child_r)
    solution(tree)
