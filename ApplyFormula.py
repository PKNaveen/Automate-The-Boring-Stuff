import openpyxl

files = [] # Insert paths to files here

for file in files:
    wb = openpyxl.load_workbook(file)
    sheet = wb['Sheet1']
    sheet['F9'] = '=SUM(F5:F8)'
    sheet['F9'].style = 'Currency'
    wb.save(file)