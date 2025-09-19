class Spreadsheet:

    def __init__(self, rows: int):
        self.Speadsheet = [ [0]*26  for _ in range(rows+1)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - 65  
        row = int(cell[1:])
        self.Speadsheet[row][col] = value      

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - 65  
        row = int(cell[1:])
        self.Speadsheet[row][col] = 0    
        
    def findcellval(self,address):
        if address[0] not in "0123456789":
            col = ord(address[0]) - 65  
            row = int(address[1:])
            return self.Speadsheet[row][col] 
        else:
            return int(address) 

    def getValue(self, formula: str) -> int:

        val1,val2 = formula[1:].split("+")
        return self.findcellval(val1) + self.findcellval(val2)



        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)