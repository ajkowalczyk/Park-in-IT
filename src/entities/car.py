"""
Car entity.

Represents the player (and potentially NPC) vehicle.
Stores position, speed, angle and other movement-related data.
"""

# TODO:
# - Position (x, y)
# - Speed and acceleration
# - Rotation / angle
# - Basic update structure

# TODO 
# import src.core.config as cfg
# CAR_MAX_SPEED on default in __init__ maybe? :)

class Car:
    def __init__(self, x = 0, y = 0, speed = 0, angle = 0, width = 1, length = 2):     # angle is AI-Tip which I truly appreciated c:
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.width = width
        self.length = length
