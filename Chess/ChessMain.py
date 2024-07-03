# This is our main driver file. It will be responsible for handling user input and displaying current GameState object.

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 400
DIMENSION = 8 # Dimensions 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # Animations later on
IMAGES = {}


# Initialize a global dictionary of images. This will be called exactly once in the main
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

# This will be main driver for our code. This will handle user input and updating the graphics
#Test2
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)
    load_images()
    running = True
    sqSelected = () # No square is selected, keep track of the last click of the user (tuple: row, col)
    playerClicks = [] # Keep track of the player clicks (two tuples: [(6,4)], to (4,4)])
    while running:
        for i in p.event.get():
            if i.type == p.QUIT:
                running = False
            elif i.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # x,y location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col): # The user clicked the same square twice (invalid move)
                    sqSelected = () # Deselect
                    playerClicks = [] # Clear player clicks
                else: # (Valid move)
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # Append for both 1st and 2nd clicks
                if len(playerClicks) == 2: # After 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board) # [0] represents starting square, [1] represents end square
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # Reset user clicks
                    playerClicks = []



        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen,gs):
    drawBoard(screen) # Draw the squares on board

    drawPieces(screen, gs.board) # Draw pieces on top of those squares


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("pink")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))



def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))





if __name__ == "__main__":
    main()




