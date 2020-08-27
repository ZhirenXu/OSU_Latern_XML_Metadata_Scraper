import xml.etree.ElementTree as ET
from functions import ParseXML
from functions import GetAttr

## the main process of scrap
# @param    isBypassed
#           a bool value indicates if error is ignored
# @param    xml
#           target xml need to be scraped
# @param    desiredAttr
#           a dict conatins what attr we want
# @return    resultList
#           a list contains lists of each attri value          
def runProcess(isBypassed, xml, desiredAttr):
    resultList = []
    tagAttr = {}
    
    tree = ET.parse(xml)
    tagAttr = ParseXML.parseXML(tree)
    resultList = GetAttr.getAttr(isBypassed, desiredAttr, tagAttr)

    return resultList
