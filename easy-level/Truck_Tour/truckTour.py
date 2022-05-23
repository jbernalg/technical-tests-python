def truckTour(petrolpumps):
    


if __name__ == '__main__':
    
    n = int(input().strip())

    petrolpumps = []

    for i in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
    print(result)
