import ReadAttr
import GetOutput
import ReadXML
import RunProcess
import MergeList
import WriteCSV
import SysExit

def main():
    outFile = ""
    desiredAttr = []
    xmlList = []
    attrValList = []
    tagAttrDict = {}
    numOfAttrs = 0

    print("******XML Scrapper for Latern Archieve v1.0.0******\n Author: Zhiren Xu\n")
    desiredAttr = ReadAttr.readAttr()
    outFile = GetOutput.getOutput()
    numOfAttrs = len(desiredAttr)
    xmlList = ReadXML.readXML()
    while (len(xmlList) > 0):
        attrValList.append(RunProcess.runProcess(xmlList.pop(0), desiredAttr))
    WriteCSV.writeCSV(desiredAttr, attrValList, outFile)
    SysExit.sysExit(outFile)
    
if __name__ == "__main__":
    main()
