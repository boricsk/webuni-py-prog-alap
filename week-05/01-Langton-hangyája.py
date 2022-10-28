# https://en.wikipedia.org/wiki/Langton%27s_ant

max_x = 11
max_y = 11

langton_matrix = [[0 for i in range(max_x)] for j in range(max_y)]

hangya_x = 5
hangya_y = 5
hangya_irany = 0 #fölfele irány

while 0 <= hangya_x < max_x and 0 <= hangya_y < max_y: # addig fut a ciklus amig ki nem ér
    if langton_matrix[hangya_y][hangya_x] == 0:
        hangya_irany += 1
    else:
        hangya_irany += 3
    hangya_irany %= 4
    langton_matrix[hangya_y][hangya_x] = 1 - langton_matrix[hangya_y][hangya_x]
    if hangya_irany == 0: #folfele
        hangya_y -= 1
    elif hangya_irany == 1: #jobbra megy
        hangya_x += 1
    elif hangya_irany == 2: #lefele
        hangya_y += 1
    elif hangya_irany == 3: #balra
        hangya_x -= 1
    else:
        assert False #ide nem mehet ?
            
for sor in langton_matrix: 
    print(*sor)
    