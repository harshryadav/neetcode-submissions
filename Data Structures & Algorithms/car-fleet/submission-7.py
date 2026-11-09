class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = tuple(sorted(zip(position, speed), reverse=True))
        stack = []
        for car_pos, car_speed in sorted_cars:
            curr_car_dist = (target - car_pos) / car_speed
            stack.append(curr_car_dist)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)



'''
Time Complexity: O(nlogn + n) = O(nlogn), 
                 the O(nlogn) comes from sorting
                 O(n) comes from loop through the sorted tuple pair of position and speed of a car

Space COmplexity: O(n) as we are adding cars to our stack

'''


