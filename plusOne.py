def plusOne(digits):
    n = len(digits)
    for i in range(n):
        index = n - 1 - i
        if digits[index] == 9:
            digits[index] = 0
        else:
            digits[index] += 1

            return digits
    return [1] + digits

print(plusOne([3,5,9])) #[3,5,1,0]
print(plusOne([9,9,9])) #[1,0,0,0]