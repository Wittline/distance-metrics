class switch:

	def __init__(self, vbe, comparator=None, strict=False):
		self.vbe = vbe
		self.matched = False
		self.match = False
		if comparator:
			self.comparator = comparator
		else:
			self.comparator = lambda x, y: x == y
		self.strict = strict

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass

	def case(self, expr, break_=False):
		if self.strict:
			if self.matched:
				return False
		if self.match or self.comparator(self.vbe, expr):
			if not break_:
				self.match = True
			else:
				self.matched = True
				self.match = False
			return True
		else:
			return False

	def default(self):
		return not self.matched and not self.match