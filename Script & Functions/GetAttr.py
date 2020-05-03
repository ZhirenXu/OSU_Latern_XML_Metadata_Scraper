import sys

## match attributes with their tag and find it in parsed xml, return attri value
# @param    desiredAttr
#           a list contain attributes client want
# @param    tagAttrDict
#           a dict contain specific tag and all attrs of these tag.
#           DesiredAttr is gurantee to be in this dict
# @return   attribValueList
#           a list for all attrib values required
def getAttr(desiredAttr, tagAttrDict):
    attrValue = ""
    attribValueList = []
    
    for key in tagAttrDict.keys():
        attribTuplesDict = tagAttrDict[key]
        for attr in desiredAttr:
            if (attr in attribTuplesDict):
                attrValue = attribTuplesDict[attr]
                attribValueList.append(attrValue)
    if(len(attribValueList) == 0):
        print("Could not find any keywords! Press enter to exit.")
        key = input()
        sys.exit()

    return attribValueList
