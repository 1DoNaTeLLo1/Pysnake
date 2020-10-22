import pygame

class FrameWork:
    def __init__(self, window_size=(500, 500), window_title="FrameWork"):
        pygame.init()

        self.surface = pygame.display.set_mode(window_size)
        pygame.display.set_caption(window_title)

        self.bg_color = (0, 0, 0)

        self.fps_timer = pygame.time.Clock()
        self.fps = 60
        self.dt = 0.

    def set_title(self, new_title):
        pygame.display.set_caption(new_title)

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def logic(self):
        pass

    def draw(self):
        pass

    def run(self):
        while True:
            self.dt = self.fps_timer.tick(self.fps) / 1000.
            self.get_input()
            self.logic()
            self.surface.fill(self.bg_color)
            self.draw()
            pygame.display.update()