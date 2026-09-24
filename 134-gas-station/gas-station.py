class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total=0
        tank=0
        start=0

        for i in range(len(gas)):
            fuel = gas[i] - cost[i]
            total+=fuel
            tank+=fuel

            if tank<0:
                start=i+1
                tank=0

        if total>=0:
            return start

        else:
            return -1

        