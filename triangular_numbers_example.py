# Practice with performance of nested loops!

# Exactly N^2 operations, so O(N^2)
def nestedLoop1(n: int):
    do_something = 0
    for i in range(0, n):
        for j in range(0, n):
            do_something += 1
    print(do_something)


# Number of operations here is represented by the Triangular Numbers
# Exactly n(n+1)/2 operations, still a O(N^2)
def nestedLoop2(n: int):
    do_something = 0
    for i in range(0, n):
        for j in range(i, n):
            do_something += 1
    print(do_something)


if __name__ == "__main__":
    nestedLoop2(n=3)

"""
Nested Loop #1:
1 2 3
1 4 9

x x x
x x x
x x x

Nested Loop #2:
1 2 3 4  5
1 3 6 10 15

1 + 2 + 3 + 4 + ... + n-1 + n

x x x
x x
x

Triangular numbers are n(n+1)/2
"""
