#Another sorting method, the counting sort, does not require comparison.
#Instead, you create an integer array whose index range covers the entire 
#range of values in your array to sort. Each time a value occurs in 
#the original array, you increment the counter at that index. 
#At the end, run through your counting array, printing the value of each 
# non-zero valued index that number of times.

def countingSort(arr):
    valMax = 100
    matrizf = [0 for i in range(valMax)]
    cont = 0

    for i in range(valMax):
        for j in arr:
            if i == j:
                cont += 1

        matrizf[i] = cont
        cont = 0
    
    return matrizf


if __name__ == '__main__':
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(result)
