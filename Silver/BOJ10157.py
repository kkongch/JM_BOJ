C,K = map(int,input().split())
n = int(input())
arr = [[1]*(C+2)]+ [[1]+[0]*C+[1] for _ in range(K)] + [[1]*(C+2)]
if C*K <n:
    print(0)
else:
    directy = [1,0,-1,0]
    directx = [0,1,0,-1]

    cy,cx,dr = 1,1,0
    for i in range(1,n):
        arr[cy][cx] = i

        ny, nx = cy+directy[dr], cx+directx[dr]
        if arr[ny][nx] == 0:
            cy,cx = ny,nx
        else:
            dr = (dr+1) % 4
            cy,cx = cy+directy[dr],cx+directx[dr]
    print(f'{cx} {cy}')