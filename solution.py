from itertools import permutations

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    out = []
    inp = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k != n):
                    inp = [i,j,k]
                    out.append(inp)
    
    print(out)
                   
