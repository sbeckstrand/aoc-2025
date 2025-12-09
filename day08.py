import math
import itertools

class JunctionBox():
    id_iter = itertools.count()

    def __init__(self, x: int, y: int, z: int):
        self.id = next(self.id_iter)
        self.circuit = Circuit()
        self.coords = (x, y, z)

        self.circuit.junction_boxes.append(self)
    
    def distance_to(self, other: 'JunctionBox') -> float:
        return math.sqrt((self.coords[0] - other.coords[0]) ** 2 + (self.coords[1] - other.coords[1]) ** 2 + (self.coords[2] - other.coords[2]) ** 2)

class Circuit():
    id_iter = itertools.count()

    def __init__(self):
        self.id = next(self.id_iter)
        self.junction_boxes = []

def get_distances(junction_boxes: list[JunctionBox]) -> list[tuple[JunctionBox, JunctionBox, float]]:
    distances = []
    for junction_box in junction_boxes:
        for other_box in junction_boxes:
            if junction_box != other_box:
                sorted_junction_boxes = sorted([junction_box, other_box], key=lambda box: box.id)
                distances.append((sorted_junction_boxes[0], sorted_junction_boxes[1], junction_box.distance_to(other_box)))
            
    return sorted(list(set(distances)), key=lambda distance: distance[2]) # Return distances of unique pairs (dont return the same pair twice)

def main(data_input: str, pairs: int) -> tuple[int, int]:
    junction_boxes = [JunctionBox(*map(int, line.split(","))) for line in data_input.splitlines()]
    distances = get_distances(junction_boxes)

    circuits = []
    
    for idx, distance in enumerate(distances):
        boxA, boxZ = distance[0], distance[1]
        
        if boxA.circuit != boxZ.circuit:
            
            boxA.circuit.junction_boxes.extend(boxZ.circuit.junction_boxes)
            for junction in boxZ.circuit.junction_boxes:
                junction.circuit = boxA.circuit
            
            if len(boxA.circuit.junction_boxes) == len(junction_boxes):
               p2 = boxA.coords[0] * boxZ.coords[0]

        if idx == pairs:
            
            for junction_box in junction_boxes:
                if junction_box.circuit not in circuits:
                    circuits.append(junction_box.circuit)

            circuits = sorted(circuits, key=lambda circuit: len(circuit.junction_boxes), reverse=True)
            p1 = math.prod([len(circuit.junction_boxes) for circuit in circuits[:3]])

    return (p1, p2)
