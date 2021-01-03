# https://adventofcode.com/2020/day/1

report = []  # create list to store input report

f = open("input1.txt", "r")  # read input from file

while True:
    line = f.readline()
    # check if line is null
    if not line:
        break

    n = int(line.strip())
    report.append(n)  # populate list

diff = {}
magic = 2020
for expense in report:
    diff[expense] = magic - expense  # calculate difference from desired number

for key, val in diff.items():
    if val in report:
        print(key*val)  # print result
        break  # return once we find it
