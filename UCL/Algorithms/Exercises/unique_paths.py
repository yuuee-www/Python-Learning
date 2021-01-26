#Image you have a grid of r rows and c columns. 
# You are standing at the top left corner of a grid (s) and you want to move to a goal (g). 
# You can move through the grid only by moving right or down.  For any two given integers (r,c), 
# how many unique paths exist to get from s to g?
# For a 2x2 grid the answer is 2. You can go down and right, or right and down.

def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1

    return unique_paths(m-1,n) + unique_paths(m,n-1)