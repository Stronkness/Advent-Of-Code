def calculate_points(winning_numbers, your_numbers):
    points = 0
    for num in winning_numbers:
        if num in your_numbers:
            points += 1

    return 2 ** (points - 1) if points > 0 else 0

def main():
    cards = open('input', 'r').read().splitlines()

    total_points = 0
    for card in cards:
        winning, yours = card.split('|')
        _, winning_numbers = winning.split(': ')
        winning_numbers = winning_numbers.split()
        your_numbers = yours.split()

        points = calculate_points(winning_numbers, your_numbers)
        total_points += points

    print(total_points)

if __name__ == "__main__":
    main()
