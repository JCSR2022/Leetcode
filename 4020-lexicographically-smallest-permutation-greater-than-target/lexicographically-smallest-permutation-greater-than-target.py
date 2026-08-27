class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:


        # offset = ord("a")
        # count = [0]*26

        # for ch in s:
        #     count[ord(ch)-offset] +=1
        
        # ans = []
        # for ch in target:
        #     indx = ord(ch)-offset
        #     if count[indx] > 0:
        #         count[indx] -=1
        #         ans.append(ch)
        #         continue
        #     else:
        #         break

        # while index < 25 and count[indx] == 0:
        #     index += 1

        # count[indx] -=1
        # ans.append( chr(index + offset  )   )

        # for i in range(26):
        #     while count[i] >0:
        #         ans.append( chr(i + offset  )   )
        #         count[i] -=1

        # if ans == target:
        #     return ""
        # else:
        #     return ans



#no funciona , como cosa rara
#--------------------------------------------------------


        offset = ord('a')

        count = [0] * 26

        # Count letters in s
        for ch in s:
            count[ord(ch) - offset] += 1

        ans = []

        # Try to build target
        for i, ch in enumerate(target):

            index = ord(ch) - offset

            if count[index] > 0:
                count[index] -= 1
                ans.append(ch)
            else:
                break

        else:
            # We built target completely.
            # Now find the smallest permutation greater than target.

            for i in range(len(target) - 1, -1, -1):

                current = ord(target[i]) - offset

                # Return the character used at target[i]
                count[current] += 1
                ans.pop()

                # Find the smallest available character > target[i]
                for j in range(current + 1, 26):

                    if count[j] > 0:

                        ans.append(chr(j + offset))
                        count[j] -= 1

                        # Append remaining letters in sorted order
                        for k in range(26):
                            while count[k] > 0:
                                ans.append(chr(k + offset))
                                count[k] -= 1

                        return ''.join(ans)

            return ""

        # We couldn't match target completely.
        # i is the first position where we failed.

        # Try to make the answer greater at position i
        for j in range(ord(target[i]) - offset + 1, 26):

            if count[j] > 0:

                ans.append(chr(j + offset))
                count[j] -= 1

                # Append remaining letters in sorted order
                for k in range(26):
                    while count[k] > 0:
                        ans.append(chr(k + offset))
                        count[k] -= 1

                return ''.join(ans)

        # We couldn't make it greater at position i.
        # Need to backtrack.
        for pos in range(i - 1, -1, -1):

            current = ord(ans[pos]) - offset

            # Put the previously used character back
            count[current] += 1

            ans.pop()

            # Try a larger character
            for j in range(current + 1, 26):

                if count[j] > 0:

                    ans.append(chr(j + offset))
                    count[j] -= 1

                    for k in range(26):
                        while count[k] > 0:
                            ans.append(chr(k + offset))
                            count[k] -= 1

                    return ''.join(ans)

        return ""

