class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        #brute force , realy brute
        # make a q with friends, value is the most repeted lenguage on 
        #friends that ind do not have 

        # dict_friendships = defaultdict(list)
        # for f1,f2 in friendships:
        #     dict_friendships[f1].append(f2)
        #     dict_friendships[f2].append(f1)

        # for person,friends in dict_friendships.items():
        #     print(person,";",friends)
        #     language_curr_friend = []
        #     for curr_friend in friends:
        #         language_curr_friend.append( (languages[curr_friend-1 ],set(languages[person-1]) & set(languages[curr_friend-1])) )
        #     print(languages[person-1],";",language_curr_friend)

        #-----------------------------------------------------------

        cannot_communicate = set()

        for friend_1,friend_2 in friendships:
            if not any (a==b for a in languages[friend_1-1] for b in  languages[friend_2-1] ):
                cannot_communicate.add(friend_1-1)
                cannot_communicate.add(friend_2-1)

        
        frec_map = defaultdict(int)
        for friend in cannot_communicate:
            for l in languages[friend]:
                frec_map[l] +=1


        return len(cannot_communicate) - max(frec_map.values()) if frec_map.values() else 0