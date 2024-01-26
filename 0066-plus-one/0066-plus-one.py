class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        def carry(dig_pos,digits):
            if digits[dig_pos] != 9:
                digits[dig_pos] += 1
            else:
                digits[dig_pos] = 0
                if dig_pos == -len(digits):
                    digits.insert(0,1)
                else:
                    carry(dig_pos-1,digits)
                    
                    
        
        carry(-1,digits)
        return digits
                    
            
            
        
        