# Jennifer Shelby
# Advanced Operating Systems
# September 3, 2018
# Assignment 1 - CSMA/CD Time-Driven Simulator

# Driver file

import random
import station
import carrier
import message

#Main
def main():
    # Constants
    TIME = 1500
    SIZE = random.randint(16, 24)
    CARRIERLEN = SIZE - 1

    # Variables
    s0 = station.Station("s0", 0)
    s1 = station.Station("s1", 8)
    s2 = station.Station("s2", CARRIERLEN)
    stationList = [s0, s1, s2]
    myCarrier = carrier.Carrier(SIZE)
    seqNum = 0
    messageTotal = 0
    collisionTotal = 0
    success = 0
    average = 0.0
    prop = SIZE
    # Loop on ticks
    for i in range(1, TIME):
        # Loop on station
        for s in range(0, len(stationList)):
            # Status Flag for Station
            flag = True
            # Station delay
            delay = 0
            # Probability for sending a message
            p = random.random()
            # Current station and carrier information
            currentStationStatus = stationList[s].getStatus()
            currentStationName = stationList[s].getName()
            currentStationLoc = stationList[s].getLocation()
            currentStationDelay = stationList[s].getDelay()
            currentMsgList = myCarrier.getMsgList()

            # Check if current station is alreaady on delay
            if(currentStationDelay > 0):
                delay = currentStationDelay - 1
            else:
                # Determine if station is ready to send a message
                if(currentStationStatus and p > 0.9):
                    # Station is ready
                    # Check location of messages on myCarrier
                    if(currentMsgList):
                        for m in range(0, len(currentMsgList)):
                            msgLoc = currentMsgList[m].getLocation()
                            # Collision Occurs
                            if(currentStationLoc == msgLoc):
                                delay = random.randint(1, 24)
                                flag = False
                                collisionTotal = collisionTotal + 1
                    else:
                        # Station sends message
                        messageSize = random.randint(1, 3)
                        delay = messageSize
                        seqNum = seqNum + 1
                        if (currentStationName == "s0"):
                            newMsg = message.Message(seqNum, currentStationName, i, messageSize, 1, currentStationLoc)
                            myCarrier.addMessage(newMsg)
                            messageTotal = messageTotal + 1
                        elif(currentStationName == "s2"):
                            newMsg = message.Message(seqNum, currentStationName, i, messageSize, -1, currentStationLoc)
                            myCarrier.addMessage(newMsg)
                            messageTotal = messageTotal + 1
                        elif(currentStationName == "s1"):
                            newMsg = message.Message(seqNum, currentStationName, i, messageSize, 1, currentStationLoc)
                            newMsg2 = message.Message(seqNum, currentStationName, i, messageSize, -1, currentStationLoc)
                            myCarrier.addMessage(newMsg)
                            myCarrier.addMessage(newMsg2)
                            messageTotal = messageTotal + 2
                        flag = False
                        

                # If station is not ready to send
                if(currentStationStatus and p <= 0.9):
                    delay = random.randint(2, 16)
                    flag = False

            # Update current station
            stationList[s].setDelay(delay)

            # Check if delay is now zero and make sure status updates properly
            if (delay == 0):
                flag = True

            stationList[s].setStatus(flag)

            ### Prints for debugging
            print("Station Name:", currentStationName)
            print("Message Total:", messageTotal)
            print("Collision Total:", collisionTotal)
            print("------------------------------------------------")

        # Update carrier
        carrierMsgList = myCarrier.getMsgList()
        # Only update carrier if there are messages on the line
        if(carrierMsgList):
            for m in carrierMsgList:
                # Remove messages that have propagated
                msgSender = m.getSender()
                msgAlive = m.getAlive()
                msgSize = m.getLength()
                msgDirection = m.getDirection()
                msgStart = m.getStart()
                msgTime = i - msgStart
                if(msgSender == "s0" or msgSender == "s2"):
                    if((msgAlive == CARRIERLEN and msgSize == 1) or (msgAlive == CARRIERLEN+1 and msgSize == 2) or (msgAlive == CARRIERLEN+2 and msgSize == 3)):
                        # Message has propagated, calculate latency
                        latency = prop + (msgSize/msgTime)
                        if(msgSender == "s0"):
                            s0.updateLatencyList(latency)
                        if(msgSender == "s2"):
                            s2.updateLatencyList(latency)
                        # Remove message from carrier
                        #success = success + 1
                        carrierMsgList.remove(m)
                    else:
                        m.updateLocation()
                        m.updateAlive()
                if(msgSender == "s1" and msgDirection < 0):
                    if((msgAlive == 8 and msgSize == 1) or (msgAlive == 9 and msgSize == 2) or (msgAlive == 10 and msgSize == 3)):
                        # Message has propagated, calculate latency
                        latency = prop + (msgSize/msgTime)
                        s1.updateLatencyList(latency)
                        # Remove message from carrier
                        #success = success + 1
                        carrierMsgList.remove(m)
                    else:
                        m.updateLocation()
                        m.updateAlive()
                if(msgSender == "s1" and msgDirection > 0):
                    if((msgAlive == CARRIERLEN - 8 and msgSize == 1) or (msgAlive == CARRIERLEN - 9 and msgSize == 2) or (msgAlive == CARRIERLEN - 10 and msgSize == 3)):
                        # Message has propagated, calculate latency
                        latency = prop + (msgSize/msgTime)
                        s1.updateLatencyList(latency)
                        # Remove message from carrier
                        #success = success + 1
                        carrierMsgList.remove(m)
                    else:
                        m.updateLocation()
                        m.updateAlive()
                # Update message List
                myCarrier.updateMsgList(carrierMsgList)


    # Print message count
    print("Carrier Length:", myCarrier.getLen())
    print("Total Messages Sent: ", messageTotal)
    print("Total Collisions:", collisionTotal)
    success = messageTotal - collisionTotal
    print("Total Successes:", success)
    if(messageTotal == 0):
        messageTotal = 1
    average = success/messageTotal
    print("Average Throughput:", average)
    print("------------------------------------------------")
    
    # Calculate average latency per station
    for n in stationList:
        avgStationLatency = 0
        stationLatency = 0
        stationLatencyList = n.getLatencyList()
        #print("Station ", n.getName(), ": ", stationLatencyList)
        for l in range(0, len(stationLatencyList)):
            stationLatency = stationLatency + stationLatencyList[l]
            
        avgStationLatency = stationLatency/len(stationLatencyList)
        print("Average latency of station", n.getName(), ":", avgStationLatency) 


# Run main
main()

