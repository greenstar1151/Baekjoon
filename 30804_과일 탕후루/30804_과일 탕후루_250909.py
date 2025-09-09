class FruitCounter:
    def __init__(self, fruit_type_count: int = 10):
        self.distinct_count = 0
        self.counter = [0] * fruit_type_count

    def add(self, f_id: int):
        if self.counter[f_id] == 0:
            self.distinct_count += 1
        self.counter[f_id] += 1

    def remove(self, f_id: int):
        self.counter[f_id] -= 1
        if self.counter[f_id] == 0:
            self.distinct_count -= 1


def solution(fruits: list[int]):
    peak_len = 0
    front_handle = 0
    fruit_counter: FruitCounter = FruitCounter()
    for i in range(len(fruits)):
        if fruit_counter.distinct_count < 3:
            fruit_counter.add(fruits[i])
            if fruit_counter.distinct_count <= 2:
                peak_len = max(peak_len, i - front_handle + 1)
        while fruit_counter.distinct_count > 2:
            fruit_counter.remove(fruits[front_handle])
            front_handle += 1
            peak_len = max(peak_len, i - front_handle + 1)

    return peak_len


if __name__ == "__main__":
    N = int(input())
    fruits = list(map(int, input().split()))
    print(solution(fruits))
