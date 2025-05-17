# Python program to add 1 to a
# number represented as an array

def addOne(arr):

  
    carry = 1

    for i in range(len(arr) - 1, -1, -1):
        sum = arr[i] + carry
        arr[i] = sum % 10
        carry = sum // 10

    if carry:
        arr.insert(0, carry)

    return arr

# Driver code
if __name__ == "__main__":
    arr = [9, 9, 9]
    res = addOne(arr)
    for i in res:
        print(i, end="")