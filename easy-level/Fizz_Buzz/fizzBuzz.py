
def fizzBuzz(n):

    for i in range(1,n + 1):
        
          #Fizz solo divisibles por 3
        if i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        
          #Buzz solo divisibles por 5
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz')

          #FizzBuzz si es divisible por 3 y por 5
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        
        else:
            print(i)

if __name__ == '__main__':
    
    n = int(input().strip())
    
    fizzBuzz(n)
