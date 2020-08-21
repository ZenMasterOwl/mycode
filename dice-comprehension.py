red = [f'red {i}' for i in range(1,7)]
print(red)
blue = [f'blue {i}' for i in range(1,7)]
print(blue)

combo = [(r_die, b_die) for r_die in red
                            for b_die in blue]
print(combo
