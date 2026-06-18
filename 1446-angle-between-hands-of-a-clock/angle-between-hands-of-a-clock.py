class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        min_deg = (minutes/60)*360
        h_deg = (hour/12)*360 + (minutes/60)*30       
        diff_deg = abs(min_deg-h_deg)

        # print("min_deg:",min_deg)
        # print("h_deg:",h_deg)
        # print("diff_deg:",diff_deg)
        

        return min(diff_deg,360-diff_deg)