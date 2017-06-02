#!/usr/bin/python3

import shutil
import os
import time
import csv

number = 0
def writelog(action,time):
	global number 
	number += 1
	data = [(number,action,time)]

	with open("log_file.csv","wb",newline='',encoding="utf-8") as csvlog:
		file = 	csv.writer(csvlog,delimiter=",")
		file.writerows(data)
		csvlog.close()

	
def copyfile(namefile,destinationfile):
	filein = open(namefile,"r")
	fileout = open(destinationfile,"w")

	for line in filein:
		fileout.write(line)

	filein.close()
	filein.close()
	
	timeline = time.strftime('%A , %d %B %Y %H: %M: %S',time.localtime(time.time()))

	writelog("copy file",timeline)
	

def movefile(namefile,destinationfile):
	shutil.move(namefile,destinationfile)
	if os.path.exists(destinationfile):
		print ("successfully move")
	else:
		print ("error try again")

	timeline = time.strftime('%A , %d %B %Y %H: %M: %S',time.localtime(time.time()))
	writelog("move file",timeline)

def changenamefile(namefile,destinationfile):
	if os.path.exists(namefile):
		os.rename(namefile,destinationfile)
		timeline = time.strftime('%A , %d %B %Y %H: %M: %S',time.localtime(time.time()))

		writelog("change name file",timeline)
	else:
		print("file is not found try again")

	
def deletefile(namefile):
	if os.path.exists(namefile):
		os.remove(namefile)
		timeline = time.strftime('%A , %d %B %Y %H: %M: %S',time.localtime(time.time()))

		writelog("delete file",timeline)
	else:
		print("file is not found try again")
while 1:

	print("------welcome to file manipulation--------")
	print("\t\t choose: \t\t")
	print("1.copy file")
	print("2.move file")
	print("3.rename file")
	print("4.delete file")

	choice = int(input("enter a number:"))

	if choice is 1:
		user = input("input file name to be copy:")
		copy = input("input file name destination:")

		copyfile(user,copy)
	
	elif choice is 2:
		user = input("input file name to be move:")
		copy = input("input file name destination:")
	
		movefile(user,copy)
	
	elif choice is 3:
		user = input("input file name to be rename:")
		copy = input("input file name destination:")

		changenamefile(user,copy)

	elif choice is 4:
		user = input("input file name to be delete:")

		deletefile(user)
