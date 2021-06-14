class Base(object):
	name = None
	description = None
	width = None

	def __init__(self, name, description, bits_range):
		self.name = name
		self.description = description
		self.bit_range
	
	def __str__(self):
		return "name : %s description : %s width : %s" % (self.name, self.description, self.width)

	def update_name(self, name):
		self.name = name
		return self
	
	def update_description(self, description):
		self.description = description
		return self
	
	def update_width(self, width):
		self.width = width
		return self