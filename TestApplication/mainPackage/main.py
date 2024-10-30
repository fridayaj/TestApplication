from holePackage.hole import Hole
from playerPackage.player import Player
from shotPackage.shot import Shot

def main():
    # Create a simple hole, player, and shot
    hole = Hole(par=4, distance=400)
    player = Player(name="Tiger Woods")
    shot = Shot(distance=100)  # Fixed distance for simplicity

    print(hole)
    print(player)
    print(shot)
    
    # Player takes shots until the hole is completed
    while hole.current_distance > 0:
        player.take_shot(hole, shot)
        print(f"Distance remaining: {hole.current_distance} meters")

    print(f"\n{player.name} finished the hole in {player.strokes} strokes")

if __name__ == "__main__":
    main()
