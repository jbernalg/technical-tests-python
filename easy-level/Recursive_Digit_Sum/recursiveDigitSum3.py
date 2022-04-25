def superDigit(n, k):
    sum = 0
    for i in n:
        sum = sum + int(i)*k
    if sum < 10:
        return sum
    return superDigit(str(sum), 1)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    #a string representation of an integer
    n = first_multiple_input[0]
    #the times to concatenate n to make p
    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)
