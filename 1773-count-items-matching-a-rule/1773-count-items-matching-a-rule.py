class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        for i in range(len(items)):
            if ruleKey =="type":
                if items[i][0] == ruleValue:
                    c += 1
            if ruleKey == "color":
                if items[i][1] == ruleValue:
                    c += 1
            if ruleKey == "name":
                if items[i][2] == ruleValue:
                    c +=1
        return c
