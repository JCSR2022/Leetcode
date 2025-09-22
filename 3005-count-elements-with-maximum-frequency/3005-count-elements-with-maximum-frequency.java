class Solution {
    public int maxFrequencyElements(int[] nums) {
        
        Map<Integer, Integer> freqMap = new HashMap<>();
        int maxFreq = 0;
        int cntMaxFreq = 0;

        for (int n : nums) {
            freqMap.put(n, freqMap.getOrDefault(n, 0) + 1);
            int freq = freqMap.get(n);

            if (freq > maxFreq) {
                maxFreq = freq;
                cntMaxFreq = freq;  // reset count
            } else if (freq == maxFreq) {
                cntMaxFreq += freq;
            }
        }

        return cntMaxFreq;


    }
}