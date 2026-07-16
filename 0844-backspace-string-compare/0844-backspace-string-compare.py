class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in s:
            if i.isalpha():
                stack1.append(i)
            elif len(stack1) == 0:
                a = True
            else:
                stack1.pop()
        a = "".join(stack1)

        stack2 = []
        for i in t:
            if i.isalpha():
                stack2.append(i)
            elif len(stack2) == 0 :
                b = True
            else:
                stack2.pop()
        b = "".join(stack2)

        if a == b:
            return True
        else:
            return False