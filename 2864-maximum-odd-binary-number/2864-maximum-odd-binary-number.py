class Solution {
    public String maximumOddBinaryNumber(String s) {
        int ones = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                ones++;
            }
        }

        int zeros = s.length() - ones;

        if (ones == 1) {
            return "0".repeat(zeros) + "1";
        } else {
            return "1".repeat(ones - 1) + "0".repeat(zeros) + "1";
        }
    }
}
