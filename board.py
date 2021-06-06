import pygame

class Board:
    def __init__ (self, screen, color):
        self.screen = screen
        self.color = color

        self.cellCount = 3
        self.cellSize = 150
        self.offset = 75
        self.strokeWidth = 3
        self.gridData = {
            'cell1': [(75, 75), (225, 225), False],
            'cell2': [(225, 75), (375, 225), False],
            'cell3': [(375, 75), (525, 225), False],
            'cell4': [(75, 225), (225, 375), False],
            'cell5': [(225, 225), (375, 375), False],
            'cell6': [(375, 225), (525, 375), False],
            'cell7': [(75, 375), (225, 525), False],
            'cell8': [(225, 375), (375, 525), False],
            'cell9': [(375, 375), (525, 525), False]
        }

    def drawBoard (self):
        """Draws the TicTacToe Board"""
        for i in range(4):
            ## Vertical Lines
            pygame.draw.line(self.screen, self.color, \
                (i * self.cellSize + self.offset, self.offset),\
                (i * self.cellSize + self.offset, self.cellSize * self.cellCount + self.offset), self.strokeWidth)
            ## Horizontal Lines
            pygame.draw.line(self.screen, self.color, \
                (self.offset, i * self.cellSize + self.offset),\
                (self.cellSize * self.cellCount + self.offset, i * self.cellSize + self.offset), self.strokeWidth)
        pygame.display.flip()
    
    def isInRectangle (self, bound1, bound2, position):
        """Check if the position resides in a rectangle given the bounds"""
        return (position[0] > bound1[0] and position[0] < bound2[0]) and \
            (position[1] > bound1[1] and position[1] < bound2[1])

    def isClickInBoard (self, pos):
        """Check if the position resides in the game board"""
        return self.isInRectangle((self.offset, self.offset), \
            ((self.cellCount * self.cellSize) + self.offset, (self.cellCount * self.cellSize) + self.offset), pos)
    
    def getClickedCell (self, pos):
        """Returns the cell in which the mouse is clicked"""
        cellToReturn = None

        if (not self.isClickInBoard(pos)):
            cellToReturn = None
        else:
            for key, value in self.gridData.items():
                if (self.isInRectangle (value[0], value[1], pos)):
                    cellToReturn = key
                    break
        
        return cellToReturn











    # (pos[0] > self.offset and pos[0] < (self.cellCount * self.cellSize) + self.offset) and \
    #     (pos[1] > self.offset and pos[1] < (self.cellCount * self.cellSize) + self.offset)