is_operator = lambda s: s in ["*", "+"]
is_number = lambda s: s.isnumeric()
is_left_bracket = lambda s: s == "("
is_right_bracket = lambda s: s == ")"

evaluations = [
    [is_number, is_operator, is_number],
    [is_left_bracket, is_number, is_right_bracket],
    [is_left_bracket, is_number, is_operator, is_number, is_right_bracket],
]


def eval_and_merge(stack: list[str], length: int):
    return stack[:-length] + [str(eval("".join(stack[-length:])))]


def run(data: list[str], is_test: bool):
    sum = 0

    for line in data:
        tokens = line.replace("(", "( ").replace(")", " )").split(" ")

        stack = []

        for token in tokens:
            stack.append(token)

            while True:
                cleanup_performed = False

                for evaluation in evaluations:
                    if len(stack) >= len(evaluation) and all(
                        evaluation[i](stack[e]) for i, e in enumerate(range(-len(evaluation), 0))
                    ):
                        stack = eval_and_merge(stack, len(evaluation))
                        cleanup_performed = True

                if not cleanup_performed:
                    break

        sum += int(stack.pop())

    return sum
