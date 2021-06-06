import pygame

from board import Board

pygame.init()
pygame.display.set_caption('Tic Tac Toe')

X_Image = pygame.image.load('./X.png')

black = (0, 0, 0)
white = (255, 255, 255)
gray = (125, 125, 125)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

WIDTH = 800
HEIGHT = 600
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
gameDisplay.fill(white)

# Draw the game board
gameBoard = Board(gameDisplay, black)
gameBoard.drawBoard()

gameDisplay.blit(X_Image, (100, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print (event.pos)
            # print (gameBoard.isClickInBoard(event.pos))
            print (gameBoard.getClickedCell(event.pos))

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

    pygame.display.update()