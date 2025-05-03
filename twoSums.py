# Worst Solutiion
def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length -1):
            for j in range(i+1, length):
                if(nums[i] != nums[j] and (nums[i] + nums[j] == target) ):
                    return sorted([i,j])
        return []