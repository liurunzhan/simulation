
'''
  generate markdown file with mermaid style
'''

class MarkdownMark:
	layouts = [
		"TB", "TD", "BT", "RL", "LR"
	]
	edge_marks = [
		["---", "----", "-----"],
		["-->", "--->", "---->"],
		["===", "====", "====="],
		["==>", "===>", "====>"],
		["-.-", "-..-", "-...-"],
		["-.->", "-..->", "-...->"]
	]
	node_marks = [
		["[", "]"], ["(", ")"], 
		["[[", "]]"], ["[(", ")]"], ["((", "))"], ["([", "])"],
		[">", "]"], 
		["{", "}"], ["{{", "}}"],
		["[/", "/]"], ["[\\", "\\]"], ["[/", "\\]"], ["[\\", "/]"]
	]

markdown_marks = MarkdownMark

class DotMark:
	layouts = []
	edge_marks = []
	node_marks = []

def write_markdown_to_file(objects, file):
	with open(file, "w") as fout:
		print("```mermaid", file=fout)
		print("graph LR;", file=fout)
		print("```", file=fout)

def write_dot_to_file(objects, file):
	with open(file, "w") as fout:
		print("digraph %s {", file=fout)
		print("}", file=fout)
