class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        # knowledge_dict = { k:v for k,v in knowledge}

        # ans = ""
        # copy = True
        # word = ""
        # for ch in s:
        #     if ch == "(":
        #         copy = False
        #         continue
        #     elif ch == ")":
        #         copy = True
        #         ch = knowledge_dict[word] if word in knowledge_dict else "?"
        #         word = ""

        #     if copy:
        #         ans += ch
        #     else:
        #         word += ch

        # return ans 

#-------------------------------------------------------------------------------------

        # ans1 = s.replace('(','{knowledge[').replace(')',']}')
        # print(ans1)
        # ans2 = defaultdict(lambda:'?',knowledge)
        # print(dict(ans2), (ans2['age'],ans2['jho']))

        # mydict = {"a":"1","b":"2"}
        # test = "L{this_dict[a]} es {this_dict[b]}"
        # ans3 = test.format(this_dict = mydict)
        # print(ans3)

        return s.replace('(','{knowledge[').replace(')',']}').format(knowledge = defaultdict(lambda:'?',knowledge))

        