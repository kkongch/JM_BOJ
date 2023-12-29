s,p = map(int,input().split())
str = list(input())
a,c,g,t = map(int,input().split())
low, high = 0, p
cnt = 0
dic = {'A' : 0,'C' : 0,'G' : 0,'T' : 0}
for i in str[:p]:
    dic[i] +=1
if dic['A']>=a and dic['C']>=c and dic['G']>=g and dic['T']>=t:
    cnt+=1

for _ in range(s-p):
    dic[str[low]] -= 1
    high += 1
    low += 1
    dic[str[high - 1]] += 1
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1

print(cnt)

