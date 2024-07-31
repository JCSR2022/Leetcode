class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        #vi dos videos y ni siquera fui capaz de entender las soluciones de los videos:
        #@#%#@$%#$^#$^$#^$%^$%&$%#&
        # https://www.youtube.com/watch?v=nuG66q1E7dI
        # https://www.youtube.com/watch?v=lFYPPPTp8qE
        
        
        #kartikdevsharmaa !!!!!!!!!!!!!!!   
        return self.arrangeBooks(books, shelfWidth)

    def arrangeBooks(self, books: List[List[int]], maxShelfWidth: int) -> int:
        minHeights = [float('inf')] * (len(books) + 1)
        minHeights[0] = 0

        for bookIndex in range(1, len(books) + 1):
            currentShelfHeight = 0
            currentShelfWidth = 0

            for lastBook in range(bookIndex - 1, -1, -1):
                currentBookThickness, currentBookHeight = books[lastBook]

                if currentShelfWidth + currentBookThickness > maxShelfWidth:
                    break

                currentShelfWidth += currentBookThickness
                currentShelfHeight = max(currentShelfHeight, currentBookHeight)

                currentArrangementHeight = minHeights[lastBook] + currentShelfHeight
                minHeights[bookIndex] = min(minHeights[bookIndex], currentArrangementHeight)

        return minHeights[len(books)]
        
        