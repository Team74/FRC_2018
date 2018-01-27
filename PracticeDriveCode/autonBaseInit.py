from drive import driveTrain

class autonBaseInit():
    def __init__(self, side, switchPosition, scalePosition, driveTrain):
        self.side = side
        self.switchPosition = switchPosition
        self.scalePosition = scalePosition
        self.drive = driveTrain
        self.moveNumber = 1
