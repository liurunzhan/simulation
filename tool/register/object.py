class Base(object):
	name = None
	description = None
	width = None

	def __init__(self, name, description, bit_range):
		self.name = name
		self.description = description
		self.bit_range = bit_range
	
	def __str__(self):
		return "%s,%s,%s" % (self.name, self.description, self.bit_range)

	def __repr__(self):
		return "[%s,%s,%s]" % (self.name, self.description, self.bit_range)
	
	def __iter__(self):
		return next(self)
	
	def __next__(self):
		yield("name", self.name)
		yield("description", self.description)
		yield("bit_range",  self.bit_range)

	def update_name(self, name):
		self.name = name
		return self
	
	def update_description(self, description):
		self.description = description
		return self
	
	def update_bit_range(self, bit_range):
		self.bit_range = bit_range
		return self