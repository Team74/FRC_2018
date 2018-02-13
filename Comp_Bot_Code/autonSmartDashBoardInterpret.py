import wpilib
from drive import driveTrain
from autonBaseInit import *
from autonCenterEitherSwitch import *
from autonNearScale import *
from autonNearSwitch import *
from autonTwoCubeScale import *
from autonDrive import *
class interpret():
    def autonPass(self,autonCommandNumber, side, switchPosition, scalePosition, driveTrain):
        #autonCommandNumber key, 0 = drive, 1 =  autonNearScale, 2 = autonNearSwitch, 3 = autonCenterEitherSwitch, 4 = autonTwoCubeScale
        drive = self.driveTrain
        if autonCommandNumber == 0:
            return self.autonDrive(side, switchPosition, scalePosition, drive)
        elif autonCommandNumber == 1:
            return self.autonNearScale(side, switchPosition, scalePosition, drive)
        elif autonCommandNumber == 2:
            return self.autonNearSwitch(side, switchPosition, scalePosition, drive)
        elif autonCommandNumber == 3:
            return self.autonCenterEitherSwitch(side, switchPosition, scalePosition, drive)
        elif autonCommandNumber == 4:
            return self.autonTwoCubeScale(side, switchPosition, scalePosition, drive)
        else:
            return self.autonDrive(side, switchPosition, scalePosition, drive)
    def interpret(self):
        drive = self.driveTrain
        side = self.getData(positionChooser)
        fullField = DriveStation.getInstance().getGameSpecificMessage()
        fullField = fullField[:-1]
        switchPosition = fullField[0]
        scalePosition = fullField[1]
        objective = 'emptystring'
        if fullField == 'LL' and side == 'left' or fullField == 'LL' and side == 'center':
            objective = self.getData(switchLscaleL)
            if objective == 'switch':
                if side == 'center':
                    pass
                elif side != 'center':
                    pass

            elif objective == 'scale':
                pass
            elif objective == 'drive':
                pass
        elif fullField == 'LR':
            objective = self.getData(switchLscaleR)
            if objective == 'switch':
                if side == 'center':
                    pass
                elif side != 'center':
                    pass
            elif objective == 'scale':
                pass
            elif objective == 'drive':
                pass
        elif fullField == 'RL':
            objective = self.getData(switchRscaleL)
            if objective == 'switch':
                if side == 'center':
                    pass
                elif side != 'center':
                    pass
            elif objective == 'scale':
                pass
            elif objective == 'drive':
                pass
        elif fullField == 'RR':
            obective = self.getData(switchRscaleR)
            if objective == 'switch':
                if side == 'center':
                    pass
                elif side != 'center':
                    pass
            elif objective == 'scale':
                pass
            elif objective == 'drive':
                pass
        else:
            pass
