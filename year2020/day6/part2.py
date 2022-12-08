def all_yes_answers(yes_answers, people_in_group):
    return [answer for answer, count in yes_answers.items() if count == people_in_group]


def run(data: list[str], raw_data: list[str]):
    groups = []

    yes_answers = {}
    people_in_group = 0
    for line in data:
        if len(line) == 0:
            groups.append(all_yes_answers(yes_answers, people_in_group))
            yes_answers = {}
            people_in_group = 0
            continue
        for answer in line:
            if answer not in yes_answers:
                yes_answers[answer] = 0
            yes_answers[answer] += 1
        people_in_group += 1
    groups.append(all_yes_answers(yes_answers, people_in_group))

    return sum([len(group) for group in groups])
