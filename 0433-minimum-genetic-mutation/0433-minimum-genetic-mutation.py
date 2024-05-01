class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        # aporach   O(n)??
        # run through startGene compare every letter with endGene
        #  safe the index of gene that change , 
        
        # note: order matter, you can do a change in gene n = 100 and then in gene n =3 
        #       it in not the same that doing a change in gene n= 3 and later in gene n=100
        
        
#         gen_change = [ i for i,(s,e) in enumerate(zip(startGene,endGene)) if s != e]


        from queue import Queue
    
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        queue = Queue()
        queue.put((startGene,0))
        visited = {startGene}
        
 
        
        
        while not queue.empty():

            gene,level = queue.get()
            
            if gene == endGene:
                return level
            
            for i in range(len(gene)):
                for letter in'ACGT':
                    new_gene = gene[:i] + letter + gene[i+1:]
                    if new_gene not in visited and new_gene in bank:
                        queue.put((new_gene,level+1))
                        visited.add(new_gene)
        
        return -1
    
    
    
    