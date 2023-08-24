row, col = map(int, input().split())
shop = int(input())
shop_location = [list(map(int, input().split())) for _ in range(shop)]
x = list(map(int, input().split()))
result = []
Round = 2 * row + 2 * col

def len_check(loc, dis):
    if loc ==1:
        return dis
    elif loc==4:
        return row+dis
    elif loc==2:
        return row+col+row-dis
    elif loc==3:
        return row+col+row+col-dis
dist=[]
for i in range(shop):
    dist.append(len_check(shop_location[i][0],shop_location[i][1]))
ret = len_check(x[0],x[1])
result=0
for i in range(shop):
    cal_distance=abs(dist[i]-ret)
    result+=min(cal_distance,Round-cal_distance)
print(result)