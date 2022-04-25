def superDigit(n, k):
    return (k * int(n) - 1) % 9 + 1


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    #a string representation of an integer
    n = first_multiple_input[0]
    #the times to concatenate n to make p
    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)
