def find_minimun(row,col,triangle):
    if row== len(triangle):
        return 0
    else:
        pl= find_minimun(row + 1,col,triangle)
        pr= find_minimun(row + 1,col +1 ,triangle)
        minimun = min( pl, pr )
    return triangle[row][col]+ minimun

triangle = [
    [2],
    [3,4]
]

minimun=find_minimun(0,0,triangle)
print('El minimo costo es' , minimun)

''' 
Left:
[0][0] = 2
[1][0] = 3
[2][0] => 0 DONE(0)

Right:
[2][1] => 0 DONE(0)
[1][1]=> 3

'''

''' 
Left side execution:
(0,0) = 2 :=> 2

(1,0) = 3 :=> 3
(2,0) = 6 :=> 6
(3,0) = 4 :=> 4 + 0 = 4
(4,0) = 0 :=> 0

Right side execution:
At time of starting right side the states for variables was: row = 4, col = 0
(4,1) => 0
(3,1) = 1 :=> 1
(2,1) = 5 :=> 5
(1,1) = 4 :=> 4

# Using the execution values:
minum = min(4,0)
=> [0]

'''


def find_min( triangle : list ):
    minSum = 0
    
    for x in range(len(triangle)):
        minSum += min( triangle[x] )
    
    return minimun

minimun = find_min(triangle)
print('El minimo costo es' , minimun)
