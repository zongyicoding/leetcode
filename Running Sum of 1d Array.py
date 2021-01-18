class Solution:
    def runningSum(self, nums):
        current_sum = 0
        ans = []
        for idx in nums:
            current_sum = current_sum + idx
            ans.append(current_sum)
        return ans

if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    ans = sol.runningSum(nums=nums)
    print(ans)