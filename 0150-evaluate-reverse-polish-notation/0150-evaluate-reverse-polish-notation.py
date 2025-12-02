class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            if token == "+":
                s.append(s.pop() + s.pop())
            elif token == "*":
                s.append(s.pop() * s.pop())
            elif token == "-":
                second, first = s.pop(), s.pop()
                s.append(first - second)
            elif token == "/":
                second, first = s.pop(), s.pop()
                s.append(int(first / second))
            else:
                s.append(int(token))
        
        return s.pop()
        