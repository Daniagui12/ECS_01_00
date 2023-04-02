import pygame
import esper
from src.create.load_json import read_json
from src.create.prefab_creator import crear_cuadrado
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.create.spawner_data import SpawnerData

class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.delta_time = 0
        self.ecs_world = esper.World()
        try:
            self.window_info = read_json("././assets/cfg/window.json")["window"]
        except:
            self.window_info = read_json("././assets/cfg/window.json")
        self.enemies_info = read_json("././assets/cfg/enemies.json")
        self.spawn_info = read_json("././assets/cfg/level_01.json")["enemy_spawn_events"]
        self.frame_rate = self._get_framerate()
        self.screen = self._get_screen()
        self.current_time = 0
        self.spawner_data = SpawnerData()

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _get_framerate(self):
        return self.window_info["framerate"]
    
    def _get_screen(self):
        h = self.window_info["size"]["h"]
        w = self.window_info["size"]["w"]
        
        # Set window title
        pygame.display.set_caption(self.window_info["title"])
        return pygame.display.set_mode((w, h), pygame.SCALED)
        
    def _create(self):
        #system_enemy_spawner(self.ecs_world, self.enemies_info, self.spawn_info, self.current_time)
        pass

    def _calculate_time(self):
        self.clock.tick(self.frame_rate)
        self.delta_time = self.clock.get_time() / 1000.0
        self.current_time += self.delta_time

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)
        system_enemy_spawner(self.ecs_world, self.enemies_info, self.spawn_info, self.current_time, self.spawner_data)

    def _draw(self):
        r = self.window_info["bg_color"]["r"]
        g = self.window_info["bg_color"]["g"]
        b = self.window_info["bg_color"]["b"]
        self.screen.fill((r, g, b))
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()


    def _clean(self):
        pygame.quit()
