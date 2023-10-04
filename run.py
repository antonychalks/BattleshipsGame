# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pprint

def form_grid(x, y):
    """
    Used to create the grid at the size the user has given.
    """
    grid = ""
    for _ in range(rows):
        print("~" * columns)
    
    return grid


grid = form_grid(5, 5)
print(grid)