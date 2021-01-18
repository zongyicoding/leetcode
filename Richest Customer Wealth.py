class Solution:
    def __init__(self):
        self.record = 0
    def maximumWealth(self, accounts) -> int:
        for i in accounts:
            sum = 0
            for listnumber in i:
                sum = sum + listnumber
            if sum > self.record:
                self.record = sum        
        return self.record

if __name__ == '__main__':
    accounts = [[1,2,3], [3,2,1]]
    ans =Solution().maximumWealth(accounts=accounts)
    print(ans)