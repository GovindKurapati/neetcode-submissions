class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                perm.append(nums[i]) # choose
                used[i] = True

                backtrack(perm, used) # explore

                perm.pop() # unchoose
                used[i] = False
    
        backtrack([], [False] * len(nums))
        return res