import wpilib

#import drive#, operatorFunctions, robot

#from drive import driveTrain
from autonBaseInit import *

from functools import partial


class AutonInterpreter(autonBaseInit):

    def __init__(self,side, switchPosition, scalePosition, driveTrain,   name):
        super().__init__(side, switchPosition, scalePosition, driveTrain)
        self.masterlist = []
        self.default_loc = "/home/lvuser/py/convert/" #"/home/svanderark/FRC_2018/GUI/convert/"
        with open(self.default_loc + name, "r") as f:
            data = f.readlines()
            i = 0
            for line in data:
                i += 1
                temp = line[:-1].split(",")
                if temp[0] == "0":
                    self.masterlist.append(partial(self.drive.autonMove, self.drive, i, 0, temp[1], temp[2], 0, 0))
                elif temp[0] == "1":
                    turnSpeed = 0.5
                    self.masterlist.append(partial(self.drive.autonMove, self.drive, i, 1, 0, 0, temp[1], turnSpeed))
                else:
                    self.masterlist.append(partial(self.drive.autonMove, self.drive, i, temp[0], 0,0,0,0))
    def run(self):
        for i in self.masterlist:
            i()


#x = AutonInterpreter(0,0,0,0,"othersave")
