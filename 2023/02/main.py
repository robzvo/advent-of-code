MAX_CUBES={
    "red": 12,
    "blue": 14,
    "green": 13
}

# read game input
input = []
with open("input.txt") as f:
    # for each line in the file
    for line_index,line in enumerate(f.readlines()):
        #split the game number from the series
        split_on_colon = line.split(':')
        
        #get the game id
        game = split_on_colon[0].replace('Game','').strip()

        #get each set in the series
        game_sets = split_on_colon[1].split(";")

        #build object to store all game info
        tmp = {
            "game": int(game),
            "sets": []
        }

        #for each set
        for set_index,set in enumerate(game_sets):
            #separate elements
            elements = set.split(",")

            #object to store set information
            tmp_sets = {
                "set": (set_index+1),
                "elements":[]
            }
            #for each element
            for e in elements:
                #remove leading and trailing whitespace
                e = e.strip()

                #separate color and count
                split_on_comma = e.split(' ')

                #add elements to object
                tmp_sets['elements'].append({
                    "color": split_on_comma[1],
                    "count": int(split_on_comma[0])
                })
            tmp['sets'].append(tmp_sets)
        
        # add completed object to list
        input.append(tmp)


sum = 0

#part 2
sum_of_powers = 0

#for each game
for game in input:
    # assume game is valid until proven otherwise
    valid_game = True

    #part 2
    min_red = 0
    min_blue = 0
    min_green = 0

    # for each set in the game
    for set in game['sets']:
        #for each element in the set
        for e in set['elements']:
            # check if the color and count is valid
            for key,value in MAX_CUBES.items():
                #if not valid
                if e['color'] == key and e['count'] > value:
                    valid_game = False

            #part 2 - find minimum number of cubes needed to make the game valid   
            match e['color']:
                case 'red':
                    if e['count'] > min_red:
                        min_red = e['count']
                case 'blue':
                    if e['count'] > min_blue:
                        min_blue = e['count']
                case 'green':
                    if e['count'] > min_green:
                        min_green = e['count']

    # part 2 - sum of powers
    power = min_red * min_blue * min_green
    sum_of_powers += power
    
    # sum game id if the game was valid
    if valid_game:
        sum += game['game']

print(sum)

#part 2
print(sum_of_powers)
