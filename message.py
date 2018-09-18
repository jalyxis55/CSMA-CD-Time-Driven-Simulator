# Jennifer Shelby
# Advanced Operating Systems
# September 3, 2018
# Assignment 1 - CSMA/CD Time-Driven Simulator

#Message Class
class Message:
    def __init__(self, seqNum, sender, startTime, length, direction, location):
        self.seqNum = seqNum
        self.sender = sender
        self.startTime = startTime
        self.length = length
        self.direction = direction
        self.location = location
        self.alive = 0

    def getSeqNum(self):
        return self.seqNum

    def getSender(self):
        return self.sender

    def getStart(self):
        return self.startTime

    def getLength(self):
        return self.length

    def getDirection(self):
        return self.direction

    def getLocation(self):
        return self.location

    def getAlive(self):
        return self.alive

    def updateAlive(self):
        self.alive = self.alive + 1

    def updateLocation(self):
        self.location = self.location + self.direction
