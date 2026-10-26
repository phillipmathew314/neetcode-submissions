class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = [(position[i], speed[i]) for i in range(len(position))]
        sorted_cars.sort()
        # [(0,1), (3,3), (5,1), (8,4), (10,2)]
        # times = [12, 4, 7]

        times = []
        fleet_count = 1

        for start, speed in sorted_cars:
            finish_time = (target - start) / speed
            times.append(finish_time)

        cur_time = times[-1]
        for i in range(2, len(position)+1):
            if times[-i] > cur_time:
                fleet_count += 1
                cur_time = times[-i]
        
        return fleet_count