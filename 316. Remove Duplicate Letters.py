class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = {ch: i for i,ch in enumerate(s)}
        print(rindex)
        result=[]
        for i,ch in enumerate(s):
            if ch not in result:
                while (result and ch < result[-1] and i<rindex[result[-1]]):
                    result.pop()
                result.append(ch)
        return ''.join(result)
