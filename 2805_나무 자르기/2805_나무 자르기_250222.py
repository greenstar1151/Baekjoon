import sys

input = sys.stdin.readline


def solution(tree_heights: list[int], tree_needs: int):
    tree_heights.sort(reverse=True)

    def get_cut_trees(cutoff_height: int):
        tree_amount = 0
        for tree in tree_heights:
            if tree <= cutoff_height:
                break
            tree_amount += tree - cutoff_height
        return tree_amount

    low, high = 0, max(tree_heights)
    mid = (low + high) // 2
    while low < mid:
        if get_cut_trees(mid) >= tree_needs:
            low = mid
        else:
            high = mid
        mid = (low + high) // 2

    return mid


if __name__ == "__main__":
    N, M = map(int, input().split())
    tree_heights = list(map(int, input().split()))
    print(solution(tree_heights, M))
