from src.core.engine import GameEngine
import src.core.config as cfg

class Game:
    def __init__(self):
        print("Initialization of the Game begins!")
        self.running = True
        self.gameEngine = GameEngine()
        print("Game initialized")
        
    def run(self):
        print("Game loop!")
        while self.running:
            self.running = self.gameEngine.getEvents()
            
            # handle_input()
            # update()
            # render()
        self.gameEngine.exit()
