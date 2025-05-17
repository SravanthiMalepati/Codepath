from collections import deque
def wordBreak(s, wordDict):
    words = set(wordDict)
    seen = set()
    q = deque([0])
    while q:
        start = q.popleft()
        # print(s[start])
        if start == len(s):
            return True
        for end in range(start+1,len(s)+1):
            if end in seen:
                continue
            if s[start:end] in words:
                print(s[start:end])
                q.append(end)
                seen.add(end)
    return False

# print(wordBreak("leetcode",["leet","code"]))
# print(wordBreak("applepenapple",["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
