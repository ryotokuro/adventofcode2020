# https://adventofcode.com/2020/day/2
import re

f = open("input2.txt", "r")  # read input from file

policies = {}
valid_count = 0

# Extract information from input string
while True:
    line = f.readline()
    # check if line is null
    if not line:
        break

    info = line.strip()
    # print(info)

    # find the letter
    letter_filter = re.compile('[a-z]+')
    letter = letter_filter.search(info).group()
    letter_index = info.find(letter)

    # define the lower and upper bounds
    separator_index = info.find('-')  # separator gives us the location of the numbers
    lower = int(info[:separator_index])
    upper = int(info[separator_index+1:letter_index])

    # extract the string (3 positions after the letter)
    string_index = letter_index + 3  # e.g. a: string
    string = info[string_index:]

    # iterate through each password and validate
    valid = False
    count = 0
    for i in string:
        if i == letter:
            count += 1
            if count >= lower and count <= upper:
                valid = True
            else:
                valid = False
    if valid == True:
        valid_count += 1

print(valid_count)  # print the number of valid passwords
