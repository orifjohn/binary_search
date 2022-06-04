class Solution:
    def solve(self, ops):
        stack = []
        try:
            for n in ops:
                if n == "DUP":
                    stack.append(stack[-1])
                elif n == "POP":
                    stack.pop()
                elif n == "-":
                    stack.append(stack.pop() - stack.pop())
                elif n == "+":
                    stack.append(stack.pop() + stack.pop())
                else:
                    stack.append(int(n))
            return stack[-1]
        except:
            return -1
