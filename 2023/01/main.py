DICTIONARY = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "zero" : 0
}

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
        
        # part 2 looking for word literals of numbers
        for key,value in DICTIONARY.items():
            
            #literal exists at this position in the string
            if line[char_index:].startswith(key):
                matches.append(str(value))
    
    # at least one number was found
    if len(matches) > 0:
        sum = sum + int(matches[0]+matches[-1])

print(sum)