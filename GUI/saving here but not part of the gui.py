import math


ROBOT_WIDTH = 1

def getSpeeds(angle, radius, speed=1):
	return [speed, speed*(lambda x: x[1]/x[0])(getDistances(angle, radius))

def getDistances(angle, radius):
	return [(radius + ROBOT_WIDTH/2)*math.radians(angle), (radius - ROBOT_WIDTH/2)*math.radians(angle) ]
