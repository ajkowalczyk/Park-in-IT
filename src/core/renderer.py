"""
Renderer module.

Responsible for drawing the current game state to the screen.

Receives game objects (e.g. Car, World) and translates them
into visual representation using the underlying engine (pygame).

Renderer does NOT contain gameplay logic.
It only handles visual output.

Designed to be replaceable in the future if switching rendering backend
(e.g. pygame → kivy or other frameworks).
"""

# TODO:
# - clear screen
# - draw player car
# - draw environment (grid / obstacles / parking spots)
# - update display (flip / refresh)


class Renderer:
    def __init__(self, pyGameScreen):
        self.gamescreen = pyGameScreen
        print(f"Renderer initialized - {self.gamescreen.get_size()}")