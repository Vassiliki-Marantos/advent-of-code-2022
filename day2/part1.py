elf_rock = 'A'
elf_paper = 'B'
elf_scissors = 'C'

my_rock = 'X'
my_paper = 'Y'
my_scissors = 'Z'

file_path = 'day2\input.txt'
total_points = 0

def shape_selection_score(myPlay):
    if myPlay == my_rock:
        points = 1
    if myPlay == my_paper:
        points = 2    
    if myPlay == my_scissors:
        points = 3    

    return points

def convert_elf_play(elfPlay):
    if elfPlay == elf_rock:
        elfPlay = my_rock
    if elfPlay == elf_paper:
        elfPlay = my_paper
    if elfPlay == elf_scissors:
        elfPlay = my_scissors
    return elfPlay
    
def game_outcome_score(gameRound):
    elfPlay = gameRound[0]
    myPlay = gameRound[1]
    elfPlay = convert_elf_play(elfPlay)

    elfPlayShapeScore = shape_selection_score(elfPlay)
    myPlayShapeScore = shape_selection_score(myPlay)

    if elfPlayShapeScore == myPlayShapeScore:
        points = 3
    elif  myPlayShapeScore > elfPlayShapeScore:
        if myPlayShapeScore-elfPlayShapeScore > 1:
            points = 0
        else:
            points = 6
    elif  myPlayShapeScore < elfPlayShapeScore:
        if elfPlayShapeScore-myPlayShapeScore > 1:
            points = 6
        else:
            points = 0
    else:
        print("this logic did not assign points to anyone")
        points = 0
    return points

def get_score(line):
    round = line.split()
    shape_selection_points = shape_selection_score(round[1])
    game_outcome_points = game_outcome_score(round)
    round_score = shape_selection_points + game_outcome_points
    return round_score


with open(file_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    round_points = get_score(line)
    total_points += round_points


print("The score is: ", total_points)

# alternative way to do this is to do the comparisson with numbers

