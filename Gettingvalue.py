import openpyxl

files = [] 
values = []

for file in files:
    wb = openpyxl.load_workbook(file)
    sheet = wb['Sheet1']
    value = sheet['F5'].value
    values.append(value)