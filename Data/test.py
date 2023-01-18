lst = [(0, 1), (5, 2), (9, 4), (6, 0), (9, 3)]
print(sorted(lst, key = lambda x: x[1])[-1])