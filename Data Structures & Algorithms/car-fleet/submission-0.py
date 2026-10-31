class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #logic for the car fleet
        #we sort based on the position
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        slowest=0
        for p,s in cars:
            #calculate time
            time=(target-p)/s
            if time>slowest:
                #new fleet
                fleet+=1
                #slowest time will now become the current time
                slowest=time
        return fleet