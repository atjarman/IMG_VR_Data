import gzip
import os
import csv

"""
dir = "C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR"
#print(os.listdir(dir))

mainFile = "C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_Sequence_information.tsv.txt"
newFile = "C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_all_Sequence_information.tsv.txt"

with open(mainFile) as file:
    reader = csv.DictReader(file, dialect='excel-tab')
    count = 0
    mainList = []
    for row in reader:
        if count < 1:
            for x in row:
                mainList.append(x)
                # print(x)
            count += 1
    print(mainList)
    print("---------------------------")

with open(newFile) as file:
    reader = csv.DictReader(file, dialect='excel-tab')
    count = 0
    newFileList = []
    for row in reader:
        if count < 1:
            for x in row:
                newFileList.append(x)
                # print(x)
            count += 1
    print(newFileList)
    print("---------------------------")

print(mainList)
print(newFileList)
x = list(set(mainList) & set(newFileList))
print(x)
newHeaders = []
for header in newFileList:
    if not x.__contains__(header):
        newHeaders.append(header)
print(newHeaders)


for header in newHeaders:
    mainList.append(header)

print(mainList)
"""


infile1 = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_Sequence_information.tsv.txt', 'r')
infile2 = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_all_Sequence_information.tsv.txt', 'r')
outfile = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/new.txt', 'w')

import re


tree = {}

counter = 0
for line in infile1:
    sample = {}
    if counter == 0:
        line = line.strip('\n')
        headerList = line.split('\t')
        print(headerList)
        counter += 1
    else:
        line = line.strip('\n')
        lineList = line.split('\t')
        counter += 1
        counter2 = 0
        for x in lineList:
            sample[headerList[counter2]] = lineList[counter2]
            counter2 += 1
    print(sample)




"""
linecounter = 0
for line in infile2:
    for key, value in tree.items():
        matches = line.count(key)
        if matches > 0:
            print(key, value)
            line = line.replace(key, value)
            outfile.write(line + '\n')
        else:
            outfile.write(line + '\n')
    linecounter += 1
"""

infile1.close()
infile2.close()
outfile.close()






"""
for x in os.listdir(dir):
    print(x)
    filepath = dir + "/" + x
    y = os.listdir(filepath)
    #print(type(y))
    counter = 0
"""

"""
    for file in y:
        if counter < 2:
            if file.__contains__(".tsv") or file.__contains__(".txt"):
                #print(file)


                with open(filepath + "/" + file) as f:
                    reader = csv.DictReader(f, dialect='excel-tab')
                    count = 0
                    list = []
                    for row in reader:
                        if count < 1:
                            for x in row:
                                list.append(x)
                                #print(x)
                            count += 1
                    print(list)
                    print("---------------------------")



                with gzip.open(filepath + "/" + file, 'rb') as f:
                    counter2 = 0
                    #print(f)
                   
                    #print(f)
                    #file_contents = f.read()
                    #print("hello")
                counter +=1
"""

"""
    for x in os.listdir(main):
        if x.__contains__(".tsv"):
            reader = csv.DictReader(x, dialect='excel-tab')
            count = 0
            list1 = []
            for row in reader:
                if count < 1:
                    for x in row:
                        list1.append(x)
                        # print(x)
                    count += 1
            print(list1)
            print("****************")
"""

"""
                       for line in f:
                           if counter2 < 10:
                               print(line)
                               counter2 += 1
"""

#print(y)
"TESTING"