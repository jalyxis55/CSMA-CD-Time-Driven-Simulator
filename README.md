# CSMA-CD-Time-Driven-Simulator
Time-driven simulation of a carrier with 3 nodes using CSMA/CD


1. If a node is ready to send a message (according to a random probablility, p1) it senses the carrier. The station can only sense the part of the carrier that is directly attached to the station.

    **If the carrier is free, the station starts transmission of a random message (length R2 ticks where 𝑅2 ∈ [1,3])
    **Otherwise, the station delays sensing the carrier by a random number of ticks (R3 where 𝑅3 ∈ [2,16])
    
2. If a station detects collision it stops the current transmission and delays sensing the carrier by a random number of ticks (R4 where 𝑅4 ∈ [1,24])
3. As long as a station is attempting to send a message it does not generate new messages
4. The number and location of stations on the carrier, the carrier length in meters (R5 where 𝑅5 ∈ [16,24]), and the propagation time of a message through the carrier in ticks/meter are given
5. Note that a tick is an abstract atomic time unit. In this assignment we assume that a tick is the time that it takes for a message to propagate a distance of one meter in the carrier. In other words, a message propagates in the carrier at a speed of one meter per tick. 
-------------------------------------------------------------------------------------------------------------------------------------------
Write a TIME Driven simulation of a CSMA/CD scenario with 3 stations {𝑆0, 𝑆1, 𝑆2} assuming that
𝑆0 and 𝑆2 are at the two ends of the carrier and 𝑆1 is at a distance of 8 meters from 𝑆0.

Your program should use a random number generator that generates random numbers in the
range [0, 1] or [0, MAX_RAND] and augment the number as needed to get the ranges specified
below.

    **A station is ready to send a message if 𝑝1 > 0.9
    **𝑅2 ∈ [1,3]; 𝑅3 ∈ [2,16]; 𝑅4 ∈ [1,24]; 𝑅5 ∈ [16,24];

The simulation should run for 1500 ticks and produce a screen-shot (see attached instructions) of
the average throughput (average number of successfully transmitted messages per number of
messages generated) and the average latency in ticks per station.
