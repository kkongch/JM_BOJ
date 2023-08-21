from pprint import pprint
bingo = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]
new_call = []
for i in range(5):
    for k in range(5):
        new_call.append(call[i][k])
def bingo_check(bingo):
    global cnt
    for i in range(5):
        flag_row = 0
        flag_col = 0
        for k in range(5):
            if bingo[i][k]==0:
                flag_row+=1
            if bingo[k][i]==0:
                flag_col+=1
        if flag_row == 5:
            cnt+=1
        if flag_col == 5 :
            cnt+=1
    diag = 0
    for i in range(5):
        if bingo[i][i]==0:
            diag+=1
    if diag == 5:
        cnt+=1
    start = 0
    rev_diag = 0
    for k in range(4,-1,-1):
        if bingo[start][k]==0:
            rev_diag+=1
        start+=1
    if rev_diag==5:
        cnt+=1

result = 0


for j in range(len(new_call)):
    result += 1
    cnt = 0
    for i in range(5):
        for k in range(5):
            if bingo[i][k]==new_call[j]:
                bingo[i][k]=0
                bingo_check(bingo)
                if cnt >= 3:
                    break
        if cnt >= 3:
            break
    if cnt>=3:
        break
print(result)