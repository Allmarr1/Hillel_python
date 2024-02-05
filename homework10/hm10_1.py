import json

def cal_sell_cource(cource, mul):
    """
    Розраховує та оновлює курси продажу на основі курсів

    Args:
        cource (_type_): Словник, що містить курси обміну валют.
        mul (_type_): Використовується для розрахунку нових курсів продажу.

    Returns:
        dict: Оновлені курси обміну валют з новими курсами продажу.
    """
    for curr_name in cource.keys():
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource



def get_curr_cource(path="data/currency_course.json"):
    """Зчитує та повертає курси обміну валют з файлу JSON.

    Args:
        path (str, optional): Шлях до файлу JSON із курсами обміну валют. Defaults to "data/currency_course.json".

    Returns:
        dict: Курси обміну валют.
    """

    with open(path, "r") as file:
        return json.load(file)


def get_curr_bank(path="data/bank.json"):
    """
    Зчитує та повертає інформацію про кількість банкнот різного номіналу, що є в наявності.

    Args:
        path (str, optional): Шлях до файлу JSON із інформацією про кількість банкнот різного номіналу, що є в наявності. Defaults to "data/bank.json".

    Returns:
        dict: Інформація про кількість банкнот різного номіналу, що є в наявності.
    """

    with open(path, "r") as file:
        return json.load(file)



def exchange(amount, cource, operation, old_curr, new_curr):
    """Виконує обмін валюти

    Args:
        amount (float): Сума для обміну.
        cource (dict): Словник із курсами обміну валют.
        operation (str): Вказує тип операції.
        old_curr (str): Валюта для обміну.
        new_curr (str): Потрібна валюта.

    Returns:
        float: Результат обміну валюти.
    """
    return amount * cource[old_curr][operation][new_curr]






def input_data(questions, prev_answers=[]):
    """
    Збирає введені дані на основі списку питань.


    Args:
        questions questions (list): Список словників з питаннями.
        prev_answers (list, optional): Список попередніх відповідей. Defaults to [].

    Returns:
    list: Список відповідей користувача.
    """
    answers = []
    quest_index = 0

    while quest_index < len(questions):
        item = questions[quest_index]

        if item["question"] is None:
            answers.append(item.get("fixture"))
        else:
            value = input(item["question"])

            if value.lower() == "back":
                if quest_index > 0:
                    quest_index -= 1
                    answers.pop()
                else:
                    print("Не можна йти назад далі. Ви на початку.")
                continue

            value = item["func"](value)

            if value == "reset":
                return input_data(questions)

            answers.append(value)
            quest_index += 1

    return answers