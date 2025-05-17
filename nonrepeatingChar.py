from collections import defaultdict, deque

class Stream:
    def __init__(self):
        self.char_count = defaultdict(int)
        self.queue = deque()
    
    def insert(self, char):
        self.char_count[char] += 1
        if self.char_count[char] == 1:
            self.queue.append(char)
        
        # Clean up repeated characters from the front
        while self.queue and self.char_count[self.queue[0]] > 1:
            self.queue.popleft()
    
    def first_unique(self):
        if self.queue:
            return self.queue[0]
        return None


s = Stream()
s.insert('a')
s.insert('b')
# s.insert('a')
print(s.first_unique())  # Output: 'b'
s.insert('b')
s.insert('c')
print(s.first_unique())  # Output: None
