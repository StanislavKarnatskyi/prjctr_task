import random
import csv


def simulate_game() -> int:
    return random.randint(1, 1000)


with open('game_result/result.csv', mode='w') as file:
    fieldnames = ['Player name', 'Score']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(100):
        writer.writerow({'Player name': 'Smith', 'Score': simulate_game()})
        writer.writerow({'Player name': 'Edison', 'Score': simulate_game()})
        writer.writerow({'Player name': 'Reinhart', 'Score': simulate_game()})
        writer.writerow({'Player name': 'Handi', 'Score': simulate_game()})
        writer.writerow({'Player name': 'Mercy', 'Score': simulate_game()})
