#!/usr/bin/env python3
import sys
import os

def for_os(filesname):
	osname = sys.platform
	if osname == "linux":
		filesname = filesname.replace(' ','\ ')
		filesname = filesname.replace('(','\(')
		filesname = filesname.replace(')','\)')

	if osname == "win32":
		filesname = '"'+filesname+'"'

	return filesname

if __name__ == "__main__":
	print("Start")
	allthefiles = os.listdir()
	onlypdffiles = []
	
	for name in allthefiles:
		if name.count(".pdf")==1:
			onlypdffiles.append(name)
	
	onlynoncroppdf = []
	
	for name in onlypdffiles:
		if name.count("-crop.pdf") == 0:
			onlynoncroppdf.append(name)
	
	print("croping pdfs")
	for name in onlynoncroppdf:
		name = for_os(name)
		os.system("pdfcrop "+name)

	print("Done")
	input("Press Enter to finish")
