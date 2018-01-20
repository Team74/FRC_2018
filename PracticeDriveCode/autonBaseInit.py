from drive import driveTrain

class autonBaseInit():
    def __init__(self, side, position, driveTrain):
        self.side = side
        self.position = position
        self.drive = driveTrain
        self.moveNumber = 1
