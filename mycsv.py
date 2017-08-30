import sys
import codecs


def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()




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



header, myList = readcsv(getdata())
writejson(header, myList)

