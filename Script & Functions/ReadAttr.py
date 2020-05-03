from functions import ReadCSV

## read attrs from input csv file
# @return    attrsList
#           a list contains all desired attributes
def readAttr():
    csv = ""
    attrsList = []

    print("Please enter a csv file that contains attributes you want to scrape as a template.")
    print("Attributes should all be put in the first row, like a header. In the header, each cell should only has one attribute.")
    print("File name(with .csv): ", end = "")
    csv = input()
    attrsList = ReadCSV.readCSV(csv)

    return attrsList
