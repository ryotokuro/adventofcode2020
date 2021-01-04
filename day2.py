# https://adventofcode.com/2020/day/2
import re

f = open("input2.txt", "r")  # read input from file

policies = {}

while True:
    line = f.readline()
    # check if line is null
    if not line:
        break

    info = line.strip()
    print(info)
    
    separator_index = info.find('-')
    letter_filter = re.compile('[a-z]+')
    a = letter_filter.find(info)
    
    lower = int(info[:separator_index])
    upper = info[separator_index+1:]
    
valid = 0
