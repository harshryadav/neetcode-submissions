class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = tuple(sorted(zip(position, speed), reverse=True))
        stack = []

        if len(sorted_cars) == 1:
            return 1
        for car_pos, car_speed in sorted_cars:
            curr_car_dist = (target - car_pos) / car_speed
            stack.append(curr_car_dist)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        
        return len(stack)

        # for car_pos, car_speed in sorted_tuple:
        #     print(stack)
        #     while stack and car_speed < stack[-1][1]:
        #         print("Top of stack", stack[-1])
        #         # car on top of stack
        #         prev_car_pos, prev_car_speed = stack[-1]
        #         prev_car_dist = (target - prev_car_pos) / prev_car_speed

        #         # i'th car
        #         curr_car_dist = (target - car_pos) / car_speed

        #         if curr_car_dist > prev_car_dist:
        #             stack.pop()
            
        #     if len(stack) == 0:
        #         fleet_count += 1
            
        #     stack.append((car_pos, car_speed))

        # return fleet_count




'''
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3


..........10..
........8....
0...........
.....5........
...3..........



Create a tuple of position and speed
[(10 2), (8 4), (0 1), (5 1), (3 3)]


sorting the tuple by postion would give us
[(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]


We can push to a stack in montonic decreasing order based on the speed



tuple(postion, speed)
sort the tuple by position

fleet_count = -1
loop through the tuple in reverse order
    while the stack is not empty and the speed of the current car > the seep of the car from top of stack
        we calculate if we can create a fleet with the car using this (target - position / speed)
        if the i'th value is greater than the top stack's then we pop off the value from the stack
    

    if the stack is empty increment fleet_count
    
    we push i'th tuple into the stack


'''


