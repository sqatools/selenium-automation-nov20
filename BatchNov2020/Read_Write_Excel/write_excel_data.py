import openpyxl
from Read_Write_Excel.read_excel_sheet import *


wb = openpyxl.Workbook()
sheet = wb.active

sheet["A30"] = 'Python'
sheet["B30"] = 'Automation'


#wb.save('pythonlearning.xlsx')
wb.save('test_data.xlsx')

read_excel_data_by_cellname('test_data.xlsx', "A30")

