# Given
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
# Task to do --> Replace 1 to * and 0 to space
for i in picture:
    for j in i:
        if j==1:
            print("*",end='')
        elif j==0:
            print(" ",end='')
    print('\n')
