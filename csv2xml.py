import sys
import codecs

## get data by provided function 
def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()



## extract csv data into header & myList
def readcsv(data):
    '''
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    '''
    ##split data by new line character and store in splited_data
    splited_data = data.split('\n')
    length_of_splited_data = len(splited_data)
    myList = []
    header = splited_data[0].split(',')
    for i in range(1,length_of_splited_data):
        entry = splited_data[i].split(',')
        myList.append(entry)
    ##print header
    ##print myList 
    ## what is printed gets write to the file 
    return header, myList








## write the csv data into xml format 
def writexml(header, myList):
    starter = '<?xml version="1.0"?>\n'
    starter += "<file>\n"
    starter += "    <headers>"+ ','.join(header) + "</headers>\n"
    starter += "    <data>\n"
    middle = ""
    for j in range(0,len(myList)):
        middle += "        <record>\n            "
        for k in range(0,len(myList[j])):
            ##get rid of white space in xml tags name
            header[k] = header[k].replace(" ","_")
            middle += "<"+header[k]+">" + myList[j][k] + "<"+"/"+header[k]
            if k != len(myList[j])-1:
                middle += ">\n            "
            else:
                 middle += ">"
        middle += "\n        </record>\n"
    buttom  =""
    buttom  += "    </data>\n"
    buttom  += "</file>"
    print starter + middle + buttom
header, myList = readcsv(getdata())
writexml(header, myList)