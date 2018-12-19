numbers = ['0','1','2','3','4','5','6','7','8','9']

def add(string):
    result = 0
    x = 0
    length = len(string)
    while(x < length):
        if(string[x] in numbers):
            index_start = x
            num_str = ''
            while((x < length) and (string[x] in numbers)):
                num_str += string[x]
                x += 1
            
            try:
                if((index_start > 0) and (string[index_start-1] == '-')):
                    raise
            except:
                print('Negatives not allowed', -int(num_str))
                return
            
            if(int(num_str) > 1000):
                continue
            else:
                result += int(num_str)
        else:
            x += 1
    return result


if __name__ == '__main__':
    string = input();
    print('result = ',add(string))
