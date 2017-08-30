import sys
import xml.etree.ElementTree as ET


def xmltocsv():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        tree = ET.parse(sys.argv[1])
        root = tree.getroot()
        total = []
        for i in range(0,len(root[1])):
            single = []
            for j in range(0,len(root[1][i])):
                single.append(root[1][i][j].text)
            total.append(','.join(single))
        root_text = root[0].text
        
        print root_text 
        for i in range(0,len(total)):
            print total[i] 
        return root_text, total

xmltocsv()
    
