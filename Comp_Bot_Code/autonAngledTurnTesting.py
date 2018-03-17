from autonBaseInit import *

class autonAngledTurnTesting(autonBaseInit):
    def run(self):
        self.autonMove(1, 5, turnSpeed = .5, turnAngle = 90, radius = 12)
