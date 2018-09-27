import wpilib
from drivetrain_subsystem import Drivetrain
from controller import Controller

class SubsystemManager

    def __init__(self):
        self.drivetrain = Drivetrain()
        self.controllerOne = Controller(0)
        self.controllerTwo = Controller(1)

    def run(self):
        inputsOne = self.controllerOne.getControllerInputs()
        inputsTwo = self.controllerTwo.getControllerInputs()
