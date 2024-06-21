class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        SumSatCus = sum(c for c, g in zip(customers, grumpy) if g == 0)

        UnSatCus = [c if g == 1 else 0 for c, g in zip(customers, grumpy)]

        #print(SumSatCus,UnSatCus)
        
        SumUnSatCus = 0
        for i in range(len(UnSatCus)):
            #print(UnSatCus[i:i+minutes], sum(UnSatCus[i:i+minutes]))
            SumUnSatCus = max(SumUnSatCus,sum(UnSatCus[i:i+minutes]))

      
        
        return SumUnSatCus + SumSatCus