class Hole:
    def __init__(self, par, distance):
        self.par = par
        self.distance = distance
        self.current_distance = distance  # Distance remaining for the player

    def update_distance(self, shot_distance):
        """Reduce the remaining distance by the distance of a shot, down to zero."""
        self.current_distance = max(0, self.current_distance - shot_distance)

    def __str__(self):
        return f"Hole(par={self.par}, distance={self.distance})"

    def __repr__(self):
        return f"Hole(par={self.par}, distance={self.distance})"
