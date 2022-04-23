
def gridChallenge(grid):
    order_grid = []

    for i in grid:
        #almacena los string ordenados
        order_grid.append(''.join(sorted(i)))

    #elementos del string (j)
    for j in range(len(order_grid[0])):
        #elementos de la lista order_grid (i)
        for i in range(1, len(order_grid)):
            if order_grid[i][j] < order_grid[i-1][j]:
                return 'NO'
    return 'YES'


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
