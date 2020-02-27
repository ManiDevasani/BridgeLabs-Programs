import xlsxwriter
workbook = xlsxwriter.Workbook('Instance-Para.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'InstanceType')
worksheet.write('A2', 't2.micro')
worksheet.write('B1', 'ImageId')
worksheet.write('B2', 'ami-0620d12a9cf777c87')
worksheet.write('C1', 'MinCount')
worksheet.write('C2', '1')
worksheet.write('D1', 'MaxCount')
worksheet.write('D2', '1')
worksheet.write('E1', 'SubnetId')
worksheet.write('E2', 'subnet-0e2ac296077803d40')
worksheet.write('F1', 'KeyName')
worksheet.write('F2', 'Trail')
workbook.close()






