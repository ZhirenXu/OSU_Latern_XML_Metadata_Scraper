##ask user for output file name
# @return   outFile
#           name of output file
def getOutput():
    outFile = ""
    
    print("please enter the output csv file name (with .csv): ", end = "")
    outFile = input()
    return outFile
