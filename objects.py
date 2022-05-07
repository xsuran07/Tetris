'''
Author(s): Jakub Šuráň

Implementation of game objects.
'''

import constants as const


class Shape1:
    '''
    Representation of game object ("square")
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = 0
        self.color = const.RED
        self.states = [[[0, 0, 0, 0],
                       [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]]]

    def draw(self, drawer):
        for i, row in enumerate(self.states[self.pos]):
            for j, square in enumerate(row):
                if(square):
                    drawer(self.x - 1 + j, self.y - 2 + i, const.WHITE, self.color)

    def get_x(self):
        '''
        Simple method for getting x-coordinate.

        Return
        ------
        int
            Object's x-coordinate.
        '''

        return self.x

    def get_y(self):
        '''
        Simple method for getting y-coordinate.
        Returns
        -------
        int
            Object's y-coordinate.
        '''

        return self.y

    def set_cor(self, new_x, new_y):
        '''
        Simple method for setting both coordinates.
        '''

        self.x = new_x
        self.y = new_y

    def add_x(self, value):
        '''
        Adds given value to x-coordinate.
        '''

        self.x += value

    def add_y(self, value):
        '''
        Adds given value to y-coordinate.
        '''

        self.y += value

    def get_active_blocks(self):
        '''
        Finds out which blocks on playing field are occupied by the object.

        Returns
        -------
        dict
            Hash map with occupied blocks.
        '''

        ret = {}

        for i, row in enumerate(self.states[self.pos]):
            for j, square in enumerate(row):
                if(square):
                    key = (self.x - 1 + j, self.y - 2 + i)
                    ret[key] = self.color

        return ret

    def add_active_blocks(self, struct):
        '''
        Adds blocks which object currently occupies into given hash map + checks if object isn't over the top.
        Returns
        -------
        bool
            True if everything is ok, False if any part of object is over the top of playing field.
        '''

        ret = True

        for i, row in enumerate(self.states[self.pos]):
            for j, square in enumerate(row):
                if(square):
                    key = (self.x - 1 + j, self.y - 2 + i)

                    if(key[1] < 0):
                        ret = False
                        continue
                    struct[key] = self.color

        return ret


class Shape2(Shape1):
    '''
    Representation of game object ("long line")
    '''

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = const.GREEN
        self.states = [[[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0]],
                       [[0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0]],
                       [[0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0]]]


class Shape3(Shape1):
    '''
    Representation of game object ("reverse L")
    '''

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = const.BLUE
        self.states = [[[0, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 1, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 0, 0]]]


class Shape4(Shape1):
    '''
    Representation of game object ("L")
    '''

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = const.LIGHT_PURPLE
        self.states = [[[0, 0, 0, 0],
                        [0, 0, 1, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 1, 0]],
                       [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 1, 0],
                        [1, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0]]]


class Shape5(Shape1):
    '''
    Representation of game object ("reverse Z")
    '''

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = const.DARK_PURPLE
        self.states = [[[0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0]],
                       [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [1, 1, 0, 0]],
                       [[0, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0]]]


class Shape6(Shape1):
    '''
    Representation of game object ("Z")
    '''

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = const.LIGHT_ORANGE
        self.states = [[[0, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0]],
                       [[0, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0]]]


class Shape7(Shape1):
    '''
    Representation of game object ("ship")
    '''

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = const.DARK_ORANGE
        self.states = [[[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 1, 0, 0]],
                       [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0]]]
