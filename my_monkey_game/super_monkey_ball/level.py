import pymunk

class Level:
    def __init__(self, space, level_data):
        self.static_body = space.static_body
        for segment in level_data:
            segment_shape = pymunk.Segment(self.static_body, segment[0], segment[1], 0.0)
            segment_shape.elasticity = 0.4
            space.add(segment_shape)

    def get_level_data(self):
        #returns level data, for saving, or modifying.
        return self.static_body.shapes

def load_level(filepath):
    #load level from file, and return the level_data
    level_data = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                coord_pairs = line.strip().split(':')
                if len(coord_pairs) == 2:
                    coord1 = tuple(map(int, coord_pairs[0].split(",")))
                    coord2 = tuple(map(int, coord_pairs[1].split(",")))
                    level_data.append((coord1, coord2))
        return level_data
    except FileNotFoundError:
        print("Error: File not found.")
        return [] #return empty list, to prevent further errors

