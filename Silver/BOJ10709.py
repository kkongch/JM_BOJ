H,W = map(int,input().split())
lst = [list(input()) for _ in range(H)]
for i in range(H):
    cnt = -1
    for k in range(W):
        if lst[i][k]=='c':
            cnt=0
        else:
            if cnt>=0:
                cnt+=1
        lst[i][k]=cnt
    print(*lst[i])