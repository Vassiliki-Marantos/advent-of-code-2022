import re

file_path = 'day4\input.txt'

with open(file_path, 'r') as f:
    lines = f.readlines()


    
def create_list(line):
    just_numeric = re.sub('[^0-9]','', line)
    numbers = [int(char) for char in just_numeric]
    print(numbers)
    return numbers

def isContained(numbers):
    for number in numbers:
        print(number)

for line in lines:
    new_list = create_list(line)
    isContained(new_list)
    print("*****************")

    # the issue with what you have done is that you are splitting a number that is greater than 9 into many numbers, so that is a flaw lol