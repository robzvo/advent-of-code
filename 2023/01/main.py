# read game input
input = None
with open("input.txt") as f:
    input = f.readlines()

#sum starts at zero
sum = 0

# for each line
for line_index,line in enumerate(input):
    
    #list for storing matches
    matches = []

    # for each character in the line
    for char_index, char in enumerate(line):
        if char.isdigit():
            matches.append(char)
    
    # at least one number was found
    if len(matches) > 0:
        sum = sum + int(matches[0]+matches[-1])

print(sum)