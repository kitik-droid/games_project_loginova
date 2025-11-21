import random
from ..engine import run_game


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [str(start + step * i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer


def play_progression_game():
    description = 'What number is missing in the progression?'
    run_game(__import__(__name__, fromlist=['']), description)


if __name__ == "__main__":
    play_progression_game()
