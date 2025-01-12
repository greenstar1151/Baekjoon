if __name__ == "__main__":
    N, T = map(int, input().split())
    X = input()
    max_val = -1
    hop_size = 2 ** (N - T)
    for i in range(0, 2**N, hop_size):
        tanosu = int(X[i : i + hop_size])
        if tanosu > max_val:
            max_val = tanosu

    print(max_val)
