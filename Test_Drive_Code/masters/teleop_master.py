class teleopMaster():
    def __init__(self, subsystemManager_, inputManager_):
        self.subsystemManager = subsystemManager_ #A backreference -- the thing this master is currently controlling
        self.inputManager = inputManager_ #A backreference -- the thing this master is currently controlling
        pass
    def update(self):   #called each frame
        if self.inputManager.ControllerOneInputs['aButton']:
            self.subsystemManager.LiftSubsystem(1,5,10)
