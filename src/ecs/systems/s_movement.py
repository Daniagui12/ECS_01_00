import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def system_movement(word: esper.World, dt: float):
    components = word.get_components(CTransform, CVelocity)

    c_v: CVelocity
    c_t: CTransform
    for entity, (c_t, c_v) in components:
        c_t.pos.x += c_v.vel.x * dt
        c_t.pos.y += c_v.vel.y * dt