class Solution:
    def findUnion(self, a, b):
        n1 = len(a)
        n2 = len(b)
        i = 0
        j = 0
        output = []

        while i < n1 and j < n2:
            if a[i] <= b[j]:
                if len(output) == 0 or output[-1] != a[i]:
                    output.append(a[i])
                i += 1
            else:
                if len(output) == 0 or output[-1] != b[j]:
                    output.append(b[j])
                j += 1

        while i < n1:
            if len(output) == 0 or output[-1] != a[i]:
                output.append(a[i])
            i += 1
        
        while j < n2:
            if len(output) == 0 or output[-1] != b[j]:
                output.append(b[j])
            j += 1
        
        return output
    
s1 = Solution()

a = [1, 2, 4, 5, 6]
b = [2, 3, 5, 7]

result = s1.findUnion(a,b)
print(result)