class Solution:
    def sortVowels(self, s: str) -> str:


        #bruteforce
        heap = []
        for letter in s:
            if letter in "AEIOUaeiou":
                heapq.heappush(heap,ord(letter))

        new_s = []
        for letter in s:
            if letter in "AEIOUaeiou":
                new_s.append(chr(heapq.heappop(heap)) )
            else:
                new_s.append(letter)

        return "".join(new_s)


        