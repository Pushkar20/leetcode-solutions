class Solution:
    def maxArea(self, height: List[int]) -> int:
        pl = 0
        ph = len(height) - 1
        max_water = 0
        while pl != ph:
            water = (ph - pl) * min(height[pl], height[ph])
            # print(f"water: {water}, pl: {pl}, ph: {ph}")
            if water > max_water:
                max_water = water
            
            if height[pl] <= height[ph]:
                pl += 1
            else:
                ph -= 1
        return max_water
