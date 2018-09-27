import wpilib
from subsystem_manager import SubsystemManager

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.subsystemManager = SubsystemManager()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    teleopInit(self):
        pass

    teleopPeriodic(self):
        self.subsystemManager.run()
