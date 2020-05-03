import csv

## read first row of @csv and output its contents as a list
# @param    csv
#           input csv
# @return   attrs
#           a list content all cell contents
def readCSV(csvFile):
    attrs = []
    
    with open(csvFile, encoding="utf-8-sig") as inFile:
        csvReader = csv.reader(inFile, delimiter=',')
        for row in csvReader:
            attrs = row
            break
    inFile.close()
    
    return attrs
