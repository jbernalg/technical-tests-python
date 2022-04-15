
def removeChar(s,n):
    ini = 0
    fin = len(s)
    newWord= s[ini:n] + s[n+1:fin]
    return newWord

def palindromeIndex(s):
    pos = -1
    inv = s[::-1]

    if inv in s:
        pos = -1
    else:
        for i in range(len(s)):
            sin = removeChar(s, i)
            ins = sin[::-1]

            if ins in sin:
                pos = i
                break
    return pos


if __name__ == '__main__':
    q = int(input().strip())
    
    for i in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)
