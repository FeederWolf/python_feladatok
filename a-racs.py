#Saját megoldás:

def grid_create(row, column): #row-sor,column-oszlop
    grid = []
    for i in range(row):
        grid.append(0)
    for i in range(column):
        print(grid)

grid_create(5, 5)

#video
"""
def grid_create(row, col):
    grid = []
    for y in range(row):
        grid.append([])
        for x in range(col):
            grid[y].append(0)
    return grid

def grid_print(grid):
    for row in grid:
        print(row)

g = grid_create(4, 5)
grid_print(g)
"""