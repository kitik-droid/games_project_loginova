import random
from ..engine import run_game


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(find_gcd(num1, num2))
    return question, correct_answer


def play_gcd_game():
    description = 'Find the greatest common divisor of given numbers.'
    run_game(__import__(__name__, fromlist=['']), description)


if __name__ == "__main__":
    play_gcd_game()
