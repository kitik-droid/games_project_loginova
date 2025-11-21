import random
from ..engine import run_game


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def play_prime_game():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(__import__(__name__, fromlist=['']), description)


if __name__ == "__main__":
    play_prime_game()
