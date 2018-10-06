import wpilib
from subsystem_manager import SubsystemManager

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.subsystemManager = SubsystemManager()
        self.inputManager = InputManager()

    def autonomousInit(self):
        self.subsystemManager.master = SimpleAuton1_Master()#AutonMaster()

    def autonomousPeriodic(self):
        self.subsystemManager.update()

    def teleopInit(self):
        self.subsystemManager.master = TeleopMaster(inputManager)

    def teleopPeriodic(self):
        self.inputManager.update()
        self.subsystemManager.update()
