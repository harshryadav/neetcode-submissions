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
turn the position and speed lists into a (position, speed) pair for each car
sort that list on position

create a stack

traverse the sorted pair in reverse order
    compute the time it will take for a given car to get to the target
    using the following formula -> (target-position) / speed
    append that to a stack

    we have to ensure that there are at least two values in the stack
    and also check if the top of the stack's value <= the value underneath it 
        if yes then we pop off the stack

return the length of the stack


The way the loop works is by comparing the time it will take a car to get to the target. If we find that a car in a previous position would take less time to get to the target then we know that it belong to a car fleet since it would eventually hit the car in front of it and have to go at that speed. If, not then it will be a separate car fleet so we only append to the list and do nothing. Since we are only popping when we see a car belong to a fleet, that would give us only unique car fleets in the stack so we can just return the length of the stack to get the count of all car fleets.


Time Complexity: O(nlogn + n) = O(nlogn)
                 O(nlogn) is from sorting the list of pairs
                 O(n) looping through the sorted list of pairs

Space Complexity: O(n) as we are adding cars to our stack
'''


