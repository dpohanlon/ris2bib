#!/usr/bin/env python
# encoding: utf-8

"""
ris2bib.py

Takes .ris files as first argument in the form 'name.ris' and outputs files in the bibtex format in the form 'name.bib'.
Currently assuming Nature article format for ease of programming.

Usage is python ris2bib.py [FILE...]

D.P O'Hanlon
23/11/2011

"""

import sys
import os
import re
import string

def main(argv=sys.argv):
	ris = open(argv[1],'r+')
	
	entries = r2b_read(ris, argv)

	ris.close()

	bib_filename = argv[1][:-4]+'.bib' # strip and replace extension

	r2b_write(entries, bib_filename)

def r2b_read(ris,argv):
	entries = dict()
	entries['authors']=list()
	verbose = False

	for line in ris:
		if re.match("PY",line):
			entries['year'] = line[6:10]
		elif re.match("AU",line):
			entries['authors'].append(line[6:-1]) # goes from end of AU designation to end minus one to remove newline character
		elif re.match("VL",line):
			entries['volume'] = line[6:-1]
		elif re.match("TI",line):
			entries['title'] = line[6:-1]
		elif re.match("JA",line):
			entries['journal'] = line[6:-1]
		elif re.match("IS",line):
			entries['number'] = line[6:-1]
		elif re.match("SP",line):
			entries['startpage'] = line[6:-1]
		elif re.match("EP",line):
			entries['endpage'] = line[6:-1]
		elif re.match("UR",line):
			entries['url'] = line[6:-1]
		else
			print 'Unparsed line: ' + line[:-1]
	return entries
		
def r2b_write(entries,bib_filename):
	bib = open(bib_filename,'w+') # strip and replace extension

	bib.write('@ARTICLE{' + entries['authors'][0][:string.find(entries['authors'][0], ',')] + str(entries['year']) + ",") #takes surname of first author via slicing to ','
	bib.write('\nauthor=\t\"'+entries['authors'][0])
	for entry in entries['authors'][1:]:
		bib.write(" and " + entry)
	bib.write("\",")
	bib.write('\nyear=\t\"'+ entries['year'] + "\",")
	bib.write("\ntitle=\t\"" + entries['title'] + "\",")
	bib.write("\njournal=\t\"" + entries['journal'] + "\",")
	bib.write("\nvolume=\t\"" + entries['volume'] + "\",")
	bib.write("\nnumber=\t\"" + entries['number'] + "\",")
	bib.write("\npages=\t\"" + entries['startpage'] + "--" + entries['endpage'] + "\",")
	bib.write("\nurl=\t\"" + entries['url'] + "\",")
	bib.write("\n}\n")

	bib.close()			

if __name__ == '__main__':
	main()	
