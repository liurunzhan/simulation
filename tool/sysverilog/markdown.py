
'''
  generate markdown file with mermaid style
'''

class Mark:
	layout = [
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

markdown_marks = Mark

def write_markdown_to_file(objects, file):
	with open(file, "w") as fout:
		print("```mermaid", file=fout)
		print("graph LR;", file=fout)
		print("```", file=fout)
