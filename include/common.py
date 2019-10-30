"""============================================================================

  Common functions

============================================================================"""
def calculate_x_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.cos(direction)

def calculate_y_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.sin(direction)