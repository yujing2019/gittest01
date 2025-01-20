import xlwt
wb=xlwt.Workbook(encoding='utf-8')

sheet=wb.add_sheet('sgrade')

row=0
with open('input.txt') as fin:
    for lin in fin:
        lin=lin.strip()
        fields=lin.split('\t')
        for i in range(len(fields)):
            print(row,i,fields[i])
            sheet.write(row,i,fields[i])
        row +=1
print(row)
wb.save('result.xls')
