class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        run_tot=0
        for i in nums:
            if i-1 not in num_set:
                cnt=1
                while i + cnt in num_set:
                    cnt+=1
                run_tot=max(run_tot,cnt)
        return run_tot