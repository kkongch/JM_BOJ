n = int(input()) # 재료의 개수
m = int(input()) # 갑옷을 만드는데 필요한 수
num = list(map(int,input().split()))
cnt = 0
num.sort()
low, high = 0, len(num)-1
while(low<high):
    if num[low]+num[high]>m:
        high-=1
    elif num[low]+num[high]<m:
        low+=1
    elif num[low]+num[high]==m:
        cnt+=1
        low+=1
        high-=1
print(cnt)