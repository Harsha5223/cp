class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans=[0]*len(heights)
        stack=[]
        for i,height in enumerate(heights):
            while stack and heights[stack[-1]]<=height:
                ans[stack.pop()] +=1
            if stack:
