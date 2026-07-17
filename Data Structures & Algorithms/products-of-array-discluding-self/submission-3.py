# [1, 2, 3, 4]
# [2 * 3 * 4, 1 * 3 * 4, 1 * 2 * 4, 1 * 2 * 3]
# [0, 1, 2, 3]
# [ 24, 12, 8, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        indexZero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros = zeros + 1
                indexZero = i
        if zeros > 1:
            return [0] * len(nums)
        
        if zeros == 1:
            out = [0] * len(nums)
            product = 1
            for i in range(len(nums)):
                if i != indexZero:
                    product = product * nums[i]
            out[indexZero] = int(product)
            return out


        product = 1
        for i in nums:
            product = product * i

        output = []

        for i in nums:
            output.append(int(product / i))

        return output

        