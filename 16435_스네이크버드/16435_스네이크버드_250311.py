def solution(initial_height: int, fruits: list[int]):
    height = initial_height
    for h in sorted(fruits):
        if h <= height:
            height += 1
        else:
            break

    return height


if __name__ == "__main__":
    N, L = map(int, input().split())
    fruit_heights = list(map(int, input().split()))
    print(solution(L, fruit_heights))
