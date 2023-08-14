class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = [0, 0]
        end = [m - 1, n - 1]
        middle = [None, None]

        while (start[0] * n + start[1]) <= (end[0] * n + end[1]):
            start_num = start[0] * n + start[1]
            end_num = end[0] * n + end[1]
            middle_num = start_num + (end_num - start_num) // 2
            middle[0] = middle_num // n
            middle[1] = middle_num % n
            middle_val = matrix[middle[0]][middle[1]]

            if middle_val > target:
                end[0], end[1] = middle
                end[1] -= 1
                if end[1] < 0:
                    end[1] = n - 1
                    end[0] -= 1
            elif middle_val < target:
                start[0], start[1] = middle
                start[1] += 1
                if start[1] == n:
                    start[1] = 0
                    start[0] += 1
            elif middle_val == target:
                return True

        return False

"""Commentary: This problem is just binary search except we have a matrix instead of a list
This runs in O(log(m*n)) because we are halfing the input with each iteration. 
The tricky part is understanding how to find the middle and dealing with out of bounds conditions.
We essentially just convert the index to a coordinate and visa-versa."""