import heapq
import sys

input = sys.stdin.readline


def solution(jewels: list[tuple[int, int]], bag_capacities: list[int]):
    jewels.sort()
    bag_capacities.sort()

    available_values: list[int] = []
    jewel_idx = 0
    stolen_value_sum = 0
    for capacity in bag_capacities:
        while jewel_idx < len(jewels) and jewels[jewel_idx][0] <= capacity:
            _, value = jewels[jewel_idx]
            heapq.heappush(available_values, -value)
            jewel_idx += 1

        if available_values:
            stolen_value_sum -= heapq.heappop(available_values)

    return stolen_value_sum


if __name__ == "__main__":
    N, K = map(int, input().split())
    jewels: list[tuple[int, int]] = []
    for _ in range(N):
        mass, value = map(int, input().split())
        jewels.append((mass, value))
    bag_capacities = [int(input()) for _ in range(K)]

    print(solution(jewels, bag_capacities))
