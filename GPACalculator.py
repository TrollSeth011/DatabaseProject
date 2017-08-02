"""
from xlwt import Workbook

wb = Workbook()
sheetname = 'Test Sheet'
message = 'This is an example'
wbname = 'test.xls'
def ExcelWrite(message, sheetname, wbname):
    sheet1 = wb.add_sheet(str(sheetname))
    sheet1.write(0,0,str(message))
    sheet1.write(0,1, 'This is another example')
    wb.save(wbname)

ExcelWrite(message, sheetname, wbname)
"""
import xlrd

workbook = xlrd.open_workbook('data.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')

grades = []
for x in range(worksheet.nrows - 1):
    grades += worksheet.cell_value(x+1, 1)
print(grades)

def findMinus(list):
    for i in list:
        if i == '-':
            minus_index = list.index('-')
            list.append(list[minus_index-1] + list[minus_index])
            list.pop(minus_index)
            list.pop(minus_index-1)
    return list

def findPlus(list):
    for i in list:
        if i == '+':
            plus_index = list.index('+')
            list.append(list[plus_index-1] + list[plus_index])
            list.pop(plus_index)
            list.pop(plus_index-1)
    return list

for i in range(2):
    findMinus(grades)
    findPlus(grades)

def findValue(updatedlist):
    file = open("grade_scale.txt", "r")
    d = {}
    grade_value = []
    for line in file:
        x = line.split(" ")
        a = x[0]
        b = x[1]
        c=len(b)-1
        b=b[0:c]
        d[a] = b
    for i in updatedlist:
        print("this is i: " + i)
        for x in d:
            if i == x:
                grade_value.append(float(d[x]))
                print( grade_value)
    total = sum(grade_value)
    possible = len(grade_value)*4
    print(total)
    print(possible)


findValue(grades)
