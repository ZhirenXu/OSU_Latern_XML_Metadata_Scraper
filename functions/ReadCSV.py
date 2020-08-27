import csv
import sys
## read first row of @csv and output its contents as a list
# @param    csv
#           input csv
# @return   attrs
#           a list content all cell contents
def readCSV(csvFile):
    attrs = []
    
    with open(csvFile, encoding="utf-8-sig") as inFile:
        try:
            csvReader = csv.reader(inFile, delimiter=',')
            for row in csvReader:
                attrs = row
                break
            inFile.close()
        except:
            print("Fail to open file. Please check again. Press any key to exit. ")
            key = input()
            sys.exit()
    return attrs
