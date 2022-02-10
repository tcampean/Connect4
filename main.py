from Board import *
from Game import *
from UI import *
from Strategies import *
from jproperties import Properties
from os import path
from GUI import *
from Misc import Background, PlayerPiece
import pygame
from pygame import mixer
import pyganim

if __name__ == '__main__':
    configs = Properties()
    with open('settings.properties', 'rb') as config_file:
        configs.load(config_file)
    rows = int(configs.get("rows").data)
    columns = int(configs.get("columns").data)
    board = Board(rows, columns)
    if configs.get("difficulty").data == 'easy':
        strategy = RandomMoves(board)
    elif configs.get("difficulty").data == 'medium':
        strategy = MediumMoves(board)
    else:
        strategy = SmartMoves(board)
    game = Game(board, strategy)
    interface = configs.get("interface").data
    if interface == '' or interface == 'console':
        ui = UI(board, game)
        ui.start()
    else:
        pygame.init()

        square = 100

        width = board.column_count() * square
        height = (board.row_count() + 1) * square
        size = (width, height)
        screen = pygame.display.set_mode(size)
        background = Background("Draws/background_3.jpg", [0, 0])
        grid = Background("Draws/grid_1.jpg", [0, 0])
        screen.blit(background.image, background.rect)
        font = pygame.font.SysFont("arial", 60)
        player_piece = pyganim.PygAnimation(
            [("Draws/red (1).png", 100), ("Draws/red (2).png", 100), ("Draws/red (3).png", 100), ("Draws/red (4).png", 100),
             ("Draws/red (5).png", 100), ("Draws/red (6).png", 100), ("Draws/red (7).png", 100), ("Draws/red (8).png", 100),
             ("Draws/red (9).png", 100), ("Draws/red (10).png", 100), ("Draws/red (11).png", 100), ("Draws/red (12).png", 100),
             ("Draws/red (13).png", 100), ("Draws/red (14).png", 100), ("Draws/red (15).png", 100), ("Draws/red (16).png", 100),
             ("Draws/red (17).png", 100), ("Draws/red (18).png", 100), ("Draws/red (19).png", 100), ("Draws/red (20).png", 100),
             ("Draws/red (21).png", 100), ("Draws/red (22).png", 100), ("Draws/red (23).png", 100), ("Draws/red (24).png", 100),
             ("Draws/red (25).png", 100), ("Draws/red (26).png", 100), ("Draws/red (27).png", 100), ("Draws/red (28).png", 100),
             ("Draws/red (29).png", 100), ("Draws/red (30).png", 100), ("Draws/red (31).png", 100)])
        enemy_piece = pyganim.PygAnimation(
            [("Draws/yellow (1).png", 100), ("Draws/yellow (2).png", 100), ("Draws/yellow (3).png", 100), ("Draws/yellow (4).png", 100),
             ("Draws/yellow (5).png", 100), ("Draws/yellow (6).png", 100), ("Draws/yellow (7).png", 100), ("Draws/yellow (8).png", 100),
             ("Draws/yellow (9).png", 100), ("Draws/yellow (10).png", 100), ("Draws/yellow (11).png", 100), ("Draws/yellow (12).png", 100),
             ("Draws/yellow (13).png", 100), ("Draws/yellow (14).png", 100), ("Draws/yellow (15).png", 100), ("Draws/yellow (16).png", 100),
             ("Draws/yellow (17).png", 100), ("Draws/yellow (18).png", 100), ("Draws/yellow (19).png", 100), ("Draws/yellow (20).png", 100),
             ("Draws/yellow (21).png", 100), ("Draws/yellow (22).png", 100), ("Draws/yellow (23).png", 100), ("Draws/yellow (24).png", 100),
             ("Draws/yellow (25).png", 100), ("Draws/yellow (26).png", 100), ("Draws/yellow (27).png", 100), ("Draws/yellow (28).png", 100),
             ("Draws/yellow (29).png", 100)])
        gui = GUI(board, game)
        gui.start(screen, background, grid, player_piece, enemy_piece, font)
