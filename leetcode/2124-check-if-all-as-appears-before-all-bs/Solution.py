class Solution:
    def checkString(self, s: str) -> bool:
        #return "ba" not in s  -----simplest

        #loop one
        seen = False
        for i in s:
            if i == 'b':
                seen = True
            elif seen:
                return False #catch
        return True
