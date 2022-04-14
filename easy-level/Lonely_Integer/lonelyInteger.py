#Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyInteger(a):
    cont = 0
    num = 0
    
    for i in a:
        for j in a:
            if i == j:
                cont += 1
        
        if cont == 1:
            num = i
            break
        cont = 0

    return num


if __name__ == '__main__':

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyInteger(a)
    print(result)

