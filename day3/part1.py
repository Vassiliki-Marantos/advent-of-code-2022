file_path = 'day3\input.txt'
total_priority = 0

with open(file_path, 'r') as f:
    lines = f.readlines()

def get_priority(character):
    int_value = ord(character)
    if int_value > 64 and int_value < 91:
        priority = int_value - 38
    if int_value > 96 and int_value < 123:
        priority = int_value - 96
    return priority

def get_shared_item(line):
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    common_letters=list(set(firstpart)&set(secondpart))
    return common_letters[0]

for line in lines:
    sahred_item = get_shared_item(line)
    priority = get_priority(sahred_item)
    total_priority += priority

print("final priority value: ", total_priority)