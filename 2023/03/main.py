import re

symbol_pattern = re.compile(r'[^0-9a-zA-Z\.]+')
number_pattern = re.compile(r'\d+')

def find_locations_in_row(row,pattern):
    tmp_dict = []
    if row is not None:
        results = re.findall(pattern,row)
        prev_loc = -1
        for x in results:
            number_loc = row.find(x,prev_loc+1)
            prev_loc = number_loc
            tmp_dict.append(
                (
                    x,number_loc
                )
            )
    return tmp_dict

def find_parts_for_current_row(curr,prev,next):
    to_add = []
    symbols= []
    curr_numbers = find_locations_in_row(curr,number_pattern)
    prev_symbols = find_locations_in_row(prev,symbol_pattern)
    next_symbols = find_locations_in_row(next,symbol_pattern)

    symbols.extend(prev_symbols)
    symbols.extend(next_symbols)

    # print(curr_numbers,symbols)

    for number,number_loc in curr_numbers:
        start = number_loc - 1
        while start < 0:
            start +=1
        
        end = number_loc + ((len(number)-1) + 1) + 1
        while end > len(curr):
            end -= 1
        # print ("number_loc: {} start: {} end: {}".format(str(number_loc),str(start),str(end)))
        curr_window = curr[start:end]
        # print(curr_window)
        symbol_in_curr_window = False
        search = re.findall(symbol_pattern,curr_window)
        if len(search) > 0:
            symbol_in_curr_window = True
        symbol_in_other_row_window = False
        for symbol,symbol_loc in symbols:
            if symbol_loc >= start and symbol_loc <= end:
                symbol_in_other_row_window = True
        
        if symbol_in_curr_window or symbol_in_other_row_window:
            to_add.append(number)

    return to_add

sum = 0
lines = []

with open("input.txt") as f:
    # for each line in the file
    for line_index,line in enumerate(f.readlines()):     
        lines.append(line.replace('\n',''))

for line_index,line in enumerate(lines):
    print(line)

line_index = 0
max_line_index = len(lines)

parts_to_sum = []

for line_index,line in enumerate(lines):

    if line_index < max_line_index+1:
        prev = lines[line_index-1] if line_index > 0 else None
        curr = line
        next = lines[line_index+1] if line_index < max_line_index-1 else None

        parts = find_parts_for_current_row(curr,prev,next)
        parts_to_sum.append(parts)

# print(parts_to_sum)
with open("output.txt","w") as f:
    for parts in parts_to_sum:
        f.write("{}\n".format(parts))
        for part in parts:
            sum+=int(part)
print(sum)