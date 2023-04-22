#!/usr/bin/env python3
import re
import sys
import csv

#this script takes an two inputs 1) a csv key with old YJL transcript IDs and the new transcript ID 2) any number of geneIDs (just the number is okay and so is the full thing!) it must be SPACE seperated - space and comma seperated are okay
#it will return a quoted, comma seperated list of the new transcript IDs - ready to pop into a feature plot

#setting error messages
try:
	x = sys.argv[1]
except IndexError:
	print("input 'python3 update_ID.py old_id_to_new_hyphen.csv and gene list ex: \"98050311-catl1-4\", \"98022839-sap\", \"98009864-y3950-2\"' ")

def readData(fileName):
   f = open(fileName, "r")
   data = f.readlines()
   f.close()
   return data
   
#Data is a list of strings
def removeBlankLines(data):
   goodLines = []
   for thisLine in data:
	   thisLine = thisLine.rstrip()
	   if len(thisLine) != 0:
		   goodLines.append(thisLine)
   return(goodLines)
   
def splitLines(data):
   newLines = []
   for line in data:
	   myList = line.split(",")
	   newLines.append(myList)
   return(newLines)
   
rawdata = readData("old_id_to_new_hyphen.csv")
newData = removeBlankLines(rawdata)
csvData = splitLines(newData)
length = len(csvData)

i = 2

while i < len(sys.argv):
	gene_in = sys.argv[i]
	gene_ID = re.findall(r'98\d*', gene_in)
	gene_ID = gene_ID[0]
	for row in csvData:
		if row[0] == gene_ID:
			print('"'+row[1]+'"', end="")
	if i != len(sys.argv)-1:
		print(", ", end="")
	else:
		print()
	i += 1 
