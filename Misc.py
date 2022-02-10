import pygame


class Background(pygame.sprite.Sprite):
    """""
    Sprite class for any static picture
    """

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class PlayerPiece(pygame.sprite.Sprite):
    """""
    Animation class for the player piece
    """

    def __init__(self, x, y):
        super().__init__()
        self.animation = True
        self.sprites = []
        self.sprites.append(pygame.image.load("Draws/red (1).png"))
        self.sprites.append(pygame.image.load("red (2).png"))
        self.sprites.append(pygame.image.load("red (3).png"))
        self.sprites.append(pygame.image.load("red (4).png"))
        self.sprites.append(pygame.image.load("red (5).png"))
        self.sprites.append(pygame.image.load("red (6).png"))
        self.sprites.append(pygame.image.load("red (7).png"))
        self.sprites.append(pygame.image.load("red (8).png"))
        self.sprites.append(pygame.image.load("red (9).png"))
        self.sprites.append(pygame.image.load("red (10).png"))
        self.sprites.append(pygame.image.load("red (11).png"))
        self.sprites.append(pygame.image.load("red (12).png"))
        self.sprites.append(pygame.image.load("red (13).png"))
        self.sprites.append(pygame.image.load("red (14).png"))
        self.sprites.append(pygame.image.load("red (15).png"))
        self.sprites.append(pygame.image.load("red (16).png"))
        self.sprites.append(pygame.image.load("red (17).png"))
        self.sprites.append(pygame.image.load("red (18).png"))
        self.sprites.append(pygame.image.load("red (19).png"))
        self.sprites.append(pygame.image.load("red (20).png"))
        self.sprites.append(pygame.image.load("red (21).png"))
        self.sprites.append(pygame.image.load("red (22).png"))
        self.sprites.append(pygame.image.load("red (23).png"))
        self.sprites.append(pygame.image.load("red (24).png"))
        self.sprites.append(pygame.image.load("red (25).png"))
        self.sprites.append(pygame.image.load("red (26).png"))
        self.sprites.append(pygame.image.load("red (27).png"))
        self.sprites.append(pygame.image.load("red (28).png"))
        self.sprites.append(pygame.image.load("red (29).png"))
        self.sprites.append(pygame.image.load("red (30).png"))
        self.sprites.append(pygame.image.load("red (31).png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, speed):
        """""
        Cycles through the images creating an animation
        """
        if self.animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
