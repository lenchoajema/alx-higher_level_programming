#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

from sys import argv

if __name__ == "__main__":
    len_a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    len_n = int(argv[1])
    if len_n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(len_n):
        len_a.append([i, None])

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        for x in range(len_n):
            if y == len_a[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if already_exists(y):
            return False
        i = 0
        while i < x:
            if abs(len_a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure on"""
        for i in range(x, len_n):
            len_a[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(len_n):
            clear_a(x)
            if reject(x, y):
                len_a[x][1] = y
                if x == len_n - 1:  # accepts the solution
                    print(len_a)
                else:
                    nqueens(x + 1)  # moves on to the next x value to continue

    # start the recursive process at x = 0
    nqueens(0)
