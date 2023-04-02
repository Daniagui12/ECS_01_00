import pygame

class CEnemySpawner:
    
    def __init__(self, spawn_time: float, type: str, pos: pygame.Vector2, color: pygame.Color, vel: pygame.Vector2, size: pygame.Vector2, id: int) -> None:
        self.id = id
        self.time = pygame.time.get_ticks()
        self.spawn_time = spawn_time
        self.type = type
        self.pos = pos
        self.color = color
        self.vel = vel
        self.size = size

