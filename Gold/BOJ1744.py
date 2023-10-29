n = int(input())
m_lst = [] #음수리스트
p_lst = [] #양수리스트
cnt=0
for i in range(n):
    num = int(input())
    if num<=0:
        if num == 0:
            cnt+=1
        else:
            m_lst.append(num)
    else:
        p_lst.append(num)
result = []
m_lst.sort()
p_lst.sort()
# 양수 일때
if p_lst:
    if 1 not in p_lst:
        #리스트의 길이가 짝수
        if len(p_lst)%2==0:
            for i in range(0,len(p_lst),2):
                result.append(p_lst[i]*p_lst[i+1])
        #리스트의 길이가 홀수
        else:
            result.append(p_lst[0])
            for i in range(1,len(p_lst),2):
                result.append(p_lst[i]*p_lst[i+1])
    else:
        while 1:
            if 1 not in p_lst:
                break
            result.append(1)
            p_lst.pop(0)
        #리스트의 길이가 짝수
        if len(p_lst)%2==0:
            for i in range(0,len(p_lst),2):
                result.append(p_lst[i] * p_lst[i + 1])
        #리스트의 길이가 홀수
        if len(p_lst)%2 ==1:
            result.append(p_lst[0])
            for i in range(1, len(p_lst), 2):
                result.append(p_lst[i] * p_lst[i + 1])
# 음수일때
if cnt:
    if len(m_lst)%2 ==0:
        for i in range(0,len(m_lst),2):
            result.append(m_lst[i]*m_lst[i+1])
    if len(m_lst)%2 ==1:
        m_lst.pop()
        for i in range(0,len(m_lst),2):
            result.append(m_lst[i]*m_lst[i+1])
else:
    if len(m_lst)%2 ==0:
        for i in range(0,len(m_lst),2):
            result.append(m_lst[i]*m_lst[i+1])
    if len(m_lst)%2 ==1:
        result.append(m_lst[-1])
        m_lst.pop()
        for i in range(0,len(m_lst),2):
            result.append(m_lst[i]*m_lst[i+1])

print(sum(result))