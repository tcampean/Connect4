from random import randint
import pygame
import sys
import math
from Board import Board
from Game import Game
from main import SmartMoves
from pygame import mixer

class GUI:

    def __init__(self,board,game):
        self._board = board
        self._game = game

    def start(self, screen, background, grid, player_piece, enemy_piece, font):
        mixer.init()
        mixer.music.load("Draws/Paradigm.mp3")
        mixer.music.play()
        mixer.music.set_volume(1.0)
        screen.blit(background.image, background.rect)
        self.draw_board(screen, grid, player_piece, enemy_piece)
        game_over = False
        player_turn = randint(1, 2)
        myfont = font
        clock = pygame.time.Clock()
        places = self._board.column_count() * self._board.row_count()
        while not game_over:
            enemy_piece.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    screen.blit(background.image, background.rect)
                    self.draw_board(screen, grid, player_piece, enemy_piece)
                    x = event.pos[0]
                    if player_turn == 1:
                        player_piece.play()
                        player_piece.blit(screen,(x-50, 0))

                pygame.display.update()
                if places == 0:
                    label = myfont.render("DRAW!!", 1, (255, 255, 255))
                    screen.blit(label, (40, 10))
                    game_over = True


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_turn == 1:
                        x = event.pos[0]
                        col = int(math.floor(x / 100))

                        if self._board._data[0][col] == 0:
                            row = self._board.get_lowest_row(col)
                            self._game.human_move(row,col,1)
                            places -=1

                            if self._game.win_condition(1):
                                label = myfont.render("Player 1 wins!!", 1, (255, 0, 0))
                                screen.blit(label, (40, 10))
                                game_over = True

                            player_turn = 2
                            print(self._board._data)
                            self.draw_board(screen, grid, player_piece, enemy_piece)

            if player_turn == 2 and not game_over:

                col = self._game.computer_move()[0]

                if self._board._data[0][col] == 0:
                    pygame.time.wait(500)
                    row = self._board.get_lowest_row(col)
                    self._game.human_move(row,col,2)
                    places -=1

                    if self._game.win_condition(2):
                        label = myfont.render("Player 2 wins!!", 1, (255, 255, 0))
                        screen.blit(label, (40, 10))
                        game_over = True

                    print(self._board._data)
                    self.draw_board(screen, grid, player_piece, enemy_piece)

                    player_turn = 1
            clock.tick(60)
            pygame.display.update()
            if game_over:
                if self._game.win_condition(2):
                    if self._game.win_condition(2)[4] == 1:
                        pygame.draw.line(screen,(255,0,0),(self._game.win_condition(2)[1]+40,self._game.win_condition(2)[0]+50),(self._game.win_condition(2)[3]+70,self._game.win_condition(2)[2]+50),15)
                        pygame.display.update()
                    elif self._game.win_condition(2)[4] == 2:
                        pygame.draw.line(screen, (255, 0, 0),
                                         (self._game.win_condition(2)[1] + 50, self._game.win_condition(2)[0] + 40),
                                         (self._game.win_condition(2)[3] + 50, self._game.win_condition(2)[2] + 60), 15)
                        pygame.display.update()
                    elif self._game.win_condition(2)[4] == 3:
                        pygame.draw.line(screen, (255, 0, 0),
                                         (self._game.win_condition(2)[1] + 55, self._game.win_condition(2)[0] + 50),
                                         (self._game.win_condition(2)[3] + 55, self._game.win_condition(2)[2] + 50), 15)
                        pygame.display.update()
                    elif self._game.win_condition(2)[4] == 4:
                        pygame.draw.line(screen, (255, 0, 0),
                                         (self._game.win_condition(2)[1] + 55, self._game.win_condition(2)[0] + 50),
                                         (self._game.win_condition(2)[3] + 55, self._game.win_condition(2)[2] + 50), 15)
                        pygame.display.update()
                elif self._game.win_condition(1):
                    if self._game.win_condition(1)[4] == 1:
                        pygame.draw.line(screen,(255,255,0),(self._game.win_condition(1)[1]+40,self._game.win_condition(1)[0]+50),(self._game.win_condition(1)[3]+70,self._game.win_condition(1)[2]+50),15)
                        pygame.display.update()
                    elif self._game.win_condition(1)[4] == 2:
                        pygame.draw.line(screen, (255, 255, 0),
                                         (self._game.win_condition(1)[1] + 50, self._game.win_condition(1)[0] + 40),
                                         (self._game.win_condition(1)[3] + 50, self._game.win_condition(1)[2] + 60), 15)
                        pygame.display.update()
                    elif self._game.win_condition(1)[4] == 3:
                        pygame.draw.line(screen, (255, 255, 0),
                                         (self._game.win_condition(1)[1] + 55, self._game.win_condition(1)[0] + 50),
                                         (self._game.win_condition(1)[3] + 55, self._game.win_condition(1)[2] + 50), 15)
                        pygame.display.update()
                    elif self._game.win_condition(1)[4] == 4:
                        pygame.draw.line(screen, (255, 255, 0),
                                         (self._game.win_condition(1)[1] + 55, self._game.win_condition(1)[0] + 50),
                                         (self._game.win_condition(1)[3] + 55, self._game.win_condition(1)[2] + 50), 15)
                        pygame.display.update()
                mixer.music.set_volume(1.0 - 0.1)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.2)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.3)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.4)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.5)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.6)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.7)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.8)
                pygame.time.wait(300)
                mixer.music.set_volume(1.0 - 0.9)
                pygame.time.wait(300)
                """""
                # sounds worse
                for i in range(1,10):
                    mixer.music.set_volume(1.0 - i/10)
                    pygame.time.wait(300)
                """""

    def draw_board(self, screen,grid,player_piece,enemy_piece):
        for c in range(self._board.column_count()):
            for r in range(1,self._board.row_count() + 1):
                screen.blit(grid.image,(c*100-1,r*100,100,100))

        for c in range(self._board.column_count()):
            for r in range(self._board.row_count()):
                if self._board._data[self._board.row_count() - r - 1][c] == 1:
                    player_piece.blit(screen,(int(c * 100 + 100 / 2-45), (self._board.row_count()+1)*100 - int(r * 100 + 100 / 2)-45))
                elif self._board._data[self._board.row_count() - r - 1][c] == 2:
                    enemy_piece.blit(screen, (int(c * 100 + 100 / 2 - 45),
                                               (self._board.row_count() + 1) * 100 - int(
                                                   r * 100 + 100 / 2) - 45))
        pygame.display.update()



