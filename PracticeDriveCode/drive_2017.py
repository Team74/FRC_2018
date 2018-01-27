


import wpilib
import robotpy_ext
from robotpy_ext.common_drivers.navx.ahrs import AHRS
from wpilib.drive import DifferentialDrive
import ctre
from drive import driveTrain
class driveTrain2017(driveTrain):

    def instantiateMotors(self):
        self.lfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(6)
        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(7)
        self.rfMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)

    def setWheelCircumference(self):
        self.wheelCircumference = 12.5663706144

    def drive(self, leftY, rightY):
        leftY = leftY*-1
        self.lbMotor.set(leftY)
        self.lfMotor.set(leftY)
        self.rfMotor.set(rightY)
        self.rbMotor.set(rightY)

        def autonPivot(self, turnAngle, turnSpeed):
            if self.firstRun:
                self.zeroGyro()
                self.firstRun = False
            if turnAngle < 0:
                if self.getGyroAngle() > turnAngle:
                    self.drive(-turnSpeed, -turnSpeed)
                    return True
                else:
                    self.drive(0,0)
                    self.firstRun = True
                    self.zeroGyro()
                    return False
            elif turnAngle > 0:
                if self.getGyroAngle() < turnAngle:
                    self.drive(turnSpeed, turnSpeed)
                    return True
                else:
                    self.lfMotor.set(0)
                    self.lbMotor.set(0)
                    self.rfMotor.set(0)
                    self.rbMotor.set(0)
                    self.zeroGyro()
                    self.firstRun = True
                    return False
