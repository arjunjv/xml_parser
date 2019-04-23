#!/usr/bin/env python3

import os
import csv
import sys
import xml.dom.minidom as xml
import shutil


JPEGImagesPath = ""
AnnotationsPath = ""
tagPath = ""


#read the search path from user
def readTag():

    searchTag = input("Enter the Tag to search in XML file: ")
    return searchTag

# to read the path and validate it
def readPath():

    path = input("Enter the path for the Annotations files: ")

    if (os.path.exists(path)):
        return path
    else:
        print("Path entered is invalid")
        sys.exit()

# create the directories for output
def createDirectory(tag):

	global tagPath
	global AnnotationsPath
	global JPEGImagesPath

	path = os.getcwd()  
	print("The current working directory is %s" % path)  
	
	#	create the directory with tag name 
	tagPath = path+ "/" + tag
	if not os.path.exists(tagPath):
		os.mkdir(tagPath)
		print("Directory " , tagPath ,  " Created ")
	else:
		print("Directory " , tagPath ,  " already exists")

	#	create the directory with JPEGImages named in tag named folder
	AnnotationsPath = path+ "/" + tag + "/" + "Annotations"
	if not os.path.exists(AnnotationsPath):
		os.mkdir(AnnotationsPath)
		print("Directory " , AnnotationsPath ,  " Created ")
	else:
		print("Directory " , AnnotationsPath ,  " already exists")

	#	create the directory with Annotations named in tag named folder
	JPEGImagesPath = path+ "/" + tag + "/" + "JPEGImages"
	if not os.path.exists(JPEGImagesPath):
		os.mkdir(JPEGImagesPath)
		print("Directory " , JPEGImagesPath ,  " Created ")
	else:
		print("Directory " , JPEGImagesPath ,  " already exists")



def main():
	global  AnnotationsPath
	global JPEGImagesPath

	annoationPath = readPath()
	searchTag = readTag()
	createDirectory(searchTag)
	
	for root, dirs, files in os.walk(annoationPath):
		for fileName in files:
			xmlFile = annoationPath + '/' + fileName
			doc = xml.parse(xmlFile)
	
			name = doc.getElementsByTagName("name")
			j = 0
			# main loop to copy the files ;)
			for i in name:
				if (name[j].firstChild.nodeValue == searchTag):
					print(fileName)
					shutil.copy(xmlFile, AnnotationsPath)
					xmlFile = os.path.splitext(xmlFile)[0]
					xmlFile = xmlFile.replace("Annotations","JPEGImages") + ".jpg"
					shutil.copy(xmlFile,JPEGImagesPath)
					break
				j = j + 1;


if __name__ == "__main__":
	print("Make sure you execute the file with sudo permission")
	main()	
	print("Sucessfully copied the files")
