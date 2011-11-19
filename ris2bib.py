#!/usr/bin/env python
# encoding: utf-8

"""
ris2bib.py

Takes .ris files as first argument in the form 'name.ris' and outputs files in the bibtex format in the form 'name.bib'.
Currently assuming Nature article format for ease of programming.

D.P O'Hanlon
19/10/2011

"""

import sys
import os
import re
import string

def r2b():

	authors=[]

	ris = open(sys.argv[1],'r+')

	for line in ris:
		if re.match("PY",line):
			year = line[6:10]
		elif re.match("AU",line):
			authors.append(line[6:-1]) # goes from end of AU designation to end minus one to remove newline character
		elif re.match("VL",line):
			volume = line[6:-1]
		elif re.match("TI",line):
			title = line[6:-1]
		elif re.match("JA",line):
			journal = line[6:-1]
		elif re.match("IS",line):
			number = line[6:-1]
		elif re.match("SP",line):
			startpage = line[6:-1]
		elif re.match("EP",line):
			endpage = line[6:-1]
		elif re.match("UR",line):
			url = line[6:-1]
		else:
			print "Unparsed line: " + line

	ris.close()

	bib = open(sys.argv[1][:-4]+'.bib','w+') # strip and replace extension

	bib.write('@ARTICLE{' + authors[0][:string.find(authors[0], ',')] + str(year) + ",") #takes surname of first author via slicing to ','
	bib.write('\nauthor=\t\"'+authors[0])
	for entry in authors[1:]:
		bib.write(" and " + entry)
	bib.write("\",")
	bib.write('\nyear=\t\"'+ year + "\",")
	bib.write("\ntitle=\t\"" + title + "\",")
	bib.write("\njournal=\t\"" + journal + "\",")
	bib.write("\nvolume=\t\"" + volume + "\",")
	bib.write("\nnumber=\t\"" + number + "\",")
	bib.write("\npages=\t\"" + startpage + "--" + endpage + "\",")
	bib.write("\nurl=\t\"" + url + "\",")
	bib.write("\n}\n")

	bib.close()			

if __name__ == '__main__':
	r2b()
