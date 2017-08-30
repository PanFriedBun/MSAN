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






## write the csv data into json format 
def writejson(header, myList):
    starter = "{\n"
    starter += '  "headers":['
    for i in range(0,len(header)):
        starter += '"'+header[i]+'"'
        if(i != len(header)-1):
            starter += ','
    starter += '],\n'
    middle = '  "data":[\n    '
    for j in range(0,len(myList)):
        middle +='{\n      '
        for k in range(0,len(myList[j])):
            middle += '"'+header[k]+'":' + '"'+myList[j][k]+'"'
            if(k != len(myList[j]) -1):
                middle += ','
        middle += '\n    }'
        if (j != len(myList)-1):
            middle += ',\n    '
        else:
            middle += "\n  "
    bottom = ']\n'
    bottom += '}'
    print starter + middle + bottom


header, myList = readcsv(getdata())
writejson(header, myList)