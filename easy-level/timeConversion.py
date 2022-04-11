#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

def timeConversion(s):
    
    time = ' '

    if s[-2].lower() == 'a':
        if s[:2] == '12':
            time = '00'+ s[2:8]
        else:
            time = s[:8]
    elif s[-2].lower() == 'p':
        if s[:2] == '12':
            time = s[:8]
        else:
            hora = int(s[:2]) + 12
            time = str(hora) + s[2:8]
    
    return time



if __name__ == '__main__':
    
    s = input()
    result = timeConversion(s)
    print(result)
