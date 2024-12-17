class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        #aproach:
#         hash_letters = defaultdict(int)
        
#         for letter in s:
#             hash_letters[letter] +=1
#         hash_letters = Counter(s)
            
#         letters = list(hash_letters.keys())
#         letters.sort(reverse=True)

#         def find_next_letter(indx):
#             while  indx < len(letters) - 1:
#                 indx += 1
#                 if hash_letters[letters[indx]] > 0:
#                     hash_letters[letters[indx]] -=1
#                     return letters[indx]

#         ans = ""
        
#         for i in range(len(letters)):
#             while hash_letters[letters[i]] > 0:
#                 cant_letters =  hash_letters[letters[i]]
#                 if cant_letters//repeatLimit > 0:
#                     ans += letters[i]*repeatLimit
#                     hash_letters[letters[i]] -= repeatLimit
#                 else:
#                     ans += letters[i]*cant_letters
#                     hash_letters[letters[i]] = 0
                    
#                 next_letter = find_next_letter(i)
#                 if next_letter:
#                     ans += next_letter
#                 else:
#                     return ans
#         return ans

#did not work
#-------------------------------------------------------
        #heap aproach
    
#         hash_letters = Counter(s)
#         heap = [ (-ord(letter),count) for letter,count in  hash_letters.items() ]
#         heapq.heapify(heap)
        
#         ans = []
#         while heap:
#             char_ascii,cnt = heapq.heappop(heap) 
#             print(char_ascii,cnt)
#             char = chr(-char_ascii)
#             current_count = min(cnt,repeatLimit)
#             ans.append(char*current_count)
            
#             #print(cnt,current_count,heap,cnt - current_count > 0 and heap)
#             if cnt - current_count > 0 and heap:
#                 nxt_char_ascii, next_cnt = heapq.heappop(heap) 
#                #print("next:",nxt_char_ascii, next_cnt)
#                 nxt_char = chr(-nxt_char_ascii)
#                 ans.append(nxt_char)
#                 if next_cnt > 2:
#                     heapq.heappush(heap,(nxt_char_ascii,next_cnt-1))
#                 print(heap)
            
#                 heapq.heappush(heap,(char, cnt-current_count))
            
            
#         return "".join(ans)
        
  #$^#$^%$&$&$%&%^*^%(&*)(^*)*&()&*)*()_()P(*)P_*nxt_charO 
#----------------------------------------------------------------------


        pq = [(-ord(k), v) for k, v in Counter(s).items()] 
        heapify(pq)
        ans = []
        while pq: 
            k, v = heappop(pq)
            if ans and ans[-1] == k: 
                if not pq: break 
                kk, vv = heappop(pq)
                ans.append(kk)
                if vv-1: heappush(pq, (kk, vv-1))
                heappush(pq, (k, v))
            else: 
                m = min(v, repeatLimit)
                ans.extend([k]*m)
                if v-m: heappush(pq, (k, v-m))
        return "".join(chr(-x) for x in ans)



