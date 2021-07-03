import json

OBJECT_IS_IDLE       = 0 # 
OBJECT_IS_OPERATOR   = 1 # 
OBJECT_IS_NAME       = 2 # ch == "_" or ch.isalpha()
OBJECT_IS_NUMBER     = 3 # ch.isnumeric()
OBJECT_IS_STRING     = 4 # ch == "\""
OBJECT_IS_DOCUMENT   = 5 # ch == "/"
OBJECT_IS_SDOCUMENT  = 6 # ch[1:0] == "//"
OBJECT_IS_DDOCUMENT  = 7 # ch[1:0] == "/*" 
OBJECT_IS_DDOCUMENT1 = 8 # ch[1:0] == "*/"

class Token(object):
	def __init__(self, name, type, row, col):
		self.name = name
		self.type = type
		self.row  = row
		self.col  = col
	def __str__(self):
		return "%s,%d,%d,%d" % (self.name, self.type, self.row, self.col)
	def __repr__(self):
		return "[%s,%d,%d,%d]" % (self.name, self.type, self.row, self.col)
	def __iter__(self):
		return next(self)
	def __next__(self):
		yield("name", self.name)
		yield("type", self.type)
		yield("row",  self.row)
		yield("col",  self.col)

class Lexer(object):
	def __init__(self, name):
		self.name = name
		self.tokens = []
	def __str__(self):
		return "%s:%s" % (self.name, self.tokens)
	def __repr__(self):
		return "name : %s, tokens : %s" % (self.name, self.tokens)
	def __iter__(self):
		return next(self)
	def __next__(self):
		yield("name", self.name)
		yield("tokens", self.tokens)
	def __getitem__(self, item):
		return self.tokens[item]
	def to_json(self, file):
		pass
	def to_file(self, file):
		with open(file, "w") as fout:
			for token in self.tokens:
				print(token, file=fout)

def create_lexer_from_string(string):
	lexer = Lexer(list(dict(string=string).keys())[0])
	object = None
	word  = []
	state = OBJECT_IS_IDLE
	i = 0
	for j in range(len(string)):
		ch = string[j]
		if state == OBJECT_IS_IDLE:
			if "_" == ch or ch.isalpha():
				object = Token("", OBJECT_IS_NAME, i+1, j+1)
				word.append(ch)
				state = OBJECT_IS_NAME
			elif ch.isnumeric():
				object = Token("", OBJECT_IS_NUMBER, i+1, j+1)
				word.append(ch)
				state = OBJECT_IS_NUMBER
			elif ch == "/":
				object = Token("", OBJECT_IS_DOCUMENT, i+1, j+1)
				word.append(ch)
				state = OBJECT_IS_DOCUMENT
			elif ch == "\"":
				word.append(ch)
				object = Token("", OBJECT_IS_STRING, i+1, j+1)
				state = OBJECT_IS_STRING
			else:
				word = []
				if not ch.isspace():
					lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
				state = OBJECT_IS_IDLE
		elif state == OBJECT_IS_NAME:
			if "_" == ch or ch.isalnum():
				word.append(ch)
			else:
				object.name = "".join(word)
				lexer.tokens.append(object)
				word = []
				if ch == "/":
					object = Token("", OBJECT_IS_DOCUMENT, i+1, j+1)
					word.append(ch)
					state = OBJECT_IS_DOCUMENT
				else:
					if not ch.isspace():
						lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
					state = OBJECT_IS_IDLE
		elif state == OBJECT_IS_NUMBER:
			if ch.isnumeric() or ch in {"'", "_", "b", "d", "o", "h", "x", "z", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}:
				word.append(ch)
			else:
				object.name = "".join(word)
				lexer.tokens.append(object)
				word = []
				if ch.isalpha():
					object = Token("", OBJECT_IS_NAME, i+1, j+1)
					word.append(ch)
					state = OBJECT_IS_NAME
				elif ch == "/":
					object = Token("", OBJECT_IS_DOCUMENT, i+1, j+1)
					word.append(ch)
					state = OBJECT_IS_DOCUMENT
				else:
					if not ch.isspace():
						lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
					state = OBJECT_IS_IDLE
		elif state == OBJECT_IS_STRING:
			word.append(ch)
			if ch == "\"":
				object.name = "".join(word)
				lexer.tokens.append(object)
				word = []
				state = OBJECT_IS_IDLE
		elif state == OBJECT_IS_DOCUMENT:
			if ch == "/":
				word.append(ch)
				state = OBJECT_IS_SDOCUMENT
			elif ch == "*":
				word.append(ch)
				state = OBJECT_IS_DDOCUMENT
			else:
				object.name = "/"
				object.type = OBJECT_IS_OPERATOR
				lexer.tokens.append(object)
				if "_" == ch or ch.isalpha():
					object = Token("", OBJECT_IS_NAME, i, j)
					word.append(ch)
					state = OBJECT_IS_NAME
				elif ch.isnumeric():
					object = Token("", OBJECT_IS_NUMBER, i, j)
					word.append(ch)
					state = OBJECT_IS_NUMBER
				else:
					word = []
					if not ch.isspace():
						lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
					state = OBJECT_IS_IDLE
		elif state == OBJECT_IS_SDOCUMENT:
			if ch == "\n":
				object.name = "".join(word)
				lexer.tokens.append(object)
				word = []
				state = OBJECT_IS_IDLE
			else:
				word.append(ch)
		elif state == OBJECT_IS_DDOCUMENT:
			word.append(ch)
			if ch == "*" and line[j+1] == "/":
				word.append("/")
				object.name = "".join(word)
				lexer.tokens.append(object)
				word = []
				state = OBJECT_IS_DDOCUMENT1
		elif state == OBJECT_IS_DDOCUMENT1:
			state = OBJECT_IS_IDLE

	return lexer

def create_lexer_from_file(file):
	lexer = Lexer(file)
	object = None
	word  = []
	state = OBJECT_IS_IDLE
	with open(file, "r") as fin:
		lines = fin.readlines()
		for i in range(len(lines)):
			line = list(lines[i])
			for j in range(len(line)):
				ch = line[j]
				if state == OBJECT_IS_IDLE:
					if "_" == ch or ch.isalpha():
						object = Token("", OBJECT_IS_NAME, i+1, j+1)
						word.append(ch)
						state = OBJECT_IS_NAME
					elif ch.isnumeric():
						object = Token("", OBJECT_IS_NUMBER, i+1, j+1)
						word.append(ch)
						state = OBJECT_IS_NUMBER
					elif ch == "/":
						object = Token("", OBJECT_IS_DOCUMENT, i+1, j+1)
						word.append(ch)
						state = OBJECT_IS_DOCUMENT
					elif ch == "\"":
						word.append(ch)
						object = Token("", OBJECT_IS_STRING, i+1, j+1)
						state = OBJECT_IS_STRING
					else:
						word = []
						if not ch.isspace():
							lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
						state = OBJECT_IS_IDLE
				elif state == OBJECT_IS_NAME:
					if "_" == ch or ch.isalnum():
						word.append(ch)
					else:
						object.name = "".join(word)
						lexer.tokens.append(object)
						word = []
						if ch == "/":
							object = Token("", OBJECT_IS_DOCUMENT, i+1, j+1)
							word.append(ch)
							state = OBJECT_IS_DOCUMENT
						else:
							if not ch.isspace():
								lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
							state = OBJECT_IS_IDLE
				elif state == OBJECT_IS_NUMBER:
					if ch.isnumeric() or ch in {"'", "_", "b", "d", "o", "h", "x", "z", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}:
						word.append(ch)
					else:
						object.name = "".join(word)
						lexer.tokens.append(object)
						word = []
						if ch.isalpha():
							object = Token("", OBJECT_IS_NAME, i+1, j+1)
							word.append(ch)
							state = OBJECT_IS_NAME
						elif ch == "/":
							object = Token("", OBJECT_IS_DOCUMENT, i+1, j+1)
							word.append(ch)
							state = OBJECT_IS_DOCUMENT
						else:
							if not ch.isspace():
								lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
							state = OBJECT_IS_IDLE
				elif state == OBJECT_IS_STRING:
					word.append(ch)
					if ch == "\"":
						object.name = "".join(word)
						lexer.tokens.append(object)
						word = []
						state = OBJECT_IS_IDLE
				elif state == OBJECT_IS_DOCUMENT:
					if ch == "/":
						word.append(ch)
						state = OBJECT_IS_SDOCUMENT
					elif ch == "*":
						word.append(ch)
						state = OBJECT_IS_DDOCUMENT
					else:
						object.name = "/"
						object.type = OBJECT_IS_OPERATOR
						lexer.tokens.append(object)
						if "_" == ch or ch.isalpha():
							object = Token("", OBJECT_IS_NAME, i, j)
							word.append(ch)
							state = OBJECT_IS_NAME
						elif ch.isnumeric():
							object = Token("", OBJECT_IS_NUMBER, i, j)
							word.append(ch)
							state = OBJECT_IS_NUMBER
						else:
							word = []
							if not ch.isspace():
								lexer.tokens.append(Token(ch, OBJECT_IS_OPERATOR, i+1, j+1))
							state = OBJECT_IS_IDLE
				elif state == OBJECT_IS_SDOCUMENT:
					if ch == "\n":
						object.name = "".join(word)
						lexer.tokens.append(object)
						word = []
						state = OBJECT_IS_IDLE
					else:
						word.append(ch)
				elif state == OBJECT_IS_DDOCUMENT:
					word.append(ch)
					if ch == "*" and line[j+1] == "/":
						word.append("/")
						object.name = "".join(word)
						lexer.tokens.append(object)
						word = []
						state = OBJECT_IS_DDOCUMENT1
				elif state == OBJECT_IS_DDOCUMENT1:
					state = OBJECT_IS_IDLE
	
	return lexer

if __name__ == "__main__":
	file = "tbench.sv"
	string = "reg [123 : 12] abc;"
	lexer1 = create_lexer_from_file(file)
	lexer2 = create_lexer_from_string(string)
	print(lexer1)
	print(lexer2)
	
