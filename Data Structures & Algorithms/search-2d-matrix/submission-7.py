class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        def search(nums: List[int], target: int) -> bool:
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return False

        while left <= right:
            mid_row = (right + left) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][len(matrix[mid_row])-1]:
                return search(matrix[mid_row], target)
            elif matrix[mid_row][len(matrix[mid_row])-1] > target:
                right = mid_row - 1
            else:
                left = mid_row + 1
        
        return False

        # if not matrix or not matrix[0]:
        #     return False

        # rows, cols = len(matrix), len(matrix[0])
        # left, right = 0, (rows * cols) - 1

        # while left <= right:
        #     mid = left + (right - left) // 2
            
        #     # Virtual 1D index mapped to 2D coordinates
        #     r = mid // cols
        #     c = mid % cols
        #     val = matrix[r][c]

        #     if val == target:
        #         return True
        #     elif val < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return False
    
'''
check the first and last value of a row, if target is withing that then perform binary search on that list

left = 0
right = matrix.length

while left <= right
    compute middle row --> mid = (right + left) // 2

    if matrix[mid][0] <= target <= matrix[mid][end]
        perform binary search serach on that list

    if target < matrix[mid][end]
        then check right/bottom matrix
        right = mid - 1

    else
        check left/top matrix
        left = mid + 1


Time Complexity: O(log(M * N))
The algorithm runs in O(log(M * N)) time by performing two sequential binary searches. First it halves the M rows which is in O(log M) time and then it halves the N columns of the matching row in O(log N)

Space Complexity: O(1) as we only track a few integer pointers without copying the matrix


'''