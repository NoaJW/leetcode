# sol = [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]
sol = []


sol.append(sorted([-1, 0, 1]))
sol.append(sorted([-1, 2, -1]))

if sorted([0, 1, -1]) not in sol: 
    print("in there")
else:
    print("not")
# sol.append(sorted([0, 1, -1]))

print(sol)