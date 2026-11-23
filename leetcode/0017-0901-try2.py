# Solved
#
class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        answer = 1

        while self.st and self.st[-1][0] <= price:
            answer += self.st.pop()[1]
        self.st.append((price, answer))

        print(self.st)
        return answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


sol = StockSpanner()
print(sol.next(7))
print(sol.next(34))
print(sol.next(1))
print(sol.next(2))
print(sol.next(5))
print(sol.next(3))
print(sol.next(4))