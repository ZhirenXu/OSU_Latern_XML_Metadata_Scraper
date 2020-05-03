import ReadAttr
import GetOutput
import ReadXML
import RunProcess
import MergeList
import WriteCSV
import SysExit
import AskBypass

def main():
    outFile = ""
    desiredAttr = []
    xmlList = []
    xmlListCp = []
    attrValList = []
    tagAttrDict = {}
    numOfAttrs = 0
    isBypassed = False

    print("******XML Scrapper for Lantern Archieve v1.1.0******\n Author: Zhiren Xu\n")
    desiredAttr = ReadAttr.readAttr()
    outFile = GetOutput.getOutput()
    isBypassed = AskBypass.askBypass()
    numOfAttrs = len(desiredAttr)
    xmlList = ReadXML.readXML()
    xmlListCp = xmlList.copy()

    while (len(xmlList) > 0):
        print("Processing File: ", xmlList[0], " ......", end = "")
        attrValList.append(RunProcess.runProcess(isBypassed, xmlList.pop(0), desiredAttr))

    desiredAttr.insert(0, "Original_File_Name")
    WriteCSV.writeCSV(xmlListCp, desiredAttr, attrValList, outFile)
    SysExit.sysExit(outFile)
    
if __name__ == "__main__":
    main()
