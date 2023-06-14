class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        start=0

        totalGasAndCost=0
        for i in range(len(gas)):
            totalGasAndCost+=gas[i]-cost[i]
            total+=gas[i]-cost[i]

            if total<0:
                total=0
                start=i+1

        if totalGasAndCost<0:
            return -1

        return start
