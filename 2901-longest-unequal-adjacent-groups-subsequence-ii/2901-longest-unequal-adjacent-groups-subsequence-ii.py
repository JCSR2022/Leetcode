class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def is_hamming_distance1(s1,s2):
            if len(s1) != len(s2):
                return False
            hamming = 0
            for ch1,ch2 in zip(s1,s2):
                if ch1 != ch2:
                    hamming +=1
                if hamming > 1:
                    return False
            return True
        
        N = len(words)
        dp = [1]*N
        prev = [-1] * N
        for i in range(N):
            for j in range(i+1,N):
                if groups[i] != groups[j] and is_hamming_distance1(words[i],words[j]):
                    if dp[j] < dp[i] + 1:
                        dp[j] = dp[i] + 1
                        prev[j] = i

        best_i = 0
        for i in range(1,N):
            if dp[i]>dp[best_i]:
                best_i = i
        
        ans = []
        current  = best_i
        while current != -1:
            ans.append(words[current])
            current = prev[current]
        ans.reverse()
        return ans
        





#------------------------------------------------
        # def is_hamming_distance1(s1,s2):
        #     hamming = 0
        #     for ch1,ch2 in zip(s1,s2):
        #         if ch1 != ch2:
        #             hamming +=1
        #         if hamming > 1:
        #             return False
        #     return True
        
        # hash_word_len = defaultdict(list)
        # for i,word in enumerate(words):
        #     hash_word_len[len(word)].append(i)

        # ans = []
        # for size, hwlv in hash_word_len.items():  
        #     N = len(hwlv)
        #     prev = groups[hwlv[0]]
        #     cur_ans = [words[hwlv[0]]
        #     i=1
        #     while i < N:
        #         while i < N and prev==groups[hwlv[i]]:
        #             i+=1
        #         if i < N:
        #             cur_ans.append(words[hwlv[i]])
        #             prev=groups[hwlv[i]]
        #         i+=1
        #     if len(cur_ans) > len(ans):
        #         ans = cur_ans

        # return ans 


        #         ans_indx = [hwlv[i]]
        #         for j in range(i+1,N):
        #             if groups[hwlv[j]] != groups[ans_indx[-1]]:
        #                 if is_hamming_distance1(words[hwlv[j] ],words[ans_indx[-1] ]):
        #                     ans_indx.append(hwlv[j])  
        #         if len(ans_indx) >len(curr_ans):
        #             curr_ans = ans_indx
        #     print("curr_ans",ans_indx,curr_ans)

        # return [words[i] for i in curr_ans]

#simply not good enoghv imbecil!!!!!!!!!!!!!!!
#--------------------------------------------------




#         curr_ans = []
#         for size, hwlv in hash_word_len.items():  
#             print(size,hwlv) 
#             N = len(hwlv)
#             for i in range(N):
#                 ans_indx = [hwlv[i]]
#                 for j in range(i+1,N):
#                     if groups[hwlv[j]] != groups[ans_indx[-1]]:
#                         if is_hamming_distance1(words[hwlv[j] ],words[ans_indx[-1] ]):
#                             ans_indx.append(hwlv[j])  
#                 if len(ans_indx) >len(curr_ans):
#                     curr_ans = ans_indx
#             print("curr_ans",ans_indx,curr_ans)

#         return [words[i] for i in curr_ans]

# #simply not good enoghv imbecil!!!!!!!!!!!!!!!
# #--------------------------------------------------


