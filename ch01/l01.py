def destroy_walls(walls):
    for wall in walls:
        if wall <= 0:
            walls.remove(wall)
    return walls
