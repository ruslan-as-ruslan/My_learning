class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        si=ti=0
        while si<len(s) and ti<len(t):
            if s[si]==t[ti]:
                si+=1
            ti+=1   
        return si==len(s)        

    def isSubsequence2(self, s: str, t: str) -> bool:
        fisrt, second = 0, 0

        while (fisrt < len(s) and second < len(t)):
            if s[fisrt] == t[second]:
                fisrt = fisrt+1
                second = second+1
            else:
                second = second+1
        return fisrt == len(s)


if __name__ == "__main__":
    assert Solution().isSubsequence(s="axc", t="ahbgdc") == False
    assert Solution().isSubsequence(s="abc", t="ahbgdc") == True
    assert Solution().isSubsequence2(s="axc", t="ahbgdc") == False
    assert Solution().isSubsequence2(s="abc", t="ahbgdc") == True
    