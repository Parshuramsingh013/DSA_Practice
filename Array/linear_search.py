class Solution:
    def linear_search(self,arr,N,K):
        for i in range(N):
            if arr [i] == K:
                return True
        else:
            return False

arr = [1,2,3,4,8,9]        
s1 = Solution()

result = s1.linear_search(arr, len(arr), 7)
print(result)