import openpyxl

# Creating object for the workbook to use it.
wb = openpyxl.Workbook()
# Verifying the current active sheet name
sh = wb.active
print(sh.title)
# Changing the sheet name in excel
sh.title="HelloTestingworld"
print(sh.title)

# Entering the value into the excel
# By selecting the cell and sending data to it
sh['A1'].value='Name'
sh['B1'].value='City'
sh['C1'].value='State'

# Second Sheet is created using openpyxl
wb.create_sheet('Test Sheet To Store data')

# Creating object for the second sheet newly created.
sh1 = wb['Test Sheet To Store data']
sh1['A1'].value='Name'
sh1['B1'].value='City'
sh1['C1'].value='State'

#Approach to remove sheet
wb.remove_sheet(wb['HelloTestingworld'])

wb.save('SampleexcelWriteData.xlsx')



