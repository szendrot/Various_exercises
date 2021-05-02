# write your code here
import sys
import os
import pathlib
print(sys.argv[0])
print(os.getcwd())
print(os.path)
print(pathlib.Path(__file__).parent.absolute())

path = sys.argv[0]
data = '''3500
4780
6666
4567
6785
3214
3456'''

with open('salary.txt', 'w') as f:
    f.write(data)
f.close()

f = open('salary.txt', 'r')
#print(f.readline())
print(f.read())
f.close()

f = open('salary.txt', 'r')
salary = []
for i in f:
    salary.append(int(i))
print(f.read())
f.close()

f = open('salary_year.txt', 'w')
for i in salary:
    f.write(str(i * 12) + ' \n')
f.close()

f = open('salary_year.txt', 'r')
print(f.read())
f.close()

# ------or-------

with open('salary.txt') as in_file, open('salary_year.txt', 'w') as out_file:
    for line in in_file:
        annual_salary = 12 * int(line)
        out_file.write(str(annual_salary) + '\n')








