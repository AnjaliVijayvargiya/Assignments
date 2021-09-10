# Link: https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/
# Python code to find minimum steps to reach to specific cell in minimum moves by Knight
class cell:
     
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
         
# checks whether given position is inside the board
def isInside(x, y, N):
    if (x >= 0 and x <= N and y >= 0 and y <= N):
        return True
    return False
     
# Method returns minimum step to reach target position
def minStepToReachTarget(playerpos, targetpos, N, player):
     
    if(player == "horse"):
        # all possible movments for the knight
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        n = 8
    if(player == "bishop"):
        # all possible movments for the bishop
        dx = [1, 1, -1, -1]
        dy = [1, -1, 1, -1]
        n=4
     
    queue = []
     
    # push starting position of knight with 0 distance
    queue.append(cell(playerpos[0], playerpos[1], 0))
    # print("hi===========",(playerpos[0], playerpos[1], 0))
     
    # make all cell unvisited
    visited = [[False for i in range(N + 1)] for j in range(N + 1)]
     
    # visit starting state
    visited[playerpos[0]][playerpos[1]] = True
     
    # loop until we have one element in queue
    while(len(queue) > 0):
         
        t = queue[0]
        queue.pop(0)
         
        # if current cell is equal to target cell, return its distance
        if(t.x == targetpos[0] and t.y == targetpos[1]):
            return t.dist
             
        # iterate for all reachable states
        for i in range(n):
             
            x = t.x + dx[i]
            y = t.y + dy[i]
             
            if(isInside(x, y, N) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))
 
# Driver Code    
if __name__=='__main__':
    N = 7
    knightpos = [6, 6]
    list_moves_horse = []
    pos_list = []
    for i in range(N+1):
        for j in range(N+1):
            # print([i,j])
            targetpos = [i,j]
            min_moves = minStepToReachTarget(knightpos, targetpos, N,"horse")
            pos_list = [i,j]
            if(min_moves != None):
                list_moves_horse.append([pos_list,min_moves])
    print("horse moves: ",list_moves_horse)
    print('\n')

    bishoppos = [5, 2]
    list_moves_bishop = []
    pos_list = []
    for i in range(N+1):
        for j in range(N+1):
            # print([i,j])
            targetpos = [i,j] #0,1  5,2
            min_moves = minStepToReachTarget(bishoppos, targetpos, N,"bishop")
            pos_list = [i,j]
            if(min_moves != None):
                list_moves_bishop.append([pos_list,min_moves])
    print("bishop moves: ",list_moves_bishop)
    print('\n')
    # targetpos = [6, 0]
    # print(minStepToReachTarget(knightpos, targetpos, N))
     
Blocked_moves = [[0,3],[0,7],[2,0],[2,6],[4,3],[6,7],[7,1]]

for i in Blocked_moves:
    for pos in list_moves_horse:
        # print(pos)
        if(pos[0] == i):
            list_moves_horse.remove(pos)

print("Final possible moves for horse",list_moves_horse)
print('\n')

for i in Blocked_moves:
    for pos in list_moves_bishop:
        # print(pos)
        if(pos[0] == i):
            list_moves_bishop.remove(pos)

print("Final possible moves for bishop",list_moves_bishop)
print('\n')

Matching_Point = []
for i in list_moves_horse:
    for j in list_moves_bishop:
        if(i[0]==j[0]):
            Matching_Point.append(i[0])

print("They can meet at these position: ",Matching_Point)
