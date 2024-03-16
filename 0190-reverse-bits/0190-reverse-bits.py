class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = str(bin(n))[2:].zfill(32)
        binary_str = binary_str[::-1]
        return int(binary_str, 2)