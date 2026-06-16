class Solution:
    def processStr(self, s: str) -> str:
        #brute force


        # ans = []        
        # for ch in s:
        #     if ch == '*':
        #         ans = ans[:-1]
        #     elif ch == "#":
        #         ans += ans
        #     elif ch == '%':
        #         ans = ans[::-1]
        #     else:
        #         ans.append(ch)

        # return  "".join(ans)


#---------------------------------------------



        def append_char(ch):
            return lambda arr: arr + [ch]

        def remove(arr):
            return arr[:-1]

        def duplicate(arr):
            return arr + arr

        def reverse(arr):
            return arr[::-1]

        # Build dispatch table
        hash_func = {ch: append_char(ch) for ch in string.ascii_lowercase}

        hash_func['*'] = remove
        hash_func['#'] = duplicate
        hash_func['%'] = reverse


        ans = []
        for ch in s:
            ans = hash_func[ch](ans)
        return "".join(ans)