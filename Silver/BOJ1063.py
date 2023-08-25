lst = list(input().split())
king = [ord(lst[0][0])-ord('A'),int(lst[0][1])]
rock = [ord(lst[1][0])-ord('A'),int(lst[1][1])]
directx = [1,-1,0,0,1,-1,1,-1]
directy = [0,0,-1,1,1,1,-1,-1]

for i in range(int(lst[2])):
    move = input()
    if move=='R':
        dy = directy[0] + king[1]
        dx = directx[0] + king[0]
        if dy<1 or dx<0 or dx>7 or dy>8:
            continue
        king[1] += directy[0]
        king[0] += directx[0]

        if king == rock:
            r_dy = directy[0] + rock[1]
            r_dx = directx[0] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[0]
                king[0] -= directx[0]
                continue
            rock[1]+=directy[0]
            rock[0]+=directx[0]
    elif move == 'L':
        dy = directy[1] + king[1]
        dx = directx[1] + king[0]
        if dy < 1 or dx < 0 or dx > 7 or dy > 8:
            continue
        king[1] += directy[1]
        king[0] += directx[1]

        if king == rock:
            r_dy = directy[1] + rock[1]
            r_dx = directx[1] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[1]
                king[0] -= directx[1]
                continue
            rock[1] += directy[1]
            rock[0] += directx[1]
    elif move == 'B':
        dy = directy[2] + king[1]
        dx = directx[2] + king[0]
        if dy < 1 or dx < 0 or dx > 7 or dy > 8:
            continue
        king[1] += directy[2]
        king[0] += directx[2]

        if king == rock:
            r_dy = directy[2] + rock[1]
            r_dx = directx[2] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[2]
                king[0] -= directx[2]
                continue
            rock[1] += directy[2]
            rock[0] += directx[2]
    elif move == 'T':
        dy = directy[3] + king[1]
        dx = directx[3] + king[0]
        if dy < 1 or dx < 0 or dx > 7 or dy > 8:
            continue
        king[1] += directy[3]
        king[0] += directx[3]

        if king == rock:

            r_dy = directy[3] + rock[1]
            r_dx = directx[3] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[3]
                king[0] -= directx[3]
                continue
            rock[1] += directy[3]
            rock[0] += directx[3]
    elif move == 'RT':
        dy = directy[4] + king[1]
        dx = directx[4] + king[0]
        if dy < 1 or dx < 0 or dx > 7 or dy > 8:
            continue
        king[1] += directy[4]
        king[0] += directx[4]


        if king == rock:
            r_dy = directy[4] + rock[1]
            r_dx = directx[4] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[4]
                king[0] -= directx[4]
                continue
            rock[1] += directy[4]
            rock[0] += directx[4]
    elif move == 'LT':
        dy = directy[5] + king[1]
        dx = directx[5] + king[0]
        if dy < 1 or dx < 0 or dx > 7 or dy > 8:
            continue
        king[1] += directy[5]
        king[0] += directx[5]


        if king == rock:
            r_dy = directy[5] + rock[1]
            r_dx = directx[5] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[5]
                king[0] -= directx[5]
                continue
            rock[1] += directy[5]
            rock[0] += directx[5]
    elif move == 'RB':
        dy = directy[6] + king[1]
        dx = directx[6] + king[0]
        if dy < 1 or dx < 0 or dx > 7 or dy > 8:
            continue
        king[1] += directy[6]
        king[0] += directx[6]


        if king == rock:
            r_dy = directy[6] + rock[1]
            r_dx = directx[6] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[6]
                king[0] -= directx[6]
                continue
            rock[1] += directy[6]
            rock[0] += directx[6]
    elif move == 'LB':
        dy = directy[7] + king[1]
        dx = directx[7] + king[0]
        if dy < 1 or dx < 0 or dx > 7 or dy > 8:
            continue
        king[1] += directy[7]
        king[0] += directx[7]

        if king == rock:
            r_dy = directy[7] + rock[1]
            r_dx = directx[7] + rock[0]
            if r_dy < 1 or r_dx < 0 or r_dx > 7 or r_dy > 8:
                king[1] -= directy[7]
                king[0] -= directx[7]
                continue
            rock[1] += directy[7]
            rock[0] += directx[7]
print(f'{chr(ord("A")+king[0])}{king[1]}')
print(f'{chr(ord("A")+rock[0])}{rock[1]}')