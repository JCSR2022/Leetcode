from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # aproach hashTable
        c = Counter(nums)
        return [key for key,value in c.items() if value >1 ] 
    
    def create_nums(n):
        """ Creat an integer array nums of length n 
        where all the integers of nums are in the range [1, n] 
        and each integer appears once or twice """

        nums = random.sample(range(1,n+1),n)
        #print(nums)
        r = random.randint(0,n//2)
        #print(f"repetitions:{r}")
        repited = random.sample(nums,r*2)
        print(f"repited: {repited[len(repited)//2:]}")
        for i in range(len(repited)//2):
            nums[nums.index(repited[i])] = nums[nums.index(repited[-i-1])]
        return nums
    
    def create_nums2(n):
        nums = random.sample(range(1,n+1),n)
        r = random.randint(0,n//2)
        for i in range(0,r*2,2):
            nums[i] = nums[i+1]
        nums = random.sample(nums,n)
        return nums
     