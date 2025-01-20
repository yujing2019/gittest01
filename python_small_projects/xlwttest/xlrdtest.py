import xlrd
wb=xlrd.open_workbook('result.xls')
print("The number of worksheets is {0}".format(wb.nsheets))
sh = wb.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))