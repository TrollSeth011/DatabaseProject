from xlwt import Workbook
"""
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

print(grades[2] + grades[3])
