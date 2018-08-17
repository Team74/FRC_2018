import wpilib
import Subsystems

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.subsystems = Subsystems()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    teleopInit(self):
        pass

    teleopPeriodic(self):
        self.subsystems.run()
