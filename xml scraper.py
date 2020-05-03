from functions import Greeting
from functions import ReadAttr
from functions import SimpleCSV
from functions import AskBypass
from functions import ReadXML
from functions import RunProcess
from functions import WriteCSV

def main():
    outFile = ""
    desiredAttr = []
    xmlList = []
    xmlListCp = []
    attrValList = []
    tagAttrDict = {}
    numOfAttrs = 0
    isBypassed = False

    Greeting.showInfo()
    desiredAttr = ReadAttr.readAttr()
    outFile = SimpleCSV.getCSVOutput()
    isBypassed = AskBypass.askBypass()
    numOfAttrs = len(desiredAttr)
    xmlList = ReadXML.readXML()
    xmlListCp = xmlList.copy()

    while (len(xmlList) > 0):
        print("Processing File: ", xmlList[0], " ......", end = "")
        attrValList.append(RunProcess.runProcess(isBypassed, xmlList.pop(0), desiredAttr))

    desiredAttr.insert(0, "Original_File_Name")
    WriteCSV.writeCSV(xmlListCp, desiredAttr, attrValList, outFile)
    Greeting.sysExit(outFile)
    
if __name__ == "__main__":
    main()
