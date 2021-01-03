# https://adventofcode.com/2020/day/1

report = [1721, 979, 366, 299, 675, 1456]
diff = [2000 - i for i in report]
print(diff)

for i in diff:
    if i in report:
        return 
    
