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
    while running:
        for i in p.event.get():
            if i.type == p.QUIT:
                running = False
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




