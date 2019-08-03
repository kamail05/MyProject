# Importing package -> Moving to the workbook -> Moving to the sheet
import openpyxl
# Here we are importing the openpyxl package to use its functions

wb = openpyxl.load_workbook("C:/Users/Abilash/PycharmProjects/AT/Testdata.xlsx")
# Creating object to open the excel/workbook

sh = wb['Hi Dude']
# creating object for the sheet where the values are stored in to use it.

# First Way to read values from excel

print(sh['E4'].value)
print(sh['A2'].value)
print(sh['B3'].value)
# Using the sheet object by giving the excel index value(sh['B3'].value) we are reading the values in excel.

# Another way to read the values available in the excel
# Creating object for the cell using sheet naem and accessing the cell values
cl = sh.cell(2,4)
print(cl.value)

# By using this 2 approaches we can fetch values from the excel
# 1.By Using sheet name object with excel cell value index(A4).value
# 2.By Creating object for cell with sheetname object and passing excel index to it(1,4) and .value