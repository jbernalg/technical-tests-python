
def palindromeIndex(s):
    pos = -1
    var =  s[::-1]

    if var in s:
        pos = -1
    else:
        for i in range(len(s)):
            ar = list(s)
            ar.pop(i)
            ra = ar[::-1]
            ar = ''.join(ar)
            ra = ''.join(ra)

            if ra in ar:
                pos = i
                break

    return pos



if __name__ == '__main__':
    q = int(input().strip())
    
    for i in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)
