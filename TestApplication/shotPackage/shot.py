class Shot:
    def __init__(self, distance=100):
        self.distance = distance  # Fixed distance for each shot

    def __str__(self):
        return f"Shot(distance={self.distance})"

    def __repr__(self):
        return f"Shot({self.distance})"
