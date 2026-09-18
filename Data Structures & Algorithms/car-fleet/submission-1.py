class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car’s position and speed.
        # Sort by position, closest to the target first.
        # Convert each car into its arrival time.
        # Compare that time with the fleet ahead.
        # Faster or equal arrival means merge; slower arrival means new fleet.

        # (7,1) = 3, (4,2) = 3, (1,2) = 3.5, (0,1) = 10
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        arrivalTime = 0

        for p, s in cars:
            time = (target - p) / s
            if time > arrivalTime:
                fleets += 1
                arrivalTime = time
        
        return fleets
