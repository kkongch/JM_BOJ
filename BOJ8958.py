test_case_num = int(input())
for i in range(test_case_num):
    arr = list(input())
    score = 0
    new_score = 0
    for k in range(len(arr)):
        if arr[k] =='O':
            score +=1
            new_score+= score
        else:
            score=0
    print(new_score)


        

