file_path = 'day3\input.txt'
total_priority = 0
counter = 0
small_list = []

with open(file_path, 'r') as f:
    lines = f.readlines()

def get_priority(character):
    int_value = ord(character)
    if int_value > 64 and int_value < 91:
        priority = int_value - 38
    if int_value > 96 and int_value < 123:
        priority = int_value - 96
    return priority

def get_shared_item(lines):
    firstpart, secondpart, thirdpart = lines[0], lines[1], lines[2]
    common_letters=list(set(firstpart)&set(secondpart)&set(thirdpart))
    return common_letters[0]

for line in lines:
    small_list.append(line.strip())
    if counter == 2:
        counter = 0
        shared_item = get_shared_item(small_list)
        priority = get_priority(shared_item)
        total_priority += priority
        small_list = []
    else:
        counter +=1
    
    

print("final priority value: ", total_priority)