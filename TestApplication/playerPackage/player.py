class Player:
    def __init__(self, name):
        self.name = name
        self.strokes = 0

    def take_shot(self, hole, shot):
        """Simulate taking a shot by decreasing the distance to the hole."""
        hole.update_distance(shot.distance)
        self.strokes += 1
        print(f"{self.name} took a shot of {shot.distance} meters.")

    def __str__(self):
        return f"Player(name={self.name}, strokes={self.strokes})"

    def __repr__(self):
        return f"Player({self.name})"
