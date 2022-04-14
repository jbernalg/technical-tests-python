#Given an array of integers, calculate the ratios of its elements 
#that are positive, negative, and zero. 
#Print the decimal value of each fraction on 
#a new line with 6 places after the decimal.
def plusMinus(arr):
    contPos = 0
    contNeg = 0
    contZero = 0

    for i in arr:
        if i > 0:
            contPos += 1
        elif i < 0:
            contNeg += 1
        else:
            contZero += 1

    Pos = contPos/len(arr)
    Neg = contNeg/len(arr)
    Zero = contZero/len(arr)

    print('{:.6f}'.format(Pos))
    print('{:.6f}'.format(Neg))
    print('{:.6f}'.format(Zero))


if __name__ == '__main_':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
