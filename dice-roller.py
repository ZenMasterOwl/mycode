red = []
blue = []

for i in range(1,7):
    red.append(f'red {i}')
    blue.append(f'blue {i}')

print(red)
print(blue)

combo = []
for die in red:
    for dice in blue:
        combo.append((die, dice))

print(combo)
