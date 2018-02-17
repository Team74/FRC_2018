import wpilib

from autonBaseInit import *

from functools import partial


class AutonInterpreter(autonBaseInit):

    def __init__(self,side, switchPosition, scalePosition, driveTrain):#,   name):
        super().__init__(side, switchPosition, scalePosition, driveTrain)


        #name = "FARSWITCH" #    <-----

        with open("prog_auton.txt") as f:
            name = f.readline().strip()

        self.masterlist = []
        self.default_loc = "/home/lvuser/" #"/home/svanderark/FRC_2018/GUI/convert/"
        with open(self.default_loc + name, "r") as f:
            data = f.readlines()
            i = 0
            del data[0]
            for line in data:
                i += 1
                temp = line[:-1].split(",")
                if temp[0] == "0":
                    self.masterlist.append(partial(self.bloob, self.drive, i, 0, float(temp[1]), float(temp[2]), 0, 0))
                elif temp[0] == "1":
                    turnSpeed = 0.5
                    self.masterlist.append(partial(self.bloob, self.drive, i, 1, 0, 0, float(temp[1]), float(turnSpeed)))
                else:
                    self.masterlist.append(partial(self.bloob, self.drive, i, float(temp[0]), 0,0,0,0))
    def run(self):
        for i in self.masterlist:
            i()

    def bloob(self, a, b, c, d, e, f, g, _h=0, _i=0):
        a.autonMove(b,c,d,e,f,g)
