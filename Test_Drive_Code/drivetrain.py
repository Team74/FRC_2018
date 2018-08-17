import wpilib

class Drivetrain():

    def __init__(self):
        pass

    def drive(self, throtle, wheel, quickturn):
        

    def handledeadband(self, value, deadband):
        return value if abs(value) >= deadband else 0
