import sys

## Prompt message when program finished and wait for program exit
# @param    outFile
#           name of output csv file
def sysExit(outFile):
    print("The program has finished. The output file is: ", outFile, " . It is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
