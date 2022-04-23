import string


def gridChallenge(grid):
    alphabet = string.ascii_lowercase
    gridOrder = []
    n =  len(grid)
    respuesta ='YES'

    for subS in grid:
        #subS son los string de grid
        sN = [] 

        for j in subS:
            index= alphabet.index(j)
            sN.append(index) #lista de indices de subS

        sN.sort() #ordenamiento de indices 
        for ord in sN:
            gridOrder.append(ord)

    for i in range(n):
        if  gridOrder[i] > gridOrder[i+3]:
            respuesta ='NO'
            break
    

    return respuesta


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
