def int_to_string(num: int) -> str:
    if num == 0:
        return "0"
    negative_flag = num < 0
    num = abs(num)
    arr = []
    while num != 0:
        arr.append(chr(num % 10 + ord('0')))
        num = num // 10
    arr.reverse()
    return "-" + "".join(arr) if negative_flag else "".join(arr) 

print(int_to_string(123))
print(int_to_string(-6714))
