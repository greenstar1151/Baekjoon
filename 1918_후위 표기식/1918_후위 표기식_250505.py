def solution(inorder_expression: str) -> str:
    output: list[str] = []
    stack: list[str] = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    for tok in inorder_expression:
        if tok.isalpha():
            output.append(tok)
        elif tok == "(":
            stack.append(tok)
        elif tok == ")":
            # pop until "("
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # drop "("
        else:  # + - * /
            while (
                stack and stack[-1] != "(" and precedence[stack[-1]] >= precedence[tok]
            ):
                output.append(stack.pop())
            stack.append(tok)

    while stack:
        output.append(stack.pop())

    return "".join(output)


if __name__ == "__main__":
    inorder_expression = input()
    print(solution(inorder_expression))
