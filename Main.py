"""
projekt_2a.py: Druhý projekt do Engeto Online Python Akademie

author: Jan Koppan
email: jan.koppan@seznam.cz
"""
import random
import time

# Funkce pro generování tajného 4místného čísla s unikátními číslicemi
def generate_secret_number():
    digits = list('123456789')  # první číslice nesmí být 0
    first_digit = random.choice(digits)
    digits = list('0123456789')
    digits.remove(first_digit)
    other_digits = random.sample(digits, 3)
    return first_digit + ''.join(other_digits)

# Funkce pro vyhodnocení pokusu – vrátí počet bulls (správné číslo i pozice) a cows
def evaluate_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

# Funkce pro kontrolu platnosti vstupu
def is_valid_guess(guess):
    return (
        guess.isdigit() and
        len(guess) == 4 and
        guess[0] != '0' and
        len(set(guess)) == 4
    )

# Funkce pro jednotné/množné číslo
def plural(n, word):
    return f"{n} {word}" + ("s" if n != 1 else "")

# Funkce pro odehrání jedné hry
def play_game():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    secret = generate_secret_number()
    guesses = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number:\n>>> ").strip()

        # Kontrola platnosti vstupu
        if not is_valid_guess(guess):
            print("Invalid input! Enter a 4-digit number with unique digits")
            print("that doesn't start with 0.")
            continue

        guesses += 1
        bulls, cows = evaluate_guess(secret, guess)

        if bulls == 4:
            end_time = time.time()
            duration = end_time - start_time
            minutes = int(duration) // 60
            seconds = int(duration) % 60
            print(f"Correct, you've guessed the right number")
            print(f"in {guesses} guesses!")
            print(f"Time taken: {minutes:02}:{seconds:02} minutes")
            print("-" * 47)
            print("That's amazing!\n")
            return guesses, duration
        else:
            bull_word = plural(bulls, 'bull')
            cow_word = plural(cows, 'cow')
            print(f"{bull_word}, {cow_word}")
            print("-" * 47)

# Funkce pro výpočet průměrných statistik
def show_stats(stats):
    if not stats:
        print("No games played yet.")
        return

    total_games = len(stats)
    total_guesses = sum(g for g, _ in stats)
    total_time = sum(t for _, t in stats)

    avg_guesses = total_guesses / total_games
    avg_time = total_time / total_games

    minutes = int(avg_time) // 60
    seconds = int(avg_time) % 60

    print("Games played:", total_games)
    print(f"Average guesses per game: {avg_guesses:.2f}")
    print(f"Average time: {minutes:02}:{seconds:02}")
    print("=" * 47)

# Hlavní smyčka programu
def main():
    all_game_stats = []  # seznam statistik

    while True:
        guesses, duration = play_game()
        all_game_stats.append((guesses, duration))

        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            break

    show_stats(all_game_stats)

if __name__ == "__main__":
    main()
