def minimunBribes(q):
    counter= 0
    for i in range(len(q)-1,0,-1):
        if q[i]!=i+1:
            if q[i-1]==i+1:
                counter +=1
                q[i],q[i-1]= q[i-1],q[i]
            elif q[i-2]==i+1:
                counter +=2
                q[i-2],q[i-1]= q[i-1],q[i-2]
                q[i-1],q[i]= q[i],q[i-1]
            else:
                print('Too chaotic')
                return
    print(counter)


if __name__ == '__main__':
    #proof number
    t = int(input().strip())

    for t_itr in range (t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))

        minimunBribes(q)
