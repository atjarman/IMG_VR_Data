import gzip
import os
import csv

dir = "C:/Users/Owner/Desktop/School/BMI 483/IMG_VR_download/IMG_VR"
#print(os.listdir(dir))


for x in os.listdir(dir):
    filepath = dir + "/" + x
    y = os.listdir(filepath)
    #print(type(y))
    counter = 0
    for file in y:
        if counter < 1:
            if file.__contains__(".tsv"):
                #print(file)


                with open(filepath + "/" + file) as f:
                    reader = csv.DictReader(f, dialect='excel-tab')
                    count = 0
                    for row in reader:
                        if count < 1:
                            for x in row:
                                print(x)
                            count += 1
                    print("---------------------------")



                with gzip.open(filepath + "/" + file, 'rb') as f:
                    counter2 = 0
                    #print(f)
                    """
                    for line in f:
                        if counter2 < 10:
                            print(line)
                            counter2 += 1
                    """
                    #print(f)
                    #file_contents = f.read()
                    #print("hello")
                counter +=1


    #print(y)