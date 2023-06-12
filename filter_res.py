import pandas as pd
import csv

count = 0
doobls = 0

csv_file = 'Data/result_list.csv'
result_file = 'Data/newResult.csv'

with open(result_file, "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        (
            'name',
            'url',
            'email'
        )
    )

def check_line(line1):
    with open(result_file, 'r') as fileline:
        if line1 in fileline:
            return True
        else:
            return False


def write_line(line2):
    with open(result_file, 'a') as newfile:
        newfile.write(line2)


with open(csv_file, 'r') as oldfile:
    for line in oldfile:
        if check_line(line):
            doobls += 1
        else:
           write_line(line)
           count += 1


print(count)
print(doobls)
