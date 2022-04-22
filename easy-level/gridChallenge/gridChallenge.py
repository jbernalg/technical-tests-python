import string


def gridChallenge(grid):
    alphabet = string.ascii_lowercase
    gridOrder = []

    for i in range(len(grid)):
        s = grid[i]
        print(s)
        print(s[i])
        for j in range(len(grid)):
            if j + 1 < len(grid):
                a = alphabet.index(s[j])
                b = alphabet.index(s[j+1])
                print(a,b)
                if a > b:
                    a = b
                    b = a
                    print(a,b)
                    s.replace(s[j],alphabet[a])
                    s.replace(s[j+1],alphabet[b])
                    print(s)
            else:
                gridOrder.append(s)

    print(gridOrder)


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
