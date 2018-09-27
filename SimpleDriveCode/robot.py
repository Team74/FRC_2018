import wpilib
import ctre
from xbox import XboxController
class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.controller = XboxController(0)

        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.rfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(0)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)

        self.armMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(4)

        self.rollerMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(5)

        self.lfMotor.setNeutralMode(2)
        self.lbMotor.setNeutralMode(2)
        self.rfMotor.setNeutralMode(2)
        self.rbMotor.setNeutralMode(2)

        self.armMotor.setNeutralMode(2)

        self.rollerMotor.setNeutralMode(2)

        self.left = wpilib.SpeedControllerGroup(self.lfMotor, self.lbMotor)
        self.right = wpilib.SpeedControllerGroup(self.rfMotor, self.rbMotor)
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        throttle = self.controller.getLeftY()
        wheel = self.controller.getRightX()
        leftThrottle = (throttle - wheel) * -1#On 2016 robot Joystick was reading the leftY inverted, foward was - back was positive the bot
        rightThrottle = throttle + wheel#also had the riight and left not synced up
        self.lfMotor.set(leftThrottle)
        self.lbMotor.set(leftThrottle)
        self.rfMotor.set(rightThrottle)
        self.rbMotor.set(rightThrottle)

        if self.controller.getLeftTrigger():
            armPower = -1
        elif self.controller.getRightTrigger():
            armPower = 1
        else:
            armPower = 0
        self.armMotor.set(armPower)

        if self.controller.getLeftBumper():
            rollerPower = -1
        elif self.controller.getRightBumper():
            rollerPower = 1
        else:
            rollerPower = 0
        self.rollerMotor.set(rollerPower)

if __name__ == "__main__":
    wpilib.run(MyRobot)
