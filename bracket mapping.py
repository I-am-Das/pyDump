class Solution(object):
    def isValid(self, s):
        stack = []
        b= {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in b.values():
                stack.append(char)
            elif char in b:
                if not stack or stack.pop() != b[char]:
                    return False
            else:
                return False 

        return not stack
