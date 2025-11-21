import random
from ..engine import run_game


def calculate_expression(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        raise ValueError("Unknown operator")


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate_expression(num1, num2, operator))
    return question, correct_answer


def play_calc_game():
    description = 'What is the result of the expression?'
    run_game(__import__(__name__, fromlist=['']), description)


if __name__ == "__main__":
    play_calc_game()
