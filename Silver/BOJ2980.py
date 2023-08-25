N,L = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
num=0
traffic_count = 0
while 1:
    if traffic_count<N and num==lst[traffic_count][0]:
        if cnt%(lst[traffic_count][1]+lst[traffic_count][2])> lst[traffic_count][1]:
            num+=1
            cnt+=1
        else:
            cnt+=lst[traffic_count][1]-cnt%(lst[traffic_count][1]+lst[traffic_count][2])
        traffic_count+=1
    else:
        num+=1
        cnt+=1
    if num==L:
        break

print(cnt)


