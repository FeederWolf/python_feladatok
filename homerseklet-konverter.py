def cel_far(c):
    return c * 9/5 + 32
def far_cel(f):
    return round((f - 32) * 5/9, 1)

print(cel_far(40))
print(far_cel(40))