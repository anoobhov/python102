import xlrd

f = xlrd.open_workbook("SampleData.xlsx")

sheet = f.sheet_by_index(1)

# for row 0 and column 0
print(sheet.cell_value(0,0))