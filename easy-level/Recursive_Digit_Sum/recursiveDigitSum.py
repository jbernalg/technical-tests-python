def superDigit(n, k):
    #print(n*k)
    string_number = n*k
    #number = int(string_number)
    sum = 0
    band = True

    while band:
        for i in string_number:
            sum += int(i)

        if sum < 10:
            band = False
        else:
            string_number = str(sum)
            sum = 0
        
    return sum


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    #a string representation of an integer
    n = first_multiple_input[0]
    #the times to concatenate n to make p
    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)
