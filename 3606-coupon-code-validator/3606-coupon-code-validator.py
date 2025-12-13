class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        # def is_valid_code(s: str) -> bool:
        #     return bool(re.fullmatch(r'\w+', s))
 

        def is_valid_code(s: str) -> bool:
            #string.ascii_letters
            if len(s) == 0: return False
            #valids ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
            for ch in s:
                if ch not in valids:
                    return False
            return True


        def is_valid_code(s: str) -> bool:
            #string.ascii_letters
            if not s: return False
            
            valids ={'F', 'p', 'N', 'P', 'h', 'E', 'g', 'm', 'H',
             'X', 'o', 'K', 'G', 'v', 's', 'c', 'A', 'I', 'r', 'C',
              'n', 'd', 'z', '9', 'a', 'T', 'W', 'i', 'V', 'x', 'q', 
              '1', 'f', 'Y', 'y', '0', '2', 'M', '3', 'e', 'j', 'b',
               'u', 'J', '5', 'l', 'O', 'w', '6', '7', 'U', 'R', 'k', 
               'L', 'Z', '8', '4', '_', 'D', 'Q', 'B', 't', 'S'}

            return all(ch in valids for ch in s)



        # def is_valid_code(s: str) -> bool:
        #     if not s:
        #         return False
        #     return all(ch.isalnum() or ch == '_' for ch in s)

        def is_valid_business(s:str) ->bool:
            return s in {"electronics", "grocery", "pharmacy", "restaurant"}


        ans = {"electronics":[],"grocery":[],"pharmacy":[],"restaurant":[]}
        for i in range(len(code)):
            if (  is_valid_code(code[i]) and 
                  is_valid_business(businessLine[i]) and
                  isActive[i] ):
                
                ans[businessLine[i]].append(code[i])

        final_ans = []
        for businessLine in ["electronics", "grocery", "pharmacy", "restaurant"]:
            ans[businessLine].sort(reverse=False)
            final_ans += ans[businessLine]

        return final_ans