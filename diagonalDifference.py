#Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    l = len(arr)
    pd = 0
    sd = 0

    for i in range(n):
        pd += arr[i][i]
        sd += arr[i][(n - 1) - i]

    return (abs(pd - sd))


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split()))) #Multilist [[],[],[]]

    result = diagonalDifference(arr)
    print(result)

    #print(arr)
    #print(arr[1][1])
