class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:


       
     


        # rec1_bl_x = rec1[0]
        # rec1_bl_y = rec1[1]
        # rec1_tr_x = rec1[2]
        # rec1_tr_y = rec1[3]
        
        # rec2_bl_x = rec2[0]
        # rec2_bl_y = rec2[1]
        # rec2_tr_x = rec2[2]
        # rec2_tr_y = rec2[3]
        
        # if  rec2_bl_x > rec1_tr_x or  rec1_bl_x > rec2_tr_x:
        #     return False
        # else:
        #     if  rec2_bl_y > rec1_tr_y or  rec1_bl_y > rec2_tr_y:
        #         return False
        #     else:
        #         return True

        
#Eres un maldito imbecil , que pierdes tu tiempo, deberias suicidarte!!!!

        return (rec1[0] < rec2[2] and 
                rec2[0] < rec1[2] and 
                rec1[1] < rec2[3] and
                rec2[1] < rec1[3] )