import csv
def getCSVData(fileName):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


def readAndWrite(filereadfrom):

    rows = []
    csv_fileread = open(filereadfrom,'r')

    csv_reader = csv.reader(csv_fileread)
    next(csv_reader)

    csv_filewrite = open('newfile.csv','w',newline='')

    # fields = list(filereadfrom[0].keys)

    csv_writter = csv.writer(csv_filewrite)
    # csv_writter.writeheader()

    for data in csv_reader:
        rows.append(data)
        csv_writter.writerow(data)
    return rows


def writeCSVData(filename):

    datafile =  open(filename,'w',newline='')

    write = csv.writer(datafile)

    for row in datafile:
        write.writerow(row)

    datafile.close()

def writedataintofile(filename):
    csvfile=open(filename,'w', newline='')
    obj=csv.writer(csvfile)
    for data in filename:
        obj.writerow(data)
    csvfile.close()

    # Instad of iterating over the list to write each row individually, we can use writerows() method.
def writedataincsv(filename):
    csvfile = open(filename, 'w', newline='')
    obj = csv.writer(csvfile)
    obj.writerows(filename)
    obj.close()