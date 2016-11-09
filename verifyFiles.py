#!/usr/bin/env python

#Script to check whether the output files generated by HCP pipeline scripts
#are the same or not. It will check for the match between two files with respect the filename, size, content, modification time, distance etc.
#Maintainters : Big Data Lab Team, Concordia University.
#email : tristan.glatard@concordia.ca, laletscaria@yahoo.co.in

import os
import sys
import subprocess
from collections import OrderedDict

total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
print ("Script name: %s" % str(sys.argv[0]))
print ("First argument: %s" % str(sys.argv[1]))
fileNamesAndDirArray = []
file_dir_dict = OrderedDict()

#Method list_files_and_dirs is used for listing files and directories present in the input directory.
#Input Argument : Directory Path
def list_files_and_dirs(dir):
        listFileAndDirs = []
        for root, dirs, files in os.walk(dir):
           for dirname in dirs:
              listFileAndDirs.append(os.path.join(root, dirname))
           for name in files:
              listFileAndDirs.append(os.path.join(root, name))
        listFileAndDirs.sort(key=lambda x: os.path.getmtime(x))
        return listFileAndDirs

#Method populate_file_dir_dict is an ordered  python dictionary to save the status details of
#each file and directory present in the listFileAndDirs list
#Input parameter : List contianing the details of the path of each file and directory.
def populate_file_dir_dict(listFileAndDirs):
        temp_dict = OrderedDict()
        for path in listFileAndDirs:
           dirDetails = os.stat(path)
           temp_dict[path]= dirDetails
        return temp_dict

fileNamesAndDirArray=list_files_and_dirs(sys.argv[1])
file_dir_dict=populate_file_dir_dict(fileNamesAndDirArray)
print fileNamesAndDirArray
print file_dir_dict
