from subsystem_manager import SystemManager

class autonMaster():
    def __init__(self, x):
        self.subsystemManager = x #A backreference -- the thing this master is currently controlling
        pass
    def update(self):   #called each frame
        self.subsystemManager.AutonTurn(10,2)
        self.subsystemManager.LiftSubsystem(1,5,10)
