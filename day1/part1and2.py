file_path = 'day1\input.txt'

file1 = open(file_path, 'r')
Lines = file1.readlines()

calories_per_elf = []
calories = 0

for line in Lines:
    if line.strip() != "":
        calories += int(line.strip())
    else:
        calories_per_elf.append(calories)
        calories = 0

#part 1
max_calories = max(calories_per_elf)
print("Max calories: ", max_calories)

#part 2
calories_per_elf.sort()
n = 3

max_three = calories_per_elf[-n:]
total_max_three = sum(max_three)

print("Total of top 3 calories held: ", total_max_three)

