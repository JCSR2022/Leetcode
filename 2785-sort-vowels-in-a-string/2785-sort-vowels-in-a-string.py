class Solution:
    def sortVowels(self, s: str) -> str:


        #bruteforce
        # heap = []
        # for letter in s:
        #     if letter in "AEIOUaeiou":
        #         heapq.heappush(heap,ord(letter))

        # new_s = []
        # for letter in s:
        #     if letter in "AEIOUaeiou":
        #         new_s.append(chr(heapq.heappop(heap)) )
        #     else:
        #         new_s.append(letter)

        # return "".join(new_s)

# try improve time
        
        new_s = list(s)
        indx = []
        heap_letter = []

        for i,letter in enumerate(new_s):
            if letter in "AEIOUaeiou":
                heapq.heappush(heap_letter,(ord(letter),letter) )
                indx.append(i)
                
        for i in indx:
            new_s[i] = heapq.heappop(heap_letter)[1]
        
        return "".join(new_s)

        