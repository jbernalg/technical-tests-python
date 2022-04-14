#Given fiv positive integers, find the minimum and maximum
#values that can be calculated by summing exactly four of 
#the five integers. Then print the respective minimum 
#and maximum values as a single line of two 
#space-separated long integers.

def miniMaxSum(arr):
    sumTotal = sum(arr, 0)
    valSum = []
    
    valSum = []
    valSum = [sumTotal - i for i in arr]
    
    valSum.sort()
    print(f'{valSum[0]} {valSum[len(valSum) - 1]}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)e
