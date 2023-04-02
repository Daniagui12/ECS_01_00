import pygame
import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_surface import CSurface
from src.create.prefab_creator import crear_cuadrado
from src.create.spawner_data import SpawnerData

def system_enemy_spawner(world: esper.World, enemies_info: dict, spawn_info: dict, time: float, spawner_data: SpawnerData):
    ids = 0
    for enemy in enemies_info:
        for spawn in spawn_info:
            if enemy == spawn["enemy_type"]:
                enemy = enemies_info[enemy]
                world.create_entity(
                    CEnemySpawner(
                        id=ids,
                        spawn_time=spawn["time"],
                        type=spawn["enemy_type"],
                        pos=pygame.Vector2(spawn["position"]["x"], spawn["position"]["y"]),
                        color=pygame.Color(enemy["color"]["r"], enemy["color"]["g"], enemy["color"]["b"]),
                        vel=pygame.Vector2(enemy["velocity_min"], enemy["velocity_max"]),
                        size=pygame.Vector2(enemy["size"]["x"], enemy["size"]["y"])
                    )
                )
                ids += 1

    # If the time is greater than the spawn time
    for entity, c_spawner in world.get_component(CEnemySpawner):
        if time >= c_spawner.spawn_time and c_spawner not in spawner_data.enemies and c_spawner.id not in spawner_data.enemies_ids:
            # Spawn an enemy
            crear_cuadrado(world, c_spawner.pos, c_spawner.size, c_spawner.vel, c_spawner.color)
            # Reset the time
            c_spawner.time = time
            # Add the enemy to the spawner data
            spawner_data.add_enemy(c_spawner)
            # Add enemy id to the spawner data
            spawner_data.add_enemy_id(c_spawner.id)
            





