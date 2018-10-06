from utils.controller import Controller

class inputsManager():
    def __init__(self):
        self.controllerOne = Controller()
        self.controllerTwo = Controller()

        self.controllerOneInputs = None
        self.controllerTwoInputs = None

    def update(self):
        self.controllerOneInputs = self.controllerOne.getControllerInputs()
        self.controllerTwoInputs = self.controllerTwo.getControllerInputs()
