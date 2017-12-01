if __name__ == '__main__':
    N= int(input())
    
    if N == 1:
        print('m')
    elif (N%2)==0:
        print('invalid')
    else:
        for i in range(N):
            #両端の処理
            line=''
            horizone=['.'] * (N)
            for j in range(N):
                if j==0 or j==(N-1):
                    horizone[j] = 'm'
                elif i > N/2:
                    horizone[j] = '.'
                elif i is j:
                    horizone[j] = 'm'
                elif i is N-1-j:
                    horizone[j] = 'm'
                else:
                    horizone[j] = '.'
            
                line=line+str(horizone[j])
            print(line)
