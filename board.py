import pygame
import sprite

TYPE_FIELD, TYPE_WALL = 0, 1


class Board():

    def __init__(self, size, shape=(9, 9)):
        self.shape = shape  # default 9 by 9
        print("shape", self.shape)
        self.size = size  # actual size in pixels

        self.field_size = self.size[0] / 9, self.size[1] / 9
        self.map = [[Field(self.field_size) for col in range(self.shape[1])]
                    for col in range(self.shape[1])]

    def draw(self):
        surf = pygame.Surface(self.size)
        surf.fill((255, 255, 255))

        # draw grid as background
        for row, _ in enumerate(self.map):
            for col, _ in enumerate(_):
                w, h = self.field_size
                rect = pygame.Rect(col * w, row * h, w, h)
                pygame.draw.rect(surf, (100, 100, 100), rect, 1)

        # draw fields on top of it
        for row, _ in enumerate(self.map):
            for col, field in enumerate(_):
                x, y = col * self.field_size[0], row * self.field_size[1]
                surf.blit(field.image, (x, y))
        return surf

    def on_event(self, event=None):
        pass


class Field(sprite.Sprite):

    def __init__(self, size, type=TYPE_FIELD, team=None):
        super(Field, self).__init__(size)
        self.type = type

    def draw(self):
        self.surface.fill(self._bgcolor())

    def _bgcolor(self):
        if self.type == TYPE_FIELD:
            return (0, 0, 0, 0)  # reset everything
        elif self.type == TYPE_WALL:
            return (150, 50, 50, 250)
