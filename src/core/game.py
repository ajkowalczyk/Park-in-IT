from src.core.engine import GameEngine
import src.core.config as cfg

class Game:
    def __init__(self):
        print("Initialization of the Game begins!")
        self.running = True
        self.gameEngine = GameEngine()
        print("Game initialized")
        
    def run(self):
        #while self.running:
            # handle_input()
            # update()
            # render()
        print("Game loop!")
