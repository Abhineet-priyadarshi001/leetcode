class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        count = 0
        for i in operations:
            if i[1:].isnumeric() or i.isnumeric():
                s = int(i)
                stack.append(s)
            elif i == "C":
                stack.pop()
            elif i == "D":
                a = 2 * stack[-1]
                stack.append(a)
            else:
                a = stack[-1] + stack[-2]
                stack.append(a)
        for j in stack:
            count += j
        return count