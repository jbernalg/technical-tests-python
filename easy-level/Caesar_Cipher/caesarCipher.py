import string

def caesarCipher(s, k):
    alphabetm = string.ascii_lowercase
    alphabetM = alphabetm.upper()
    pal = s
    s = ''

    for i in pal:
        
        if i in alphabetm:
            a = alphabetm.index(i)
            b = a + k
            if b < len(alphabetm):
                s += alphabetm[b]
            else:
                pos = b % 26
                s += alphabetm[pos] 
        
        elif i in alphabetM:
            a = alphabetM.index(i)
            b = a + k
            if b < len(alphabetM):
                s += alphabetM[b] 
            else:
                pos = b % 26
                s += alphabetM[pos]
        else:
            s += i

    return s


if __name__ == '__main__':
    #numero de caracteres de la frase
    n = int(input().strip())

    #frase
    s = input()

    #numero de rotacion
    k = int(input().strip())

    result = caesarCipher(s,k)
    print(result)
