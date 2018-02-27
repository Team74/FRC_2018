    def operate(self, leftY, leftX, rightY, rightX, aButton, bButton, xButton, yButton, rightTrigger,rightBumper, leftTrigger, leftBumper, startButton, backButton):
        #Passes inputs from operator controller to the appropriate operator functions
        self.liftTilt(rightBumper, leftBumper)
        self.raiseLowerLift(leftY)
        self.winchUpDown(rightY)
        self.manipulatorIntake(aButton, bButton)
        self.ejectCube(xButton, yButton)
        self.deployClimber(startButton, backButton)

    def manipulatorIntake(self, aButton, bButton):#operator can toggle the intake using A, the intake will run until it detects that it has a cube, or the operator can toggle if off using A
        if aButton and not self.toggle:#If a has been pressed, it will intake cubes
            self.toggle = True
        if bButton and self.toggle:
            self.toggle = False
        if self.toggle:
            self.leftManipulatorMotor.set(-1)
            self.rightManipulatorMotor.set(-1)
        else:
            self.leftManipulatorMotor.set(0)
            self.rightManipulatorMotor.set(0)
    def ejectCube(self, xButton, yButton):#Ejects cube from the manipulator
        if xButton and not self.etoggle:#If a has been pressed, it will intake cubes
            self.etoggle = True
        if yButton and self.etoggle:
            self.etoggle = False
        if self.etoggle:
            self.leftManipulatorMotor.set(-1)
            self.rightManipulatorMotor.set(-1)
        else:
            self.leftManipulatorMotor.set(0)
            self.rightManipulatorMotor.set(0)
