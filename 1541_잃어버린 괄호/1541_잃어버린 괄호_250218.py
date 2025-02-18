expression = input()
intermediate = [sum(map(int, part.split("+"))) for part in expression.split("-")]
print(intermediate[0] - sum(intermediate[1:]))
