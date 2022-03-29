# This is a tic tac toe game using pygame
# Player 1 is X and Player 2 is O
# If you finished your game with a win or tie press R to start a new game
# Made by George Issa
# ID 20211027
# Made for bonus 4 : task 7


import pygame, sys
import numpy as np

pygame.init()
#Constants
W = 600
H = 600
Board_Rows = 3
Board_Col = 3
##RGB format
COLOR = (138,43,226)
LineColor = (75,0,130)
White = (255, 255 , 255)
Black = (0,0,0)


LineWidth = 10

#Screen
gameScreen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tic Tac Toe FCAI")
gameScreen.fill(COLOR)

# Console Board
Board = np.zeros ((Board_Rows , Board_Col))

#Drawing the graphical board
def draw_lines():
    #Horizontal lines
    pygame.draw.line (gameScreen  , LineColor, (0,200), (600,200) , LineWidth)
    pygame.draw.line(gameScreen, LineColor, (0, 400), (600, 400), LineWidth)
    #Vertical lines
    pygame.draw.line(gameScreen, LineColor, (200, 0), (200, 600), LineWidth)
    pygame.draw.line(gameScreen, LineColor, (400, 00), (400, 600), LineWidth)

#Drawing the figures
def DrawXO ():
    for row in range(Board_Rows):
        for col in range(Board_Col):
            if Board[row][col] == 1 :
                pygame.draw.line (gameScreen , White , (col * 200 + 55 , row * 200 + 200 - 55),(col* 200 + 200 - 55 , row * 200 + 55), 25)
                pygame.draw.line (gameScreen , White , (col * 200 + 55 , row * 200 + 55),(col* 200 + 200 - 55 , row * 200 + 200 - 55), 25)

            elif Board[row][col] == 2 :
                pygame.draw.circle(gameScreen , Black , (int(col * 200+100) , int(row * 200 + 100)), 60 , 15)
#marking square function
def markSquare (row, col , player) :
    Board[row][col] = player


#checking if the sqaure is available
def available_square (row, col) :
    if Board[row][col] == 0 :
        return True
    else :
        return False

#checking win function
def check_win(player) :
    #vertical check
    for col in range(Board_Col):
        if Board[0][col] == player and Board[1][col] == player and Board[2][col] == player :
            draw_vertical_line(col , player)
            return True
    #horizontal check
    for row in range(Board_Rows) :
        if Board[row][0] == player and Board[row][1] == player and Board[row][2] == player :
            draw_horizontal_line(row , player)
            return True
    #asc diagonal check
    if Board[2][0] == player and Board[1][1] == player and Board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    #desc diagonal check
    if Board[0][0] == player and Board[1][1] == player and Board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


#drawing winning lines
def draw_vertical_line(col , player):
    posX = col * 200 + 100
    if player == 1 :
        color = White
    elif player == 2 :
        color = Black
    pygame.draw.line(gameScreen , color ,(posX , 15 ), (posX,H - 15),15)

def draw_horizontal_line(row , player):
    posY = row * 200 + 100
    if player == 1:
        color = White
    elif player == 2:
        color = Black
    pygame.draw.line(gameScreen, color, (15, posY), (W - 15, posY), 15)

def draw_asc_diagonal(player) :
        if player == 1:
            color = White
        elif player == 2:
            color = Black
        pygame.draw.line(gameScreen, color, (15, H - 15), (W - 15, 15), 15)

def draw_desc_diagonal(player) :
    if player == 1:
        color = White
    elif player == 2:
        color = Black
    pygame.draw.line(gameScreen, color, (15,  15), (W - 15,H - 15), 15)

#starting new game function
def restart_game():
    gameScreen.fill(COLOR)
    draw_lines()
    player = 1
    for row in range(Board_Rows):
        for col in range(Board_Col):
            Board[row][col] = 0



player = 1
EndGame = False
draw_lines()


###mainloop###
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not EndGame:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square (clicked_row , clicked_col) :
                if player == 1 :
                    markSquare(clicked_row , clicked_col, 1 )
                    if check_win(player) :
                        EndGame = True
                    player = 2

                elif player == 2 :
                    markSquare(clicked_row , clicked_col , 2 )
                    if check_win(player) :
                        EndGame = True
                    player = 1
                DrawXO()
            #assigning R key to restart the game
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_r :
                restart_game()
                EndGame=False



        pygame.display.update()
