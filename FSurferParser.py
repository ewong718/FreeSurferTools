'''
Created on Jul 31, 2014

@author: edmundwong
'''

import os
import sys
import csv
import glob
import getopt

help_message = """
Provides command line tool for parsing FreeSurfer output aseg.stats files.

Commands
--------
-h, --help
    Prints out this message.
-i The input directory containing all recon-all FreeSurfer output directories (Mandatory)
-o The full filename and path to output csv file (Mandatory)
"""

class Usage(Exception):
    def __init__(self, msg=help_message):
        self.msg = msg

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    except getopt.error, msg:
        raise Usage()
    for option, value in opts:
        if option in ("-h"):
            raise Usage()
        if option in ("-i"):
            FSinput = value
        if option in ("-o"):
            outputCsv = value
    
    os.chdir(FSinput)
    wholeList = list()
    for fsFile in glob.glob("*/stats/aseg.stats"):
        subList = list()
        subList.append("Subject")
        f=open(fsFile,"r")
        for line in f:
            if (line[0] != "#"):
                lll = line.split()            
                subList.append(lll[4])        
        wholeList.append(subList)
        break
    for fsFile in glob.glob("*/stats/aseg.stats"):
        subList=list()
        f=open(fsFile,"r")
        subList.append(fsFile[0:15])
        for line in f:
            if (line[0] != "#"):
                lll = line.split()            
                subList.append(lll[3])
        wholeList.append(subList)
        

    with open(outputCsv, 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        data = wholeList
        a.writerows(data)
    
    print "Success. See output file at " + outputCsv
        

if __name__ == "__main__":
    sys.exit(main())