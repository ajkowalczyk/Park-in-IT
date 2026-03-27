from src.core.renderer import Renderer
import src.core.config as cfg

class Game:
    def __init__(self):
        self.running = True
        self.renderer = Renderer()
        print("Game initialized")
        

    def run(self):
        while self.running:
            print("Game loop!")


