class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        #Aproach:
        # 1 insert max words per line per line cointing the letters and 1 space for between words"
        
        
        def adjustline(line):
            
            if len(line) > 1:
                cont_words = (len(line)-1)
                cont = sum([ len(word) for word in line])
                reman_spaces =  maxWidth - cont

                spaces = [" " * (reman_spaces//cont_words)]*cont_words

                if reman_spaces%cont_words != 0:
                    for i in range(reman_spaces%cont_words):
                        spaces[i] += " "

                newLine = ""
                for i,space in enumerate(spaces):
                    newLine +=line[i]
                    newLine += space
                newLine += line[-1]
                return newLine
            else:
                newLine = line[0] +" " * (maxWidth-len(line[0]))
                return newLine
        
        
            


        lines = []
        line = []
        
        cont = 0 
        for word in words:
            
            cont += len(word)
            print(word, line, lines,cont)
            if cont <= maxWidth:
                line.append(word)
                cont +=1 
                
            else:
                lines.append(adjustline(line))    
                line = [word]
                cont = len(word)+1
        
        
        last_line = " ".join(line) +" " * (maxWidth-sum([len(w) for w in line])-(len(line)-1) )
        
        lines.append(last_line)
       
        return lines
            
        
        