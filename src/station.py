# Jennifer Shelby
# Advanced Operating Systems
# September 3, 2018
# Assignment 1 - CSMA/CD Time-Driven Simulator

#Station Class
class Station:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.status = True
        self.delay = 0
        self.latencyList = []

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    # Station Status
    # Boolean that tells whether the station is ready to send
    # True = Ready; False = Not Ready
    def getStatus(self):
        return self.status

    # Station Backoff Counter
    # Counter for number of ticks to backoff sending a msg or sensing carrier
    def getDelay(self):
        return self.delay

    def getLatencyList(self):
        return self.latencyList

    def setStatus(self, status):
        self.status = status

    def setDelay(self, delay):
        self.delay = delay

    def updateLatencyList(self, latency):
        self.latencyList.append(latency)
