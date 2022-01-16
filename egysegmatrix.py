from sqlite3 import Row


def matrix_identity(dim):
    mlist = []
    for y in range(dim):
        mlist.append([])
        for x in range(dim):
            if y % dim == x and x % dim == y: #% modulo
                mlist[y].append(1)
            else:
                mlist[y].append(0)
    return mlist
def matrix_print(m):
    for i in m:
        print(i)
m = matrix_identity(4)
matrix_print(m)
