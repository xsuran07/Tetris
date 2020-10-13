import random
import objects as ob

class Picker:
	def __init__(self):
		self.values = [ob.Shape1, ob.Shape2, ob.Shape3, ob.Shape4, ob.Shape5, ob.Shape6, ob.Shape7] 

	def pick(self):
		result = random.choice(self.values)
		return result(4, 5)
