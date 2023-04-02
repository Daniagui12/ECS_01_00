from src.ecs.components.c_enemy_spawner import CEnemySpawner


class SpawnerData:

    def __init__(self):
        self.enemies = []
        self.enemies_ids = []

    def add_enemy(self, enemy: CEnemySpawner):
        self.enemies.append(enemy)

    def add_enemy_id(self, enemy_id: int):
        self.enemies_ids.append(enemy_id)

    def get_enemy(self, enemy_id: int):
        for enemy in self.enemies:
            if enemy.id == enemy_id:
                return enemy
        
        return None

    def remove_enemy(self, enemy_id: int):
        self.enemies.pop(enemy_id)
    