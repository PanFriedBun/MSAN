import json
import sys

## change made here !!!

def jsontocsv():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        ##read file load into python
        json_data=open('t.json').read()
        data = json.loads(json_data)
        ##extract 'header' from json file
        header = []
        for i in range(0,len(data["headers"])):
            header.append(data["headers"][i])
        real_header = ','.join(header)
        ##write header into file 
        print real_header
        ##extract 'data' from python 
        total = []
        for j in range(0,len(data["data"])):
            single = []
            for k in range(0,len(data["headers"])):
                single.append(data["data"][j][data["headers"][k]])
            total.append(','.join(single))
            
        ##print total[m] with last new line also
        ##write the 'data' into file   
        new_line = ""
        for m in range(0,len(total)):
            if m != len(total)-1 : 
                new_line += total[m] + '\n'
            else:
                new_line += total[m]
        print new_line
        return real_header, total
jsontocsv()