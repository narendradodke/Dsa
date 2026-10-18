
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= 0 else -1
