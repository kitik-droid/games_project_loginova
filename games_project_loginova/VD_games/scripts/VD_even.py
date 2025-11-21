import random

def generate_round():
    number = random.randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return number, correct_answer

def play_even_game():
    from ..engine import run_game
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(__import__(__name__, fromlist=['']), description)

if __name__ == "__main__":
    play_even_game()
