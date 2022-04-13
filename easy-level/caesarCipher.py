#Julius Caesar protected his confidential information by encrypting it using a cipher. 
#Caesar's cipher shifts each letter by a number of letters. If the shift takes you 
#past the end of the alphabet, just rotate back to the front of the alphabet. 
#In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

#Example
#s = there's-a-starman-waiting-in-the-sky
#k = 3

#The alphabet is rotated by 3, matching the mapping above. The encrypted string is 
#wkhu'v-d-vwdupdp-zdlwlqj-lq-wkh-vnb.

#Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

def caesarCipher(s, k):
    alphabet = list(map(chr, range(97, 123)))
    lk = k - 1
    pal = s
    s = ''

    for i in (pal):
        if i.islower() == False:
            i = i.lower()
            try:
                ndx = alphabet.index(i)
                dif = 25 - ndx
                if dif > lk:
                    ndx = ndx + k
                    s += alphabet[ndx].upper()
                else:
                    ndx = lk - dif
                    s += alphabet[ndx].upper()
            except:
                ndx = -1
                s += i
        else:
            try:
                ndx = alphabet.index(i)
                dif = 25 - ndx
                if dif > lk:
                    ndx = ndx + k
                    s += alphabet[ndx]
                else:
                    ndx = lk - dif
                    s += alphabet[ndx]
            except:
                ndx = -1
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
