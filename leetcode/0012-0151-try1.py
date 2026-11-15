# Solved
# 빠르게 풀긴 풀었는데, 상당히 복잡하게 풀었네

class Solution:
    def reverseWords(self, s: str) -> str:

        tmp = ""
        st = []
        for ch in s:
            if ch == " ":
                if len(tmp) > 0:
                    st.append(tmp)
                tmp = ""
            else:
                tmp += ch
        if tmp != "":
            st.append(tmp)

        answer = ""
        n = len(st)
        print(st)
        for i in range(n):
            nxt = st.pop()
            if i == n - 1:
                answer += nxt
            else:
                answer += nxt
                answer += " "

        return answer

# GPT
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.split()
#         words.reverse()
#         return ' '.join(words)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(s.split()[::-1])