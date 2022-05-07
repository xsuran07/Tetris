'''
Author(s): Jakub Šuráň

Implementation of class for random picking.
'''

import random
import objects as ob


class Picker:
    '''
    Simple class for random picking.
    '''

    def __init__(self):
        self.values = [ob.Shape1, ob.Shape2, ob.Shape3, ob.Shape4, ob.Shape5, ob.Shape6, ob.Shape7]

    def pick(self, x, y):
        '''
        Randomly picks one of the game objects.

        Parameters
        ----------
        x : int
            X-coordinate of new object.
        y : int
            Y-coordinate of new object.
        Returns
        -------
        ob.Shape1
            Returns randomly picked game object.
        '''

        result = random.choice(self.values)
        return result(x, y)
