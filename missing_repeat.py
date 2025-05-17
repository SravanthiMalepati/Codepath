# Python program to find Missing 
# and Repeating in an Array

def findTwoElement(arr):
    n = len(arr)

    # Creating frequency list of size n+1 with
    # initial values as 0. Note that array
    # values will go upto n, that is why we 
    # have taken the size as n+1
    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    # Find the frequency of all elements.
    for i in range(n):
        freq[arr[i]] += 1

    for i in range(1, n + 1):

        # For missing element, frequency
        # will be 0.
        if freq[i] == 0:
            missing = i

        # For repeating element, frequency
        # will be 2.
        elif freq[i] == 2:
            repeating = i

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)

    print(ans[0], ans[1])