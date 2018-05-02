# map = [[0 for i in range(4)] for j in range(4)]
# print(map)

map = [[2, 0, 0, 0], [0, 0, 0, 4], [8, 0, 0, 0], [4, 0, 0, 2]]

# ma = [[map[c][r] for c in range(4)] for r in reversed(range(4))]
# print(ma)



ma = [[map[c][r] for r in reversed(range(4))] for c in range(4)]
print(ma)