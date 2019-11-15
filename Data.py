import gzip
import os
import csv
import json

dir = "C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR"

old = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_Sequence_information.tsv.txt', 'r')
new = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_all_Sequence_information.tsv.txt', 'r')
outfile = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/new.txt', 'w')

counter1 = 0
masterList = []
headerList1 = []

for line in old:
    temp = {}
    if counter1 == 0:
        line = line.strip('\n')
        headerList1 = line.split('\t')
        counter1 += 1
    else:
        line = line.strip('\n')
        lineList1 = line.split('\t')
        keyCount = 0
        for x in lineList1:
            temp[headerList1[keyCount]] = x
            keyCount += 1
        counter1 += 1
        masterList.append(temp)

counter2 = 0
tempList = []
headerList2 = []

for line in new:
    if counter2 == 0:
        line = line.strip('\n')
        headerList2 = line.split('\t')
        counter2 += 1
    else:
        line = line.strip('\n')
        lineList2 = line.split('\t')
        counter2 += 1
        tempList.append(lineList2)

difference = set(headerList2) - set(headerList1)
same = set(headerList2) & set(headerList1)

headerDifPositionDict = {}
for x in difference:
       headerDifPositionDict[x] = headerList2.index(x)

headerSamePositionDict = {}
for x in same:
    headerSamePositionDict[x] = headerList2.index(x)

headerDifPositionList = list(headerDifPositionDict.values())
headerSamePositionList = list(headerSamePositionDict.values())

tempNewDict2 = {}

for x in tempList:
    tempNewDict = {}
    iD = x[headerList1.index("mVCs")]

    for y in masterList:
        present = False
        if list(y.values()).__contains__(iD):
            present = True
            for z in headerSamePositionList:
                if x[z] != y[headerList2[z]]:
                    tempNewDict[headerList2[z]] = x[z]
            break

    if not present:
        for y in headerList2:
            tempNewDict[y] = x[headerList2.index(y)]
        tempNewDict2[x[headerList1.index("mVCs")]] = tempNewDict
    else:
        for y in headerDifPositionList:
            tempNewDict[headerList2[y]] = x[y]
        tempNewDict2[x[headerList1.index("mVCs")]] = tempNewDict

#print(json.dumps(tempNewDict2, indent=4, sort_keys=True))


#for x in tempNewDict2:
#    print(x)

#test = json.dumps(tempNewDict2, indent=4, sort_keys=True)



old.close()
new.close()
outfile.close()






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

"""
print(tempNewDict2)
print(headerList1)
print(masterList)
print("----------------------------------")
print(headerList2)
print(tempList)
"""

"""
for x in headerList2:
    if not headerList1.__contains__(x):
        print(x, headerList2.index(x))
"""

"""
for x in tempList:
    iD = x[headerList1.index("mVCs")]

    for y in masterList:
        present = False
        if list(y.values()).__contains__(iD):
            present = True
            break
    if not present:
        print(x)
        print("true")
"""

"""
print(headerSamePositionList)
for x in tempList:
    iD = x[headerList1.index("mVCs")]
    for y in masterList:
        if list(y.values()).__contains__(iD):
            for z in headerSamePositionList:
                if x[z] != y[headerList2[z]]:
                    print(False, x[z], y[headerList2[z]])

    #print(x)
"""

"""
newSampleList = []
for x in tempList:
    present = False
    for y in masterList:
        if y.__contains__(x[0]):
            present = True
            print(x)
            print(y)
            print(set(x) & set(y))
            if x == y:
                print("True")
            else:
                print("False")
    if not present:
        newSampleList.append(x)
"""

"""
import os
# Read in the original and new file
orig = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_Sequence_information.tsv.txt', 'r')
new = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_all_Sequence_information.tsv.txt', 'r')
#in new but not in orig
bigb = set(new) - set(orig)
# To see results in console if desired
print(bigb)
# Write to output file
with open('different.csv', 'w') as file_out:
    for line in bigb:
        file_out.write(line)
#close the files
orig.close()
new.close()
file_out.close()
"""

"""
infile1 = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_Sequence_information.tsv.txt', 'r')
infile2 = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/IMGVR_all_Sequence_information.tsv.txt', 'r')
outfile = open('C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR/Test/new.txt', 'w')

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

print(tree)
infile1.close()
infile2.close()
outfile.close()
"""

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
