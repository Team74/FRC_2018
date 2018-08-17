import wpilib
import ctre

class Motors():
    def __init__(self):
        self.lbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.lfMotor = ctre.wpi_victorspx.WPI_VictorSPX(4)
        self.rfMotor = ctre.wpi_victorspx.WPI_VictorSPX(5)
        self.rbMotor = ctre.wpi_talonsrx.WPI_TalonSRX(1)
