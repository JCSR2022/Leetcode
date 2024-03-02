class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int left = 0;
        int right = nums.length-1;
        int[] ans = new int[nums.length];
        int i = 0;
        while( left <= right){
            if (Math.abs(nums[left])  >=  Math.abs(nums[right]) ){
                ans[i] = nums[left] * nums[left];
                i +=1;
                left +=1;
            }else{
                ans[i] = nums[right] * nums[right];
                i +=1;
                right -=1;
            }
        }
    
        
        // reverse:
         
        
        for(int j = 0; j < ans.length / 2; j++){
                int temp = ans[j];
                ans[j] = ans[ans.length - j - 1];
                ans[ans.length - j - 1] = temp;
            }    


        return ans;
        
    }
}