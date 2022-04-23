import string


def gridChallenge(grid):
    alphabet = string.ascii_lowercase
    gridOrder = []
    sr =''

    for subS in grid:
        #subS son los string de grid
        sN = [] 

        for j in subS:
            index= alphabet.index(j)
            sN.append(index) #lista de indices de subS

        sN.sort() #ordenamiento de indices de mayor a menor

        for ord in sN:
            #sr es el string ordenado alfabeticamente
            sr += alphabet[ord]

        gridOrder.append(sr)
        sr = ''
    
    return gridOrder


if __name__ == '__main__':
    #number of case
    t = int(input().strip())

    for t_itr in range(t):
        #number of elements
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
