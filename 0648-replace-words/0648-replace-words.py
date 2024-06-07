class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        def removeLongroots(dictionary):
            to_delete = []
            for i,root in enumerate(dictionary):
                for j in range(i+1,len(dictionary)):
                    if root.startswith(dictionary[j]):
                        to_delete.append(i)
                        
            return [ dictionary[i] for i in range(len(dictionary)) if i not in to_delete ]
                
        dictionary  = removeLongroots(dictionary)
        #print(dictionary)
                
        sent = sentence.split()
        
        ans = []
        for word in sent:
            isNotRoot = True
            for root in dictionary:
                #print(word,root)
                if word.startswith(root):
                    ans.append(root)
                    isNotRoot = False
                    break
            if isNotRoot: ans.append(word)
                    
        return " ".join(ans)