class Solution:
    def minRemoveToMakeValid(self, S):
        S = list(S) 
        stack = []
        for i, c in enumerate(S): 
            if c == ")":
                if stack: 
                        stack.pop()
                else: 
                    S[i] = ""
            elif c == "(":
                stack.append(i)
        for i in stack: 
            S[i] = ""
        return "".join(S)
#S = 'lee(t(c)o)de)'
S = "a)b(c)d"
#S = "))(("

obj = Solution()
print(obj.minRemoveToMakeValid(S)) 