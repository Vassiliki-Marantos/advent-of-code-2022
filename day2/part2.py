elf_rock = 'A'
elf_paper = 'B'
elf_scissors = 'C'

lose = 'X'
draw = 'Y'
win = 'Z'

file_path = 'day2\input.txt'
total_points = 0

def shape_selection(round):
    outcome = round[1]
    elfPlay =round[0]
    if outcome == draw:
        myPlay = elfPlay
    if outcome == win:
        if elfPlay == elf_rock:
            myPlay = elf_paper
        if elfPlay == elf_paper:
            myPlay = elf_scissors   
        if elfPlay == elf_scissors:
            myPlay = elf_rock    
    if outcome == lose:
        if elfPlay == elf_rock:
            myPlay = elf_scissors
        if elfPlay == elf_paper:
            myPlay = elf_rock   
        if elfPlay == elf_scissors:
            myPlay = elf_paper      
    return myPlay

def shape_selection_score(myPlay):
    if myPlay == elf_rock:
        points = 1
    if myPlay == elf_paper:
        points = 2    
    if myPlay == elf_scissors:
        points = 3    
    return points

def game_outcome_score(outcome):
    if outcome == win:
        points = 6
    if outcome == lose:
        points = 0
    if outcome == draw:
        points = 3
    return points

def get_score(line):
    round = line.split()
    game_outcome_points = game_outcome_score(round[1])
    selected_shape = shape_selection(round)
    shape_selection_points = shape_selection_score(selected_shape)
    
    round_score = shape_selection_points + game_outcome_points
    return round_score


with open(file_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    round_points = get_score(line)
    total_points += round_points

print("The score is: ", total_points)


