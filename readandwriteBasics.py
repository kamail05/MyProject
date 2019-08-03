# Importing openpyxl package to use functions available in it
import openpyxl

# Creating object to load workbook - using function available in openpyxl
wb = openpyxl.load_workbook("C:/Users/Abilash/PycharmProjects/AT/Testdata.xlsx")
# 1. Here we are asking openpyxl to open the excel file available in given file path

# Getting All sheet names which is available in given excel - using function available in openpyxl
print(wb.sheetnames)
# 2. Here we can find out what are the sheets available

# Here we are checking the active sheet in excel -(Active Sheet - By Default sheet opens when opening the excel file)
print("Active Sheet is ",wb.active.title)
# 3. Here we are getting the title of the active sheet

# Creating object for the sheet which we want to work
sh = wb['Hi Dude']
print(sh.title)
# Create object for the sheet which we want to work and printing it's name to verify
