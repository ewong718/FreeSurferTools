import os
import glob
import sys
import getopt
import csv

def main():
    
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")

    for option, value in opts:
        if option in ("-i"):
            inputFile = value
        if option in ("-o"):
            outputdir = value
    #inputFile = "/Users/edmundwong/Desktop/murrough_Freesurfer/nonPartialVolumeStatsRight.txt"
    #outputDir = "/Users/edmundwong/Desktop/murrough_Freesurfer/"
    outCsvName = "HippocampalSubfields.csv"
    f = open(inputFile, "r")

    wholeList = list()
    
    for line in f:
        subList = list()
        subList.append("Subject") 
        lll = line.split()
        subList.append(lll[1])
        subList.append(lll[2])
        subList.append(lll[3])
        subList.append(lll[4])
        subList.append(lll[5])
        subList.append(lll[6])
        wholeList.append(subList)
        break  
    
    for line in f:
        subList = list()
        lll = line.split()
        subList.append(lll[0])
        subList.append(lll[1])
        subList.append(lll[2])
        subList.append(lll[3])
        subList.append(lll[4])
        subList.append(lll[5])
        subList.append(lll[6])
        wholeList.append(subList)
    print wholeList
    
    with open(outputDir + "/" + outCsvName, 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        data = wholeList
        a.writerows(data)


if __name__ == "__main__":
    sys.exit(main())