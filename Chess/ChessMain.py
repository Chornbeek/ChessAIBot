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


