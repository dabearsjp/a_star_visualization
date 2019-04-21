from random import randint

squares = 75
        
class Spot:
    
    def __init__(self, i, j):
        self.g = float("inf")
        self.f = float("inf")
        self.h = float("inf")
        self.i = i
        self.j = j
        self.goal = False
        self.start = False
        self.neighbors = []
        self.came_from = 0
        self.wall = False
        
    def show(self, r, g, b):
        if self.goal == True:
            fill(255, 255, 0)
        elif self.start == True:
            fill(255, 0, 255)
        else:
            fill(r, g, b)
        rect(self.i * width/squares, self.j * height/squares, width/squares - 1, height/squares - 1)
        


start = False

grid = []


for i in range(squares):
    inner = []
    for j in range(squares):
        inner.append(Spot(i, j))
    grid.append(inner)
        
closed_set = []
open_set = []



def get_lowest_f():
    lowest = open_set[0]
    for i in open_set:
        if i.f < lowest.f:
            lowest = i
    
    return lowest

starting = grid[randint(0, squares - 1)][randint(0, squares - 1)]
starting.start = True
starting.g = 0
open_set.append(starting)

ending = grid[randint(0, squares - 1)][randint(0, squares - 1)]
ending.goal = True

for i in range(len(grid)):
    for j in grid[i]:
        rand = randint(0, 10)
        if rand <= 2 and j != ending:
            j.wall = True
            
def reconstruct():
    path = [ending]
    while path[-1] != starting:
        path.append(path[-1].came_from)
    return path
    
def update():
    for i in range(len(grid)):
        for j in grid[i]:
            if j in open_set and j.start == False:
                j.show(0, 255, 0)
            elif j.wall == True:
                j.show(0, 0, 0)
            elif j in closed_set and j.start == False:
                j.show(255, 0, 0)
            else:
                j.show(255, 255, 255)
                
def a_star():
    global grid
    update()
    if len(open_set) > 0:
        current = get_lowest_f()
        if current == ending:
            for i in reconstruct():
                i.show(0, 0, 255)
            return 0
        open_set.remove(current)
        closed_set.append(current)
        if current.i != 0: 
            if grid[current.i - 1][current.j].wall != True:
                current.neighbors.append(grid[current.i - 1][current.j])  
        if current.i != squares - 1:
            if grid[current.i + 1][current.j].wall != True:
                current.neighbors.append(grid[current.i + 1][current.j])
        if current.j != 0:
            if grid[current.i][current.j - 1].wall != True:
                current.neighbors.append(grid[current.i][current.j - 1])
        if current.j != squares - 1:
            if grid[current.i][current.j + 1].wall != True:
                current.neighbors.append(grid[current.i][current.j + 1])
        if current.i != 0 and current.j != 0:
            if grid[current.i - 1][current.j - 1].wall != True:
                current.neighbors.append(grid[current.i - 1][current.j - 1])
        if current.i != squares - 1 and current.j != squares - 1:
            if grid[current.i + 1][current.j + 1].wall != True:
                current.neighbors.append(grid[current.i + 1][current.j + 1])
        if current.i != squares - 1 and current.j != 0:
            if grid[current.i + 1][current.j - 1].wall != True:
                current.neighbors.append(grid[current.i + 1][current.j - 1])
        if current.i != 0 and current.j != squares - 1:
            if grid[current.i - 1][current.j + 1].wall != True:
                current.neighbors.append(grid[current.i - 1][current.j + 1])
        for i in current.neighbors:
            if i in closed_set:
                continue
            temp_g = current.g + 1
            if i not in open_set:
                open_set.append(i)
            elif temp_g <= i.g:
                continue
            i.came_from = current
            i.g = temp_g
            i.f = i.g + abs(i.i - ending.i) + abs(i.j - ending.j)
    else:
        return "no path"
    
def setup():
    size(500, 500)
    a_star()

    
def draw():
    update()
    if start == True:    
        a_star()
    
def keyPressed():
    global start
    if key == " ":
        start = True
    

        
        

def mousePressed():
    x = mouseX / (width/squares)
    if x % 1 != 0:
        x = int(x) + 1
    y = mouseY / (height/squares)
    if y % 1 != 0:
        y = int(y) + 1
    if grid[x][y].wall == False:
        grid[x][y].wall = True
    elif grid[x][y].wall == True:
        grid[x][y].wall = False
    update()
    
