import csv 
import re

with open("javaqa.txt") as read:
    data = read.read().replace('\n', ' ')
    data = re.split("\d{1,4}\.(\D*\.)", data)
    
    key = ""
    dictionary = dict()
    alllist = []
    for line in data:
        if line:
            line = re.split('(.*)\?', line)
            linelist = []
            for string in line:
                if string:
                    string = string.replace('?', 'and')
                    string = string.strip()
                    string = string.lower()
                    linelist.append(string)

            match = re.match("-\D*-", linelist[0])
            if match is not None:           
                    if alllist:
                        dictionary[key] = alllist
                    key = linelist[0]
                    alllist = []
                    #print(linelist[0])        

            elif linelist != ['']:
                alllist.append(linelist)
                #print(linelist,'\n')
            else:
                dictionary[key] = alllist
                

print(dictionary)

