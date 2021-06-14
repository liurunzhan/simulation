from enum import Flag
import re

class Object(object):
	def __init__(self, name, line):
		self.name = name
		self.line = line

mode_docw = re.compile(r"/\*[\S\s]*\*/")
mode_docs = re.compile(r"//[\S\s]*")
mode_docl = re.compile(r"/\*[\S\s]*")
mode_docr = re.compile(r"[\S\s]*\*/")

def delete_redundancy(line, flag):
	line = mode_docw.sub("", line)
	line = mode_docs.sub("", line)
	if mode_docl.match(line):
		flag = True
		line = mode_docl.sub("", line)
	if mode_docr.match(line):
		flag = False
		line = mode_docr.sub("", line)

	return re.sub(r"[\s\t\r\n]+", " ", line), flag

def file_parser(file):
	lines = []
	with open(file, "r") as fin:
		flag = False
		for line in fin.readlines():
			line, flag  = delete_redundancy(line, flag)
			print("%s %s" % (line, flag))
			if flag == False:
				lines.append(line)
	
	return lines
	
if __name__ == "__main__":
	file = "tbench.sv"
	lines = file_parser(file)
	for line in lines:
		print(line)