class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        currstr=''
        currNum=0
        for c in s:
            if c.isdigit():
                currNum=currNum*10+ int(c)
            else:
                if c=="[":
                    stack.append((currstr,currNum))
                    currstr=''
                    currNum=0
                elif c=="]":
                    prevStr,num=stack.pop()
                    currstr=prevStr+num*currstr
                else:
                    currstr+=c
        return currstr
