class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        knowledge_dict = { k:v for k,v in knowledge}


        ans = ""
        copy = True
        word = ""
        for ch in s:
            if ch == "(":
                copy = False
                continue
            elif ch == ")":
                copy = True
                ch = knowledge_dict[word] if word in knowledge_dict else "?"
                word = ""

            if copy:
                ans += ch
            else:
                word += ch

        return ans 
                
