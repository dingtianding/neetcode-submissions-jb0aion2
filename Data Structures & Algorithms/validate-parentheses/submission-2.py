class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen: # in the key
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            else:#open
                stack.append(c)

        return True if not stack else False

        