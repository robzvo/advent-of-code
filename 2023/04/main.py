
#parse scratchcard
def parse_numbers(card):
    winning_numbers = []
    numbers_to_play = []

    #separate numbers from garbage data
    split1 = card.split(':')

    #separate winning numbers from playing numbers
    numbers = split1[1].split('|')

    #separate numbers
    winning = numbers[0].strip().split(' ')
    playing = numbers[1].strip().split(' ')

    #only add winning values that are numberic
    for number in winning:
        if number.isnumeric():
            winning_numbers.append(int(number))

    #only add playing values that are numberic
    for number in playing:
        if number.isnumeric():
            numbers_to_play.append(int(number))

    return winning_numbers, numbers_to_play

#determine if numbers played are winning numbers
def process_numbers(winning_numbers,numbers_to_play):
    exponent = -1
    for number in numbers_to_play:
        if number in winning_numbers:
            exponent+=1

    return 2**exponent if exponent >=0 else 0

cards = None

#read input
with open("input.txt") as f:
    cards = f.read().strip().split('\n')


total_points = 0

#process each card
for card_index,card in enumerate(cards):
    winning_numbers, numbers_to_play = parse_numbers(card)
    total_points += process_numbers(winning_numbers, numbers_to_play)

print(total_points)
