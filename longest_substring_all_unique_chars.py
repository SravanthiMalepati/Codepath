"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "happyhalloween"
Output: 5
Explanation: The longest substring is "pyhal", with the length of 5.

Example 2:

Input: s = "trickortreat"
Output: 6
Explanation: The longest substrings are "tricko" or "ickort", both with length 6

UMPIRE:

Understand:
-> substring is contiguous
-> can't have any repeated characters
-> treat all characters the same
-> even if there are multiple strings with a max length, we just return the int

Match:
-> Sliding Window Algorithm

Plan:
-> Keep track of left pointer, right pointer, curMax, isUnique, hash/dict of character counts
-> Sliding Window is...
    -> If window is unique, move right pointer, maybe set curMax?
    -> Else move left pointer
-> curMax

Implement:

Review:
-> Added some edge cases, made sure my tests were passing

Evaluate:

-> Time complexity? 

"abcdefghijklmnopqrstuvwxyzz"

2N iterations of the While loop
O(N)

-> Space complexity?
O(1)
O(N) ??

"""

# Input: s = "happyhalloween"
def longestSubstringAllUniqueChars(s: str) -> int:
    left = 0
    right = 0
    curMax = 0
    charDict = {}
    isUnique = True

    while right < len(s):
        # print(f"left: {left}, right: {right}, curMax: {curMax}, isUnique: {isUnique}")
        # print(f"current substring: {s[0:left]} -> {s[left:right]} <- {s[right:]}")
        # print(charDict)
        # print("")
        # If current window is unique, move right pointer
        if isUnique:
            right += 1
            charDict[s[right - 1]] = charDict.get(s[right - 1], 0) + 1
            if charDict[s[right - 1]] > 1:
                isUnique = False
            else:
                curMax = max(curMax, right - left)
        # Current window is NOT unique, move left pointer
        else:
            charDict[s[left]] = charDict[s[left]] - 1
            left += 1
            # Shoutout to Hushnud who identified the bug in my code!
            if charDict[s[right - 1]] == 1:
                isUnique = True

    return curMax


def runTests() -> None:
    test_cases = [
        {
            "input": "happyhalloween",
            "expectedOutput": 5,  # pyhal
        },
        {
            "input": "trickortreat",
            "expectedOutput": 6,  # tricko / ickort
        },
        {
            "input": "",
            "expectedOutput": 0,
        },
    ]
    for case in test_cases:
        actual = longestSubstringAllUniqueChars(case["input"])
        expected = case["expectedOutput"]

        if actual == expected:
            print("Test success!")
        else:
            print(
                f"""Test failed - {case["input"]} returned {actual}, but expected {expected}"""
            )


if __name__ == "__main__":
    runTests()
