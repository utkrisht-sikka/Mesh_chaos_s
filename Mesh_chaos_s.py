'''
learning:
1.define Grid function before accessing its attributes
2.define Obstacle function before creating its instances
3.define Reward function before creating its instances
4.a=2 shows quite weird behaviour
if a==3:
    print('o3')
elif a==4:
    print('o4')
for i in range(5,10):
    elif a==i:#here it shows error
        print('o'+str(i))
else:
    print('k')

5.It doesnt matter even if class Player is defined after class Grid and used in Grid.
6.o=obstacle(1,2)
  e=obstacle(1,2)
  ids of o and e will be different
IGNORE
1.rotation:anti and clock as greater as 10 times
2.steps of movement as greater as 100
3.crossing all edges
4.crossing all edges from corners
encountering 
1.obstacle
2.reward
3.goal
4.start position
5.same position

1.game over
2.game win

1.n=20
2.n=10go
3.n=5

'''
import os,time,random
cross=[]

def uniq(l):
    '''
    returns a list with only unique elements of l
    '''
    l1=l[:]
    s=[]
    for i in l:
        for k in l1:
            if i!=k and i.x==k.x and i.y==k.y:
                l1.remove(k)
    return l1

    
n=int(input())

s = random.sample(range(n), 2)#each coordinate of s can range from 0 to n-1
g = random.sample(range(n), 2)#creates random coordinates for goal
ob=random.sample(range(n//2,n), 1)[0]#creates random no. of obstacles ranging from 10 to 19
re=random.sample(range(n//2,n), 1)[0]#creates random no. of rewards ranging from 10 to 19

class Obstacle:#represented by '#'
    '''
    x and y are coordinates of obstacle
    '''
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Reward:#represented by number
    '''
    x and y are coordinates of reward
    '''
    def __init__(self,x,y,value):
        self.x=x
        self.y=y
        self.value=value











class Grid:
    N=n
    start=(s[0],s[1])#represented by S in grid
    goal=(g[0],g[1])#represented by G in grid
    myObstacles=[]
    myRewards=[]
    def rotateClockwise(n):
        '''
        I have kept the position of start and goal as same during rotation
        .Changing energy
        Can return 'WON' or 'GAME OVER'
        '''
        a=0
        for k in range(n):
            for i in Grid.myObstacles:#checking whether grid can be rotated or not
                if Grid.N-1-i.y==Player.x and i.x==Player.y:
                    print('grid can\'t be rotated')
                    a=1
            if a!=1:#if grid can be rotated...
                for i in Grid.myObstacles:
                    i.x,i.y=Grid.N-1-i.y,i.x
                for i in Grid.myRewards:
                    i.x,i.y=Grid.N-1-i.y,i.x
                Player.energy-=Grid.N//3#decreasing player's energy
                if Player.energy<0:
                    return 'GAME OVER'
                checkReward()
                os.system('cls')#clearing the system
                Grid.showGrid()
                if Player.x==Grid.goal[0] and Player.y==Grid.goal[1]:
                        return 'WON'
            
    def rotateAnticlockwise(n):    
        '''
        I have kept the position of start and goal as same during rotation
        .Changing energy
        Can return 'WON' or 'GAME OVER'
        '''
        a=0
        for k in range(n):#k=0
            for i in Grid.myObstacles:#checking whether grid can be rotated or not
                if i.y==Player.x and Grid.N-1-i.x==Player.y:
                    print('grid can\'t be rotated')
                    a=1
            if a!=1:#if grid can be rotated...
                Grid.start=(Grid.start[1],Grid.N-1-Grid.start[0])
                for i in Grid.myObstacles:
                    i.x,i.y=i.y,Grid.N-1-i.x
                for i in Grid.myRewards:
                    i.x,i.y=i.y,Grid.N-1-i.x
                Player.energy-=(Grid.N)//3
                if Player.energy<0:
                    return 'GAME OVER'
                checkReward()
                os.system('cls')
                Grid.showGrid()
                if Player.x==Grid.goal[0] and Player.y==Grid.goal[1]:
                        return 'WON'
                
            
    def showGrid():
        '''
        shows the grid
        returns None 
        '''
        d={}
        for i in Grid.myRewards:#creates a dict with keys as x amd y coordinate of reward and their values as values of reward
            d[(i.x,i.y)]=i.value
            
        print('ENERGY:',Player.energy)
        for i in range(Grid.N):#i will indicate row
            for k in range(Grid.N):#k will indicate column
            

                if k==Player.x and i==Player.y:#checks whether i and k are coords of Player 
                    print('O',end=' ')
                elif k==Grid.start[0] and i==Grid.start[1]:
                    print('S',end=' ')
                elif k==Grid.goal[0] and i==Grid.goal[1]:
                    print('G',end=' ')
                elif ((k,i) in list(map(lambda d:(d.x,d.y),Grid.myObstacles))):#checks whether i and k are coords of any obstacle 
                        print('#',end=' ')#if yes,prints 
                elif ((k,i) in list(map(lambda d:(d.x,d.y),Grid.myRewards))):#checks whether i and k are coords of reward j
                        print(d[(k,i)],end=' ')#if yes,prints value of reward using dict d with key as tuple consisting of x and y coordinate of that reward
                elif (k,i) in cross:#prints the trail
                    print('X',end=' ')
                else:
                    print('.',end=' ')
            print()#to move cursor to next line



    





for i in range(ob):#assigning coordinates to obstacles
    o=Obstacle(random.sample(range(n), 1)[0],random.sample(range(n), 1)[0])
    if (o.x==Grid.start[0] and o.y==Grid.start[1]) or (o.x==Grid.goal[0] and o.y==Grid.goal[1]):#ensuring that obstacles dont coincide with start or goal
        pass
    else:
        Grid.myObstacles.append(o)
Grid.myObstacles=uniq(Grid.myObstacles)#removes duplicate obstacles


for i in range(re):#assigning coordinates to rewards
    r=Reward(random.sample(range(n), 1)[0],random.sample(range(n), 1)[0],random.sample(range(1,10),1)[0])#also assigns random value from 1 to 9
    if (r.x==Grid.start[0] and r.y==Grid.start[1]) or (r.x==Grid.goal[0] and r.y==Grid.goal[1]):#ensuring that rewards dont coincide with start or goal
        pass
    else:
        Grid.myRewards.append(r)#initialising myRewards
Grid.myRewards=uniq(Grid.myRewards)#removes duplicate rewards



'''
IGNORE
for i in Grid.myObstacles:#if position of any object and reward coincide then that reward will be removed
    for k in Grid.myRewards:
        if i.x==k.x and i.y==k.y:
            Grid.myRewards.remove(k)
for i in Grid.myObstacles:
    print(str(i.x)+str(i.y),end=' ')
print()

for i in Grid.myRewards:
    print(str(i.x)+str(i.y),end=' ')
'''
print()








class Player:#represented by 'O' in grid
    '''
    x,y are coordinates of player.energy is energy of the player
    '''
    x=Grid.start[0]
    y=Grid.start[1]
    energy=2*Grid.N#initial energy
    def makeMove(s):
        '''
        s is a string
        return :'GAMEOVER' OR 'WON'
        '''
        #print('make')
        le=len(s)
        l=[]
        s=s.upper()
        num=''#a1,le=2,s=A1,i=0
        for i in range(le):#R42D23
            if i!=(le-1):
                if s[i]=='R' or s[i]=='L' or s[i]=='U' or s[i]=='D' or s[i]=='A' or s[i]=='C':
                    if num!='':#if there is some number in num it will be appended to l
                        l.append(int(num))
                        num=''
                    l.append(s[i])#l=[A]
                else:
                    num=num+s[i]#num=A
            else:
                num=num+s[i]
                l.append(int(num))
        '''
        explanation for A1
        
        '''
        #say D41
        #say l=['R',42,'D',23] has been created
        le2=len(l)
        for i in range(0,le2,2):#processing input one by one
            #i=0
            if l[i]=='R':
                for i in range(l[i+1]):
                    cross.append((Player.x,Player.y))
                    Player.x+=1
                    adjust()
                    Player.energy-=1
                    checkObstacle()
                    checkReward()
                    os.system('cls')
                    Grid.showGrid()
                    if Player.energy<=0:
                        return 'GAME OVER'
                    if Player.x==Grid.goal[0] and Player.y==Grid.goal[1]:
                        return 'WON'
            elif l[i]=='L':
                for i in range(l[i+1]):
                    cross.append((Player.x,Player.y))
                    Player.x-=1
                    adjust()
                    Player.energy-=1
                    checkObstacle()
                    checkReward()
                    os.system('cls')
                    Grid.showGrid()
                    if Player.energy<=0:
                        return 'GAME OVER'
                    if Player.x==Grid.goal[0] and Player.y==Grid.goal[1]:
                        return 'WON'
            elif l[i]=='U':
                for i in range(l[i+1]):
                    cross.append((Player.x,Player.y))
                    Player.y-=1#i have taken downward as positive y axis
                    adjust()
                    Player.energy-=1
                    checkObstacle()
                    checkReward()
                    os.system('cls')
                    Grid.showGrid()
                    if Player.energy<=0:
                        return 'GAME OVER'
                    if Player.x==Grid.goal[0] and Player.y==Grid.goal[1]:
                        return 'WON'
            elif l[i]=='D':
                for i in range(l[i+1]):
                    cross.append((Player.x,Player.y))
                    Player.y+=1#i have taken downward as positive y axis
                    adjust()
                    Player.energy-=1
                    checkObstacle()
                    checkReward()
                    os.system('cls')
                    Grid.showGrid()
                    if Player.energy<=0:
                        return 'GAME OVER'
                    if Player.x==Grid.goal[0] and Player.y==Grid.goal[1]:
                        return 'WON'
            elif l[i]=='A':
                #energy has been changed in rotateAnticlockwise()
                return Grid.rotateAnticlockwise(l[i+1])
            elif l[i]=='C':
                #energy has been changed in rotateAnticlockwise()
                return Grid.rotateClockwise(l[i+1])
        while len(cross)!=0:
            cross.pop()#removing coordinates trail from cross list

def checkReward():
    '''
    takes no parametrs
    if player moves to a reward ,it increases energy and deletes that obstacle afterwards
    Return:None
    '''

    for i in Grid.myRewards:
        if Player.x==i.x and Player.y==i.y:
            Player.energy+=(i.value*Grid.N)
            Grid.myRewards.remove(i)
        
def checkObstacle():
    '''
    takes no parametrs
    if player moves to a obstacle ,it decreases energy and deletes that obstacle afterwards
    Return:None
    '''
    for i in Grid.myObstacles:
        if Player.x==i.x and Player.y==i.y:
            Player.energy-=(2*Grid.N)
            Grid.myObstacles.remove(i)
def adjust():
    '''
    if player crosses an edge ,then this function redirects it to other edge.
    It returns None
    '''
    if Player.x==10:
        Player.x=0
    elif Player.x==-1:
        Player.x=9
    if Player.y==10:
        Player.y=0
    elif Player.y==-1:
        Player.y=9

        
os.system('cls')
Grid.showGrid()
while True:#as soon as the energy becomes negative or player reaches the goal ,the game will stop
    '''
    the player wins if he/she reaches the goal at the end of making moving
    the player loses if his/her energy becomes non-postive at the end of making moving
    '''
    s=input()#showGrid() is called inside makeMove()
    
    t=Player.makeMove(s)
    if t=='GAME OVER':
        print('no energy left')
        print('GAMEOVER')
        break
    elif t=='WON':
        print('YOU WON')
        break
    
    

