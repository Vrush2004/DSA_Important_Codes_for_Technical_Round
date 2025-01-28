# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        tank = 0
        start_station = 0

        # Iterate over all stations
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            # If tank is negative, reset the starting station
            if tank < 0:
                start_station = i + 1
                tank = 0

        # If total gas is less than total cost, it's not possible to complete the circuit
        return start_station if total_gas >= total_cost else -1