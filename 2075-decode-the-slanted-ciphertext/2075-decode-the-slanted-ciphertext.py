class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        #brute force

        size = len(encodedText)
        col = size//rows

        text = []
        for j in range(col):
            for i in range(rows):
                curr_j = j+i
                if curr_j == col:
                    break
                pos = i*col+curr_j
                text.append(encodedText[pos])
        
        return "".join(text).strip()

                                  

        