## @brief Implementation of class for random picking.
## @author Jakub Šuráň

import random
import objects as ob

## @brief Simple class for random picking.
class Picker:
	def __init__(self):
		self.values = [ob.Shape1, ob.Shape2, ob.Shape3, ob.Shape4, ob.Shape5, ob.Shape6, ob.Shape7] 

	## @brief Randomly picks one of the game objects.
	## @return Returns randomly picked game object.
	def pick(self):
		result = random.choice(self.values)
		return result(4, 0)
