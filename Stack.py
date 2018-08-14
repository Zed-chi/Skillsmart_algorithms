class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    def ParenthesesComp(s):
        x = Stack()
        for i in s:
            if i == "(":
                x.push("(")
            else:
                x.pop()
        if x.size() != 0:
            print("не сбалансирована")
        else:
            print("сбалансирована")

    ParenthesesComp("(()((())()))")
    ParenthesesComp("(()()(()")
    ParenthesesComp(")(") #по сути неправильна, но по кол-ву сбалансирована


    def stackCalc(s):
        arr = s.split(" ")
        a = Stack()
        b = Stack()
        z = "+*="
        for i in arr:
            a.push(i)
        while a.size()>0:
            item = a.pop()
            if item not in z:
                b.push(item)
            elif item == "+" and b.size()>1:
                b.push(int(b.pop())+int(b.pop()))
            elif item == "*" and b.size()>1:
                b.push(int(b.pop())*int(b.pop()))
            elif item == "=":
                print(b.pop())

    stackCalc("8 2 + 5 * 9 + =")  # 59
            
            
    """
    2)while stack.size() > 0:
        print(stack.pop()) нормально выведет и уменьшит стек
        print(stack.pop()) выйдет за предел и выведет None
    3) pop O(n)
       push O(1)
    """

