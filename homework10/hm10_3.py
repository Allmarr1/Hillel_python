def input_data(questions, prev_answers=[]):
    answers = []
    i = 0
    while i < len(questions):
        item = questions[i]
        if item["question"] == None:
            answers.append(item.get("fixture"))
            i += 1
        else:
            value = input(item["question"])
            value = item["func"](value)
            if value == "back":
                if i > 0:
                    i -= 1
                    answers.pop()
                continue
            if value == "reset":
                return input_data(questions)
            answers.append(value)
            i += 1
    return answers