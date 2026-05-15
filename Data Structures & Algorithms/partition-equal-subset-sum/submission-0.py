class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            newDp = dp.copy()
            for t in dp:
                if t + nums[i] == target:
                    return True
                newDp.add(t + nums[i])
            dp = newDp
        return False
