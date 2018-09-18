# Jennifer Shelby
# Advanced Operating Systems
# September 3, 2018
# Assignment 1 - CSMA/CD Time-Driven Simulator


#Carrier Class
class Carrier:
    def __init__(self, length):
        self.length = length
        self.messageList = []

    def getLen(self):
        return self.length

    def getMsgList(self):
        return self.messageList

    def addMessage(self, msg):
        self.messageList.append(msg)

    def removeMessage(self, index):
        self.messageList.remove(index)

    def updateMsgList(self, msgList):
        self.messageList = msgList
