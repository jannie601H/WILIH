class deque:
    items = []

    def __init__(self, s):
        for i in s:
            self.items.append(i)
    
    def append(self, s):
        self.items.append(s)
    
    def appendleft(self, c):
        self.items.insert(0, c)

    def pop(self):
        return self.items.pop()
    
    def popleft(self):
        return self.items.pop(0)
    
    def __len__(self):
        return len(self.items)
    
    def right(self):
        return self.items[len(self.items - 1)]
    
    def left(self):
        return self.items[0]
    
def check_palindrome(s):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
    return palindrome

s = input()
print(check_palindrome(s))