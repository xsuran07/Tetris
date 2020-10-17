## @brief Implementation of class for random picking.
## @author Jakub Šuráň

import random
import objects as ob

## @brief Simple class for random picking.
class Picker:
	def __init__(self):
		self.values = [ob.Shape1, ob.Shape2, ob.Shape3, ob.Shape4, ob.Shape5, ob.Shape6, ob.Shape7] 

	## @brief Randomly picks one of the game objects.
	## @param x X-coordinate of new object.
	## @param y Y-coordinate of new object.
	## @return Returns randomly picked game object.
	def pick(self, x, y):
		result = random.choice(self.values)
		return result(x, y)
