import xml.etree.ElementTree as ET
import ParseXML
import GetAttr

## the main process of scrap
# @param    xml
#           target xml need to be scraped
# @param    desiredAttr
#           a dict conatins what attr we want
# @return    resultList
#           a list contains lists of each attri value          
def runProcess(xml, desiredAttr):
    resultList = []
    tagAttr = {}
    
    tree = ET.parse(xml)
    tagAttr = ParseXML.parseXML(tree)
    resultList = GetAttr.getAttr(desiredAttr, tagAttr)

    return resultList
