class Solution:
    def clearStars(self, s: str) -> str:
        
        # if "*" not in s:
        #     return s

        # def remove_small(word):
        #     size = len(word)
        #     small_ch = word[-1]
        #     indx_small = size-1
        #     for i in range(size-1,-1,-1):
        #         if  word[i] < small_ch:
        #             small_ch = word[i]
        #             indx_small = i
        #     return word[:indx_small]+word[indx_small+1:]

        # word = ""
        # for ch in s:
        #     if word and ch == '*':
        #         word = remove_small(word)
        #     else:
        #         word +=ch
        # return word

#Time Limit Exceeded
#-----------------------------------------------------------------        
        #aproach 1 pointer minheap (letter), maxheap(indx)


        if "*" not in s:
            return s

        s_num = [ -1 if ch == '*' else ord(ch)-ord("a")  for ch in s ]
        heap = []  #(letter_val , -indx_leter)
        
        for i,ch in enumerate(s_num):
            if heap and ch == -1:
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, (ch,-i))
        
        ans = [-1]*len(s)
        while heap:
            ch,i = heapq.heappop(heap)
            ans[-i] = ch

        return "".join([chr(ch+ord('a')) for ch in ans if ch != -1])
        





        def remove_small(word):
            size = len(word)
            small_ch = word[-1]
            indx_small = size-1
            for i in range(size-1,-1,-1):
                if  word[i] < small_ch:
                    small_ch = word[i]
                    indx_small = i
            return word[:indx_small]+word[indx_small+1:]

        word = ""
        for ch in s:
            if word and ch == '*':
                word = remove_small(word)
            else:
                word +=ch
        return word