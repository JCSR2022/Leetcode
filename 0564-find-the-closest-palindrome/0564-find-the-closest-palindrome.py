class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        #i am not even trying to undersatand today. 
        
        return (l:=len(n),p:=int(n[:(l+1)//2])) and str(min({10**(l-1)-1,10**l+1,*(int((t:=str(p+q))+t[-1-l%2::-1]) for q in (-1,0,1))}-{n:=int(n)},key=lambda v:(abs(v-n),v)))
        
#         number = int(numberStr)
#         if number <= 10:
#             return str(number - 1)
#         if number == 11:
#             return "9"

#         length = len(numberStr)
#         leftHalf = int(numberStr[:(length + 1) // 2])
        
#         palindromeCandidates = [
#             self.generatePalindromeFromLeft(leftHalf - 1, length % 2 == 0),
#             self.generatePalindromeFromLeft(leftHalf, length % 2 == 0),
#             self.generatePalindromeFromLeft(leftHalf + 1, length % 2 == 0),
#             10**(length - 1) - 1,
#             10**length + 1
#         ]

#         nearestPalindrome = 0
#         minDifference = float('inf')

#         for candidate in palindromeCandidates:
#             if candidate == number:
#                 continue
#             difference = abs(candidate - number)
#             if difference < minDifference or (difference == minDifference and candidate < nearestPalindrome):
#                 minDifference = difference
#                 nearestPalindrome = candidate

#         return str(nearestPalindrome)

#     def generatePalindromeFromLeft(self, leftHalf: int, isEvenLength: bool) -> int:
#         palindrome = leftHalf
#         if not isEvenLength:
#             leftHalf //= 10
#         while leftHalf > 0:
#             palindrome = palindrome * 10 + leftHalf % 10
#             leftHalf //= 10
#         return palindrome
        