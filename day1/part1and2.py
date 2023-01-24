import heapq

file_path = 'day1\input.txt'

with open(file_path, 'r') as f:
    lines = f.readlines()

calories_per_elf = []
calories = 0

for line in lines:
    if line.strip() != "":
        calories += int(line.strip())
    else:
        calories_per_elf.append(calories)
        calories = 0

#part 1
# max functionn - O(n log n)
max_calories = max(calories_per_elf)
print("Max calories: ", max_calories)

#part 2 - using heapq
#heapq nlargest - O(n log k)  (more efficient than max and sort functions)
n = 3
max_three = heapq.nlargest(n, calories_per_elf)
total_max_three = sum(max_three)
print("Total of top 3 calories held: ", total_max_three)

#part 2 - using sort
# sort fucntion - O(n log n)
calories_per_elf.sort()
max_three = calories_per_elf[-n:]
total_max_three = sum(max_three)
print("Total of top 3 calories held: ", total_max_three)

