import wpilib
from xbox import XboxController

class Controller():
    def __init__(self, controllerNumber):
        self.controller = XboxController(controllerNumber)

    def getControllerInputs(self):
        inputs = {
        aButton: self.controller.getButtonA()
        bButton: self.controller.getButtonB()
        xButton: self.controller.getButtonX()
        yButton: self.controller.getButtonY()
        rightTrigger: self.controller.getRightTrigger()
        rightButton: self.controller.getRightBumper()
        leftTrigger: self.controller.getLeftTrigger()
        leftButton: self.controller.getLeftBumper()
        rightX: self.controller.getRightX()
        rightY: self.controller.getRightY()
        leftX: self.controller.getLeftX()
        leftY: self.controller.getleftY()
        }
        return inputs
