import re

class Object(object):
	def __init__(self, name, line):
		self.name = name
		self.line = line
	
def delete_dummy_space(line):
	return re.sub(r"\r?\n", "", re.sub(r"[\r\t]+", " ", line))

def delete_document(line):
	return line


def object_parser(file):
	lines = None
	with open(file, "r") as fin:
		lines = fin.readlines()
	
