#Two players are playing a game of Tower Breakers! Player  always moves first, 
#and both players always play optimally.The rules of the game are as follows:

#- Initially there are n towers.
#- Each tower is of height m.
#- The players move in alternating turns.
#- In each turn, a player can choose a tower of height 'x' and reduce its height 
#to y, where 1 < y < x and y evenly divides x.
#If the current player is unable to make a move, they lose the game.

#Given the values of n and m, determine which player will win. If the 
#first player wins, return 1. Otherwise, return 2.

def towerBreakers(n, m):
    if m == 1:
        return 2
    else:
        return 1 if n % 2 == 1 else 2


if __name__ == '__main__':
    # numero de pruebas
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        
        #numero de torres
        n = int(first_multiple_input[0])
        
        #altura de cada torre
        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)
        print(result)

